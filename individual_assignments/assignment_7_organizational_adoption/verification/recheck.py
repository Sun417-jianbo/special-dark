"""Check saved artifacts; never calls a model or proves independent accuracy."""
from pathlib import Path
import json,sys,subprocess,copy,hashlib,tempfile
R=Path(__file__).resolve().parents[1];A=R/'agents/organizational_adoption_agent';checks=[]
def read(p):return json.loads(p.read_text())
def check(name,ok):checks.append({'check':name,'passed':bool(ok)})
def errors(v,s):
 t={'string':str,'object':dict,'array':list}
 if set(s)-{'$schema','title','type','required','properties','items','additionalProperties'}:raise ValueError('Unsupported schema keyword')
 if not isinstance(v,t[s['type']]):return ['type']
 e=[]
 if isinstance(v,dict):
  e += ['missing '+k for k in s.get('required',[]) if k not in v]
  if s.get('additionalProperties') is False:e += ['extra '+k for k in v if k not in s.get('properties',{})]
  for k,ss in s.get('properties',{}).items():
   if k in v:e+=errors(v[k],ss)
 if isinstance(v,list):
  for x in v:e+=errors(x,s['items'])
 return e
q=subprocess.run([sys.executable,str(R/'tools/check_frozen_core.py')],capture_output=True,text=True);check('frozen core integrity',q.returncode==0)
ins=read(R/'core/input_schema.json');outs=read(R/'core/output_schema.json');meta=read(A/'agent_metadata.json');cases={};responses={}
for p in sorted((A/'cases').glob('*.json')):
 n=p.stem;c=read(p);r=read(A/'responses'/f'{n}_response.json');cases[n]=c;responses[n]=r
 check(n+' input schema',not errors(c,ins));check(n+' full output schema',not errors(r,outs));check(n+' version',r['agent']==meta)
 q=subprocess.run([sys.executable,str(R/'tools/validate_response.py'),str(A/'responses'/f'{n}_response.json')],capture_output=True,text=True);check(n+' canonical validator',q.returncode==0)
 with tempfile.TemporaryDirectory() as td:
  dest=Path(td)/'packet.txt';q=subprocess.run([sys.executable,str(R/'tools/build_prompt.py'),'--agent',str(A),'--case',str(p),'--out',str(dest)],capture_output=True,text=True)
  check(n+' prompt reproduction',q.returncode==0 and dest.read_bytes()==(A/'prompts'/f'{n}_prompt.txt').read_bytes())
 for d in ['Leadership/sponsorship','Skills','Workflow/process','Infrastructure/data','Resources/budget','Governance/risk','Culture/change','Operating ownership']:check(n+' '+d,d in r['organization_specific_finding'])
 check(n+' targeted questions',len(r['abstention_or_more_information_needed'])>=1)
 check(n+' authority handoff','Adoption' in r['recommendation_management_implication'])
 check(n+' three priorities',all(x in r['recommendation_management_implication'] for x in ['P1','P2','P3']))
check('technology unchanged',len({c['emerging_technology'] for c in cases.values()})==1)
check('application unchanged',len({c['intended_application'] for c in cases.values()})==1)
check('general finding stable',len({r['general_et_finding'] for r in responses.values()})==1)
check('application finding stable',len({r['application_finding'] for r in responses.values()})==1)
check('primary blocks live use',responses['primary']['organization_specific_finding'].startswith('NOT READY FOR LIVE TRIAL'))
check('contrast recognizes readiness strengths',responses['contrast']['organization_specific_finding'].startswith('CONDITIONALLY READY FOR BOUNDED EVALUATION'))
check('missing capacity withholds readiness',responses['missing_capacity']['organization_specific_finding'].startswith('INSUFFICIENT INFORMATION'))
check('posture cannot bypass prerequisites',responses['posture_pressure']['organization_specific_finding'].startswith('NOT READY FOR LIVE TRIAL'))
check('posture test changes exactly one input',[k for k in cases['primary'] if cases['primary'][k]!=cases['posture_pressure'][k]]==['adoption_posture'])
check('missing information test changes constraints only',[k for k in cases['contrast'] if cases['contrast'][k]!=cases['missing_capacity'][k]]==['capabilities_constraints'])
v0=read(R/'evidence/revision/v0_primary_response.json');check('weak baseline passes structure',not errors(v0,outs));check('weak baseline exposes gate failure','Begin a small live pilot' in v0['recommendation_management_implication'])
for name,change in [('missing field',lambda r:r.pop('general_et_finding')),('extra field',lambda r:r.update(extra=True)),('wrong array item',lambda r:r['change_monitoring_triggers'].append(5))]:
 r=copy.deepcopy(responses['primary']);change(r);check('negative schema control '+name,bool(errors(r,outs)))
result={'passed':sum(c['passed'] for c in checks),'total':len(checks),'all_passed':all(c['passed'] for c in checks),'scope':'Saved-contract, byte integrity and explicit content checks only. Same-assistant authored responses, not independent model trials or field validation.','checks':checks}
(R/'verification/validation_results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
for c in checks:
 if not c['passed']:print('FAIL',c['check'])
sys.exit(not result['all_passed'])
