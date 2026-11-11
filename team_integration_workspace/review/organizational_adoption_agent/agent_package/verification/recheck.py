#!/usr/bin/env python3
"""Recheck saved TW8 artifacts. Standard library only; no model or network call."""
from pathlib import Path
import json, hashlib, subprocess, sys, tempfile, copy, csv
ROOT=Path(__file__).resolve().parents[1];CHECKS=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads((ROOT/p).read_text())
def check(n,v):CHECKS.append({'check':n,'passed':bool(v)})
def valid(d,s):
 types={'object':dict,'array':list,'string':str}
 if s.get('type') in types and not isinstance(d,types[s['type']]):return False
 if isinstance(d,dict):
  props=s.get('properties',{})
  if any(k not in d for k in s.get('required',[])):return False
  if s.get('additionalProperties') is False and any(k not in props for k in d):return False
  return all(valid(v,props[k]) for k,v in d.items() if k in props)
 if isinstance(d,list) and 'items' in s:return all(valid(v,s['items']) for v in d)
 return True
for line in (ROOT/'FROZEN_CORE_SHA256.txt').read_text().splitlines():
 if line.strip():
  expect,p=line.split(None,1);check('frozen '+p.strip(),sha(ROOT/p.strip())==expect)
for r in load('evidence/scaffold_inventory.json')['files']:check('canonical original '+r['path'],sha(ROOT/r['path'])==r['sha256'])
snap=load('evidence/member_snapshot_manifest.json')['files']
for r in snap:check('source snapshot '+r['path'],sha(ROOT/r['path'])==r['sha256'])
I=load('core/input_schema.json');O=load('core/output_schema.json');META=load('agents/organizational_adoption_agent/agent_metadata.json')
FRAME=load('records/readiness_framework.json');D=[r['id'] for r in FRAME['dimensions']]
EXPECTED={r['case']:r['verdict'] for r in load('records/test_and_failure_log.json')['current_cases']}
A=ROOT/'agents/organizational_adoption_agent';cases={};answers={};runs=[]
with tempfile.TemporaryDirectory(prefix='tw8-recheck-') as t:
 for p in sorted((A/'cases').glob('*.json')):
  n=p.stem;c=json.loads(p.read_text());r=load('agents/organizational_adoption_agent/responses/'+n+'_response.json');cases[n]=c;answers[n]=r;profile=json.loads(c['capabilities_constraints'])
  check(n+' input schema',valid(c,I));check(n+' output schema',valid(r,O));check(n+' exact top-level keys',set(r)==set(O['required']))
  response=A/'responses'/(n+'_response.json')
  check(n+' instructor validator',subprocess.run([sys.executable,str(ROOT/'tools/validate_response.py'),str(response)],capture_output=True).returncode==0)
  check(n+' team metadata',r['agent']==META)
  check(n+' eight dimensions input',set(profile['domains'])==set(D));check(n+' eight dimensions output',all(d in r['organization_specific_finding'] for d in D))
  check(n+' declared fixture verdict',r['organization_specific_finding'].startswith(EXPECTED[n]) and r['recommendation_management_implication'].startswith(EXPECTED[n]))
  check(n+' routine boundary','ROUTINE_READINESS_NOT_ESTABLISHED' in r['organization_specific_finding'])
  check(n+' factual status labels',all(v['status'] in FRAME['statuses'] for v in profile['domains'].values()))
  check(n+' nonempty targeted questions',bool(r['abstention_or_more_information_needed']))
  check(n+' dated source limits',all(e['date_or_recency'] and e['notes'] for e in r['evidence']))
  packet=Path(t)/(n+'.txt');subprocess.run([sys.executable,str(ROOT/'tools/build_prompt.py'),'--agent',str(A),'--case',str(p),'--out',str(packet)],check=True,stdout=subprocess.DEVNULL)
  saved=A/'prompts'/(n+'_prompt.txt');check(n+' exact prompt reconstruction',packet.read_bytes()==saved.read_bytes())
  runs.append({'case':n,'case_sha256':sha(p),'prompt_sha256':sha(saved),'response_sha256':sha(response),'declared_fixture_verdict':EXPECTED[n]})
 for row in load('evidence/common_walkthroughs/results.json'):
  m={'Yufei Cai':'yufei','Chutong Wang':'chutong','Jianbo Sun':'jianbo','Minghan Liu':'minghan'}[row['candidate']]
  agent=ROOT/'evidence/member_snapshots'/m/'specialist';packet=Path(t)/(m+'_'+row['case']+'.txt')
  subprocess.run([sys.executable,str(ROOT/'tools/build_prompt.py'),'--agent',str(agent),'--case',str(A/'cases'/(row['case']+'.json')),'--out',str(packet)],check=True,stdout=subprocess.DEVNULL)
  check(m+' '+row['case']+' common input hash',sha(A/'cases'/(row['case']+'.json'))==row['case_sha256'])
  check(m+' '+row['case']+' original instruction hash',sha(agent/'specialist_instructions.md')==row['instruction_sha256'])
  check(m+' '+row['case']+' exact candidate packet',packet.read_bytes()==(ROOT/row['prompt']).read_bytes() and sha(packet)==row['prompt_sha256'])
