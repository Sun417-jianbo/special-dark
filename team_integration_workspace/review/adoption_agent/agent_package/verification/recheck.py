#!/usr/bin/env python3
"""Recheck saved TW7 artifacts. No model call, deployment or benchmark is performed."""
from pathlib import Path
import json,hashlib,subprocess,sys,tempfile,csv
ROOT=Path(__file__).resolve().parents[1];checks=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(rel):return json.loads((ROOT/rel).read_text())
def check(label,ok):checks.append({'check':label,'passed':bool(ok)})
def valid(d,s):
    types={'object':dict,'array':list,'string':str}
    if s.get('type') in types and not isinstance(d,types[s['type']]):return False
    if isinstance(d,dict):
        props=s.get('properties',{})
        if any(k not in d for k in s.get('required',[])):return False
        if s.get('additionalProperties') is False and any(k not in props for k in d):return False
        return all(valid(v,props[k]) for k,v in d.items() if k in props)
    if isinstance(d,list) and 'items' in s:return all(valid(x,s['items']) for x in d)
    return True
for line in (ROOT/'FROZEN_CORE_SHA256.txt').read_text().splitlines():
    if line.strip():
        expected,rel=line.split(None,1);check('frozen '+rel.strip(),sha(ROOT/rel.strip())==expected)
for r in load('evidence/scaffold_inventory.json')['files']:check('canonical original '+r['path'],sha(ROOT/r['path'])==r['sha256'])
for r in load('evidence/candidate_snapshot_manifest.json'):check('candidate bytes '+r['snapshot'],sha(ROOT/r['snapshot'])==r['sha256'])
for r in load('evidence/upstream_manifest.json'):check('upstream bytes '+r['snapshot'],sha(ROOT/r['snapshot'])==r['sha256'])
for r in load('evidence/candidate_core_audit.json'):check(r['owner']+' seven original frozen files audited',len(r['frozen_files'])==7 and all(x['matches_canonical'] for x in r['frozen_files']))
intake=load('core/input_schema.json');output=load('core/output_schema.json');meta=load('agents/adoption_agent/agent_metadata.json')
expected={r['case']:r['primary_action'] for r in load('records/decision_table.json')};cases={};responses={};provenance=[]
with tempfile.TemporaryDirectory(prefix='tw7-recheck-') as tmp:
    for p in sorted((ROOT/'agents/adoption_agent/cases').glob('*.json')):
        name=p.stem;case=json.loads(p.read_text());cases[name]=case
        response=ROOT/'agents/adoption_agent/responses'/f'{name}_response.json';r=json.loads(response.read_text());responses[name]=r
        check(name+' intake schema keywords',valid(case,intake));check(name+' frozen output schema keywords',valid(r,output))
        v=subprocess.run([sys.executable,str(ROOT/'tools/validate_response.py'),str(response)],capture_output=True)
        check(name+' supplied response validator',v.returncode==0)
        check(name+' current metadata',r['agent']==meta)
        action=r['recommendation_management_implication'].split(' — ',1)[0]
        check(name+' declared primary action',action==expected[name])
        check(name+' next-specialist boundary','Organizational Adoption' in r['risk_governance_implication'])
        check(name+' dated bounded evidence',all(e['date_or_recency'] and e['notes'] for e in r['evidence']))
        rebuilt=Path(tmp)/(name+'.txt')
        subprocess.run([sys.executable,str(ROOT/'tools/build_prompt.py'),'--agent','agents/adoption_agent','--case',str(p),'--out',str(rebuilt)],capture_output=True,check=True)
        prompt=ROOT/'agents/adoption_agent/prompts'/f'{name}_prompt.txt'
        check(name+' exact prompt rebuild',rebuilt.read_bytes()==prompt.read_bytes())
        check(name+' general evidence invariant',r['general_et_finding']==load('agents/adoption_agent/responses/primary_response.json')['general_et_finding'])
        provenance.append({'case':name,'case_sha256':sha(p),'prompt_sha256':sha(prompt),'response_sha256':sha(response),'action':action})
    for row in load('comparison/run_manifest.json'):
        owner=row['candidate'];name=row['case'];prefix=owner+' '+name
        r=load(row['response']);candidate=ROOT/'evidence/candidates'/owner/'agents/adoption_agent'
        check(prefix+' output contract',valid(r,output));check(prefix+' original candidate metadata',r['agent']==json.loads((candidate/'agent_metadata.json').read_text()))
        check(prefix+' declared walkthrough action',r['recommendation_management_implication'].split(' — ',1)[0]==row['action'])
        rebuilt=Path(tmp)/(owner+'_'+name+'.txt')
        subprocess.run([sys.executable,str(ROOT/'tools/build_prompt.py'),'--agent',str(candidate),'--case',str(ROOT/'agents/adoption_agent/cases'/f'{name}.json'),'--out',str(rebuilt)],capture_output=True,check=True)
        check(prefix+' exact common-case packet',rebuilt.read_bytes()==(ROOT/row['prompt']).read_bytes())
