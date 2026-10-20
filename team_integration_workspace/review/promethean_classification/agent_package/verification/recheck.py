"""Check saved contracts, explicit fixtures and integrity; never call a model."""
from pathlib import Path
import json,hashlib,subprocess,sys,copy
P=Path(__file__).resolve().parents[1];A=P/'agents/promethean_classification_agent';checks=[]
def read(p):return json.loads(p.read_text())
def check(name,ok,detail=''):checks.append({'check':name,'passed':bool(ok),'detail':detail})
def errors(v,s,loc='$'):
 if set(s)-{'$schema','title','type','required','properties','items','additionalProperties'}:return [loc+' unsupported keyword']
 kinds={'object':dict,'array':list,'string':str}
 if not isinstance(v,kinds.get(s.get('type'),type(None))):return [loc+' wrong type']
 e=[]
 if isinstance(v,dict):
  e += [loc+' missing '+k for k in s.get('required',[]) if k not in v]
  if s.get('additionalProperties') is False:e += [loc+' extra '+k for k in v if k not in s.get('properties',{})]
  for k,sub in s.get('properties',{}).items():
   if k in v:e+=errors(v[k],sub,loc+'.'+k)
 if isinstance(v,list):
  for i,item in enumerate(v):e+=errors(item,s['items'],loc+f'[{i}]')
 return e
ins=read(P/'core/input_schema.json');outs=read(P/'core/output_schema.json');meta=read(A/'agent_metadata.json')
frozen=subprocess.run([sys.executable,str(P/'tools/check_frozen_core.py')],text=True,capture_output=True)
check('seven frozen files unchanged',frozen.returncode==0,frozen.stdout.strip())
cases={p.stem:read(p) for p in (A/'cases').glob('*.json')};rs={}
for name,c in sorted(cases.items()):
 r=read(A/'responses'/f'{name}_response.json');rs[name]=r
 check(name+' input contract',not errors(c,ins),str(errors(c,ins)))
 check(name+' output contract',not errors(r,outs),str(errors(r,outs)))
 v=subprocess.run([sys.executable,str(P/'tools/validate_response.py'),str(A/'responses'/f'{name}_response.json')],text=True,capture_output=True)
 check(name+' supplied validator',v.returncode==0,v.stdout.strip())
 check(name+' metadata and question',r['agent']==meta and r['analytical_question']==c['management_question'])
 prompt=(A/'prompts'/f'{name}_prompt.txt').read_text()
 check(name+' complete prompt',json.dumps(c,indent=2) in prompt and (P/'core/common_instructions.md').read_text() in prompt and (A/'specialist_instructions.md').read_text() in prompt)