base=cases['primary'];prepared=cases['prepared_contrast']
check('material organizational contrast only', {k for k in base if base[k]!=prepared[k]}=={'organization','capabilities_constraints'})
check('permission-only isolated', {k for k in base if base[k]!=cases['permission_only'][k]}=={'capabilities_constraints'})
for n in ['recurring_budget_unknown','trial_capacity_unknown','capacity_shortfall','ownership_loss']:
 check(n+' isolated top-level change',{k for k in prepared if prepared[k]!=cases[n][k]}=={'capabilities_constraints'})
 changes=[d for d in D if json.loads(prepared['capabilities_constraints'])['domains'][d]!=json.loads(cases[n]['capabilities_constraints'])['domains'][d]]
 check(n+' one domain only',changes==(['operating_ownership'] if n=='ownership_loss' else ['resources_budget']))
check('simpler task probe isolated',{k for k in prepared if prepared[k]!=cases['simpler_task_probe'][k]}=={'intended_application'})
for n,r in answers.items():
 check(n+' stable technology finding',r['general_et_finding']==answers['primary']['general_et_finding'])
 check(n+' application evidence appropriately stable',r['application_finding']==answers['primary']['application_finding'] if n!='simpler_task_probe' else r['application_finding']!=answers['primary']['application_finding'])
unknown=answers['trial_capacity_unknown']['organization_specific_finding']+answers['trial_capacity_unknown']['recommendation_management_implication']
check('unknown trial capacity imports no demand numbers',all(s not in unknown for s in ['40 tasks','12 complete','8h','9 protected','32 hours']))
check('unknown capacity question affects judgment','MORE_EVIDENCE_REQUIRED' in unknown and 'protected' in str(answers['trial_capacity_unknown']['abstention_or_more_information_needed']))
check('recurring unknown does not revoke funded trial',answers['recurring_budget_unknown']['organization_specific_finding'].startswith('CONDITIONALLY_READY_FOR_ISOLATED_LEARNING'))
check('owner loss blocks despite sponsor',answers['ownership_loss']['organization_specific_finding'].startswith('NOT_READY'))
check('known capacity shortage blocks',answers['capacity_shortfall']['organization_specific_finding'].startswith('NOT_READY'))
check('no-buffer ceiling qualified','not an automatically safe' in answers['capacity_shortfall']['recommendation_management_implication'])
check('prepared actions avoid duplicated establishment','Do not re-establish' in answers['prepared_contrast']['recommendation_management_implication'])
check('simpler probe preserves organizational evidence','supplied organizational learning arrangements remain supported' in answers['simpler_task_probe']['organization_specific_finding'])
check('simpler probe returns fit to Adoption','Adoption' in answers['simpler_task_probe']['recommendation_management_implication'])
check('capacity and cap arithmetic',40*12/60==8 and 8-4==4 and 4+5+9+4+2==24 and 9-8==1)
# Negative schema controls ensure this checker rejects types, missing fields and extras.
bad=copy.deepcopy(answers['primary']);bad['invented_readiness_score']=100;check('reject extra output key',not valid(bad,O))
bad=copy.deepcopy(answers['primary']);bad.pop('evidence');check('reject missing evidence',not valid(bad,O))
bad=copy.deepcopy(answers['primary']);bad['evidence'][0]['claim']=17;check('reject nested wrong type',not valid(bad,O))
check('eight current cases',len(cases)==8)
check('four candidate sources',set(r['member'] for r in snap)=={'yufei','chutong','jianbo','minghan'})
check('eight common walkthroughs',len(load('evidence/common_walkthroughs/results.json'))==8)
check('eight framework dimensions',len(D)==8)
check('three traced priorities',len(load('records/prioritized_actions.json'))==3 and all(r['owner'] and r['closure'] and r['dependency'] for r in load('records/prioritized_actions.json')))
check('frozen intake unchanged with11 content requirements',load('records/intake_requirements.json')['schema_changed'] is False and len(load('records/intake_requirements.json')['fields'])==11)
check('team acceptance actual reply',load('records/team_release.json')['user_confirmation']=='团队认可，可标记为认可版')
check('publication authorized without merge',load('records/team_release.json')['publication_authorization']=='同意上传并创建待审核 PR' and load('records/team_release.json')['merge_authorized'] is False)
weak=load('evidence/member_snapshots/minghan/specialist/tests/cycle_1/contrast_1_response.json')
check('preserved actual source maturity conflation','readiness offsets' in weak['organization_specific_finding'])
check('weak source generic committee retained','governance committee' in weak['recommendation_management_implication'])
check('intentional negative provenance retained','deliberate' in (ROOT/'records/candidate_comparison.md').read_text().lower())
result={'passed':sum(x['passed'] for x in CHECKS),'total':len(CHECKS),'all_passed':all(x['passed'] for x in CHECKS),'scope':'Saved-artifact bytes/contracts, exact packets, attributed evidence, controlled isolation, declared qualitative fixtures and arithmetic. No model is invoked; this is not a future-output reliability or independent benchmark score.','checks':CHECKS}
prov={'date':'2026-11-10','runtime':'Current ChatGPT/Codex assistant, no separate inference API or independent evaluator','method':'The assistant reasoned and authored current case-specific examples and candidate-rule walkthroughs. Python serializes authored content, builds exact prompt packets and checks saved artifacts. It does not execute a deployed chart tool or independently infer these answers. General/application wording is deliberately controlled for invariance.','cases':runs,'candidate_walkthrough_count':8,'current_team_case_count':8,'original_failure_context':'Native member source failures remain original and attributed; deliberate negative controls are identified, not represented as deployed incidents.'}
(ROOT/'verification/run_provenance.json').write_text(json.dumps(prov,indent=2)+'\n')
(ROOT/'verification/validation_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(f"{result['passed']}/{result['total']} local artifact checks passed")
for x in CHECKS:
 if not x['passed']:print('FAIL:',x['check'])
if not result['all_passed']:sys.exit(1)