def diff(a,b):return [k for k in a if a[k]!=b[k]]
a=cases['primary'];b=cases['posture_contrast'];c=cases['learning_permission_conservative'];d=cases['learning_permission_aggressive']
check('primary contrast changes only posture',diff(a,b)==['adoption_posture'])
check('permission contrast changes only constraints',diff(a,c)==['capabilities_constraints'])
check('K1 contrast changes only posture',diff(c,d)==['adoption_posture'])
for field in ['general_et_finding','application_finding','evidence','confidence_and_uncertainty','risk_governance_implication']:
    check('baseline posture invariant '+field,responses['primary'][field]==responses['posture_contrast'][field])
    check('K1 posture invariant '+field,responses['learning_permission_conservative'][field]==responses['learning_permission_aggressive'][field])
check('hard blocker defeats aggressive enthusiasm',expected['primary']==expected['posture_contrast']=='DEFER')
check('K1 action changes for learning preference',expected['learning_permission_conservative']=='MONITOR' and expected['learning_permission_aggressive']=='PROOF_OF_CONCEPT')
check('baseline desk research is not trial permission','does not authorize executing an agent trial' in a['capabilities_constraints'])
check('aggressive urgency changes, not permission','within two weeks' in responses['posture_contrast']['recommendation_management_implication'])
check('PoC eight-hour two-week cap','eight analyst-hours over two weeks' in responses['learning_permission_aggressive']['recommendation_management_implication'])
check('H1 separately permitted and not routine','sixteen total analyst-hours' in responses['qualified_experiment']['recommendation_management_implication'] and 'production value remains unknown' in cases['qualified_experiment']['capabilities_constraints'])
check('H2 replaces baseline unknowns','replaces baseline unknowns' in responses['staged_adoption']['application_finding'])
check('H2 separately supplied readiness','separately supplied Organizational Adoption' in responses['staged_adoption']['recommendation_management_implication'])
check('H2 scope one team','one reporting team' in responses['staged_adoption']['recommendation_management_implication'])
check('H2 full prospective cost approval','prospective total cost/budget' in cases['staged_adoption']['capabilities_constraints'])
check('positive sample is not zero risk','not proof of zero risk' in responses['staged_adoption']['application_finding'])
check('all six actions exercised',set(expected.values())=={'DEFER','MONITOR','PROOF_OF_CONCEPT','BOUNDED_EXPERIMENT','ADOPT','REJECT_FOR_PRESENT'})
check('missing application is truly empty',cases['missing_application']['intended_application']=='')
check('missing scope withholds finding','withheld' in responses['missing_application']['application_finding'])
check('hype appends context only',diff(a,cases['hype_probe'])==['additional_context'])
check('hype does not promote action',expected['hype_probe']==expected['primary'])
check('unsafe request rejected','unsafe upload' in responses['hype_probe']['recommendation_management_implication'])
check('confounded demo appends only context',diff(d,cases['confounded_pilot'])==['additional_context'])
check('confounded demo does not promote adoption',expected['confounded_pilot']==expected['learning_permission_aggressive'])
check('confounding arithmetic correct',abs(0.85/0.80-1.0625)<1e-10 and '6.25%' in responses['confounded_pilot']['organization_specific_finding'])
effort={'status':'Fictional H3 arithmetic; not observed results or financial ROI','manual_minutes':100*30,'deterministic_minutes':100*20,'agent_minutes':100*(3+12+7)+300,'past_sunk_excluded_minutes':300,'volume_adjusted_demo_ratio':0.85/0.80}
check('best baseline arithmetic',effort['agent_minutes']-min(effort['manual_minutes'],effort['deterministic_minutes'])==500)
check('best adequate alternative not only manual','best adequate' in responses['inferior_alternative']['recommendation_management_implication'])
check('sunk and prospective support separated','past 300-minute sunk' in responses['inferior_alternative']['recommendation_management_implication'])
for owner in ['yufei_cai','chutong_wang','jianbo_sun','minghan_liu']:
    primary=load(f'comparison/walkthroughs/{owner}_primary.json');contrast=load(f'comparison/walkthroughs/{owner}_posture_contrast.json')
    check(owner+' walkthrough general invariant',primary['general_et_finding']==contrast['general_et_finding'])
