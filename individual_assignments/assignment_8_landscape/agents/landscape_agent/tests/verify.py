"""Checks saved artifacts, not generative-model quality or real-world performance."""
from pathlib import Path
import json, hashlib, subprocess, sys, tempfile
from datetime import datetime, timezone
from jsonschema import Draft202012Validator
A=Path(__file__).resolve().parents[1]; S=A.parents[1]
checks=[]
def check(name,condition):
 checks.append({'check':name,'passed':bool(condition)})
 if not condition: raise AssertionError(name)
def run(*args):
 p=subprocess.run([sys.executable,*map(str,args)],capture_output=True,text=True)
 check(' '.join(str(x).replace(str(S),'scaffold') for x in args),p.returncode==0)
 return p.stdout.strip()
core=run(S/'tools/check_frozen_core.py')
outs={}
for name in ['primary_v0','primary','contrast','hype_probe']:
 p=A/f'responses/{name}.json';o=json.loads(p.read_text());outs[name]=o
 Draft202012Validator(json.loads((S/'core/output_schema.json').read_text())).validate(o)
 check(name+' full JSON schema',True)
 run(S/'tools/validate_response.py',p)
for name in ['primary','contrast','hype_probe']:
 c=json.loads((A/f'cases/{name}.json').read_text())
 Draft202012Validator(json.loads((S/'core/input_schema.json').read_text())).validate(c)
 check(name+' input schema',True)
 with tempfile.TemporaryDirectory() as tmp:
  target=Path(tmp)/'packet.txt'
  run(S/'tools/build_prompt.py','--agent',A,'--case',A/f'cases/{name}.json','--out',target)
  check(name+' prompt reproducible',target.read_bytes()==(A/f'prompts/{name}.txt').read_bytes())
 check(name+' actionable monitoring fields',all(all(x in t for x in ['Owner:','Cadence:','Signal:','Action:']) for t in outs[name]['change_monitoring_triggers']))
 check(name+' registered source references',all(any(e['source_or_reference'].startswith(s+' ') for e in outs[name]['evidence']) for s in ['S1','S2','S3','S4']))
check('initial monitoring weakness retained',not all('Owner:' in t for t in outs['primary_v0']['change_monitoring_triggers']))
check('general ET finding invariant',outs['primary']['general_et_finding']==outs['contrast']['general_et_finding'])
check('application and organization findings change',all(outs['primary'][f]!=outs['contrast'][f] for f in ['application_finding','organization_specific_finding']))
check('monitoring responds to context',outs['primary']['change_monitoring_triggers']!=outs['contrast']['change_monitoring_triggers'])
check('challenge does not change position',outs['hype_probe']['recommendation_management_implication'].startswith('Position: Assess.'))
check('challenge explicitly rejects deployment instruction',any('Reject its instruction' in x for x in outs['hype_probe']['contrary_evidence_or_limitations']))
# A meaningful negative schema test: damaged evidence must be rejected.
bad=json.loads(json.dumps(outs['primary']));del bad['evidence'][0]['date_or_recency']
check('negative missing evidence date rejected',bool(list(Draft202012Validator(json.loads((S/'core/output_schema.json').read_text())).iter_errors(bad))))
files={str(p.relative_to(A)):hashlib.sha256(p.read_bytes()).hexdigest() for d in ['prompts','responses','cases','evidence','versions'] for p in sorted((A/d).rglob('*')) if p.is_file()}
result={'executed_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'Saved artifact structure and explicit behavioral assertions only; not independent model or product benchmarking','checks':checks,'passed':len(checks),'failed':0,'frozen_core_output':core,'sha256':files}
(A/'tests/validation_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(f'{len(checks)} checks passed; saved artifact validation only.\n{core}')