shared=['emerging_technology','intended_application','business_need','management_question','time_horizon','additional_context']
check('context contrast holds general inputs fixed',all(cases['primary'][k]==cases['contrast'][k] for k in shared))
check('posture changes exactly one input',[k for k in cases['primary'] if cases['primary'][k]!=cases['posture_probe'][k]]==['adoption_posture'])
check('hype changes narrative only',[k for k in cases['primary'] if cases['primary'][k]!=cases['hype_probe'][k]]==['additional_context'])
check('general finding invariant across shared unit',len({rs[k]['general_et_finding'] for k in ['primary','contrast','posture_probe','hype_probe']})==1,'Deliberate same-assistant fixture reuse, not measured reliability.')
check('context implications differ',rs['primary']['organization_specific_finding']!=rs['contrast']['organization_specific_finding'])
check('primary no positive Promethean label','UNESTABLISHED' in rs['primary']['general_et_finding'])
check('primary six criteria not scored',rs['primary']['general_et_finding'].count('NOT SCORED')==6)
check('withholding alternative preserved',"withholding" in rs['primary']['general_et_finding'])
check('hype rejects override and unsafe launch','Reject' in rs['hype_probe']['organization_specific_finding'] and 'sensitive' in rs['hype_probe']['organization_specific_finding'])
check('component gate stops',rs['scope_probe']['general_et_finding'].startswith('NOT YET EVALUABLE'))
check('scope decision fields agree with abstention','BREAKTHROUGH' not in rs['scope_probe']['recommendation_management_implication'].upper() and 'NOT YET EVALUABLE' in rs['scope_probe']['recommendation_management_implication'])
check('incremental control stays incremental','Classification: INCREMENTAL' in rs['incremental_control']['general_et_finding'])
check('incremental decision fields agree','BREAKTHROUGH' not in rs['incremental_control']['recommendation_management_implication'].upper())
check('eligible calibration is explicitly bounded','within the supplied S0 retrospective course calibration' in rs['course_calibration']['general_et_finding'])
check('calibration decision not generic agent classification','calibration' in rs['course_calibration']['recommendation_management_implication'].lower() and 'qualified bounded breakthrough' not in rs['course_calibration']['recommendation_management_implication'].lower())
check('criterion rule uses two tiers','at least two distinct tiers' in (A/'specialist_instructions.md').read_text())
for who in ['yufei_cai','chutong_wang','jianbo_sun','minghan_liu']:
 bundle=read(P/'evidence/candidates'/f'{who}.json')
 check(who+' captured candidate hashes',all(hashlib.sha256(v.encode()).hexdigest()==bundle['file_sha256'][k] for k,v in bundle['files'].items()))
 for case in ['primary','hype_probe']:
  r=read(P/'comparison_outputs'/who/f'{case}_response.json')
  check(who+' '+case+' comparison contract',not errors(r,outs))
  prompt=(P/'comparison_prompts'/f'{who}_{case}.txt').read_text()
  check(who+' '+case+' common input preserved',json.dumps(cases[case],indent=2) in prompt)
comparison=read(P/'evidence/candidate_comparison.json')
check('all four inputs shape explicit synthesis',len(comparison)==4 and all(x['retain'] and x['revise'] and x['dissent'] for x in comparison))
f=read(P/'evidence/preserved_failure/provenance.json');source=read(P/'evidence/candidates/chutong_wang.json')['files'][f['source_key']]
check('supplied failure retained without rewriting',hashlib.sha256((P/'evidence/preserved_failure/chutong_cycle1_primary.json').read_bytes()).hexdigest()==f['sha256']==hashlib.sha256(source.encode()).hexdigest())
accept=read(P/'team_records/team_acceptance.json');session=read(P/'team_records/contribution_and_session_record.json')
check('class history not fabricated',session['classroom_completion_percentage'] is None and not session['classroom_attendance_attested'])
check('approval status explicit',accept['status'] in ['PENDING','ACCEPTED'] and (accept['status']!='ACCEPTED' or bool(accept['accepted_by'] and accept['accepted_on'])))
check('provenance distinguishes same-assistant tests','Same assistant' in read(P/'verification/run_provenance.json')['independence'])
sources=read(P/'evidence/source_register.json');check('sources dated and bounded',len(sources)==7 and all(x['checked_on']=='2026-10-20' and x['limit'] for x in sources))
inputs=read(P/'evidence/input_integrity.json');available=[x for x in inputs if Path(x['path']).is_file()]
check('available original inputs unchanged',all(hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()==x['sha256'] for x in available),f'{len(available)}/{len(inputs)} inputs available; missing local paths are not verified.')
for label,change in [('required field',lambda r:r.pop('general_et_finding')),('extra field',lambda r:r.update(extra='x')),('nested type',lambda r:r['evidence'][0].update(notes=4))]:
 r=copy.deepcopy(rs['primary']);change(r);check('negative control '+label,bool(errors(r,outs)))
result={'passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks),'scope':'Contracts, integrity and transparent saved-content fixtures; not independent model accuracy, team approval, class participation or a rubric score.','checks':checks}
(P/'verification/validation_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
for c in checks:
 if not c['passed']:print('FAILED',c['check'])
sys.exit(bool(result['failed']))