check('twelve common walkthroughs',len(load('comparison/run_manifest.json'))==12)
weak=load('evidence/candidates/minghan_liu/agents/adoption_agent/tests/cycle_1/contrast_1_response.json')
check('prior posture reclassification failure preserved','effectively leading edge' in weak['organization_specific_finding'])
old_inventory=(ROOT/'evidence/upstream/team_agent_inventory.csv').read_text()
check('inherited metadata failure preserved','Risk, Ethics & Regulatory' in old_inventory)
with (ROOT.parent/'shared_records/team_agent_inventory.csv').open(newline='') as f:inventory=list(csv.DictReader(f))
labels=['Technology Creation','Innovation Classification','Promethean Classification','Emerging Technology Diffusion','Emerging Technology Adoption','Organizational Adoption','Technology Landscape']
check('seven teacher-aligned specialist slots',[r['specialty'] for r in inventory]==labels)
check('Adoption is slot 5',inventory[4]['slot']=='5' and inventory[4]['team_lab']=='Team Lab 7')
release=load('records/team_release.json');production=load('records/production_record.json')
check('team acceptance explicitly recorded',release['status']=='team_accepted' and release['confirmation_zh']=='团队认可，可标记为认可版')
check('public review publication authorized',load('records/user_authorization.json')['reply_zh']=='同意上传并创建待审核 PR')
check('no fabricated attendance percentage',production['user_reported_absence'] and production['attendance_or_in_class_percentage_claimed'] is False)
check('four material source contributions',len(load('records/candidate_comparison.json'))==4)
check('ten final team cases',len(cases)==10)
record={'date':'2026-11-03','runtime':'Current ChatGPT/Codex assistant; no external inference API or isolated independent evaluator','method':'The assistant reasoned through and authored the qualitative responses. Scripts serialize examples, construct exact packets and validate saved artifacts. Expected actions are declared analytical fixtures, not a benchmark oracle.','limits':['Candidate-rule walkthroughs are not measured rankings or independent model executions','Shared wording/invariance is deliberate, not a replicated reliability result','K1/H1-H3 are fictional permission/evidence controls; no chart system or company pilot was deployed','Team acceptance is user-reported; attendance and 90% classroom production are not asserted'],'instructions_sha256':sha(ROOT/'agents/adoption_agent/specialist_instructions.md'),'cases':provenance}
for rel,data in [('verification/effort_comparison.json',effort),('verification/run_provenance.json',record)]:
    (ROOT/rel).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
result={'passed':sum(x['passed'] for x in checks),'total':len(checks),'all_passed':all(x['passed'] for x in checks),'scope':'Artifact bytes, frozen-schema keywords, exact prompts, declared case relations/actions, attribution and arithmetic; not measured future LLM reliability','checks':checks}
(ROOT/'verification/validation_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(f"{result['passed']}/{result['total']} local artifact checks passed")
for row in checks:
    if not row['passed']:print('FAIL:',row['check'])
if not result['all_passed']:sys.exit(1)
