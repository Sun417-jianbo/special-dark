"""Standard-library contract and artifact checks; no model or student code execution."""
from pathlib import Path
import json,hashlib,subprocess,sys,copy
P=Path(__file__).resolve().parents[1]
A=P/'agents/innovation_classification_agent'
results=[]
def check(name,ok,detail=''):
    results.append({'check':name,'passed':bool(ok),'detail':detail})
def read(p):return json.loads(p.read_text())
def schema_errors(x,s,path='$'):
    errors=[];types={'object':dict,'array':list,'string':str,'number':(int,float),'integer':int,'boolean':bool,'null':type(None)}
    t=s.get('type')
    if t and not isinstance(x,types[t]):return [path+': expected '+t]
    if isinstance(x,dict):
        for k in s.get('required',[]):
            if k not in x:errors.append(path+': missing '+k)
        if s.get('additionalProperties') is False:
            for k in x:
                if k not in s.get('properties',{}):errors.append(path+': extra '+k)
        for k,v in x.items():
            if k in s.get('properties',{}):errors+=schema_errors(v,s['properties'][k],path+'.'+k)
    if isinstance(x,list) and 'items' in s:
        for i,v in enumerate(x):errors+=schema_errors(v,s['items'],f'{path}[{i}]')
    return errors
def count(x):
    if isinstance(x,str):return len(x.split())
    if isinstance(x,list):return sum(map(count,x))
    if isinstance(x,dict):return sum(count(v) for k,v in x.items() if k!='agent')
    return 0
frozen=subprocess.run([sys.executable,str(P/'tools/check_frozen_core.py')],text=True,capture_output=True)
check('canonical frozen-core checker',frozen.returncode==0,frozen.stdout.strip())
frozenfiles=[]
for line in (P/'FROZEN_CORE_SHA256.txt').read_text().splitlines():
    if line.strip():frozenfiles.append(line.split('  ',1)[1])
check('seven frozen files present',len(frozenfiles)==7,str(frozenfiles))
snap=read(P/'evidence/candidate_snapshot_manifest.json')
bad=[x['path'] for x in snap if hashlib.sha256((P/x['path']).read_bytes()).hexdigest()!=x['sha256']]
check('candidate snapshot integrity',not bad,f'{len(snap)} retained files; mismatches: {bad}')
check('all four candidate owners',set(x['owner'] for x in snap)=={'chutong_wang','jianbo_sun','yufei_cai','minghan_liu'})
for old,new in [('primary','primary'),('contrast_1','contrast'),('contrast_2','borderline')]:
    check('unchanged shared case '+new,(A/'cases'/f'{new}.json').read_bytes()==(P/'evidence/candidates/chutong_wang/cases'/f'{old}.json').read_bytes())
cases={p.stem:read(p) for p in sorted((A/'cases').glob('*.json'))}
inp=read(P/'core/input_schema.json');out=read(P/'core/output_schema.json')
for name,c in cases.items():check('input schema '+name,not schema_errors(c,inp),str(schema_errors(c,inp)))
fixed=['emerging_technology','intended_application','business_need','management_question','time_horizon','additional_context']
check('organization contrast holds shared context fixed',all(cases['primary'][k]==cases['contrast'][k] for k in fixed))
changes=[k for k in cases['primary'] if cases['primary'][k]!=cases['posture_probe'][k]]
check('posture probe changes one field',changes==['adoption_posture'],str(changes))
inventory=read(P/'verification/response_inventory.json')
for item in inventory:
    path=P/item['response'];r=read(path);label=item['response']
    err=schema_errors(r,out);check('full schema '+label,not err,str(err))
    proc=subprocess.run([sys.executable,str(P/'tools/validate_response.py'),str(path)],capture_output=True,text=True)
    check('canonical validator '+label,proc.returncode==0,proc.stdout.strip())
    meta=read(A/'agent_metadata.json') if item['kind']=='team' else read(P/'evidence/candidates'/item['candidate']/'agent_metadata.json')
    check('metadata matches '+label,r['agent']==meta)
    check('target response length '+label,800<=count(r)<=1100,str(count(r)))
    check('question matches '+label,r['analytical_question']==cases[item['case']]['management_question'])
    prompt=(A/'prompts'/f"{item['case']}_prompt.txt") if item['kind']=='team' else (P/'comparison_prompts'/f"{item['candidate']}_{item['case']}.txt")
    txt=prompt.read_text();check('prompt contains exact case and frozen instructions '+label,json.dumps(cases[item['case']],indent=2) in txt and (P/'core/common_instructions.md').read_text() in txt)
r=read(A/'responses/primary_response.json')
extra=copy.deepcopy(r);extra['extra']='forbidden'
wrong=copy.deepcopy(r);wrong['evidence'][0]['notes']=17
missing=copy.deepcopy(r);missing.pop('organization_specific_finding')
check('negative control extra top-level field rejected',bool(schema_errors(extra,out)))
check('negative control nested type rejected',bool(schema_errors(wrong,out)))
check('negative control required field rejected',bool(schema_errors(missing,out)))
rr={k:read(A/'responses'/f'{k}_response.json') for k in cases}
check('stable general evidence across organization contrast',rr['primary']['general_et_finding']==rr['contrast']['general_et_finding'],'Intentional text equality is not an independent reliability estimate.')
check('stable technical classification under posture-only change',rr['primary']['application_finding']==rr['posture_probe']['application_finding'])
check('borderline explicitly withholds scope and impact','withheld' in rr['borderline']['organization_specific_finding'] and 'unverified' in rr['borderline']['application_finding'])
check('contrast preserves missing-economics branch','withheld' in rr['contrast']['organization_specific_finding'] and 'Low-to-Moderate' in rr['contrast']['organization_specific_finding'])
original=read(P/'evidence/input_integrity.json')
available=[x for x in original if Path(x['path']).exists()]
bad=[x['path'] for x in available if hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()!=x['sha256']]
check('available original input files unchanged',not bad,f'{len(available)}/{len(original)} available; mismatches: {bad}')
summary={'passed':sum(x['passed'] for x in results),'failed':sum(not x['passed'] for x in results),'checks':results,'limits':'Contracts and transparent fixture assertions, not independent model performance, factual truth, student learning or human team approval. The schema checker covers every keyword used by these supplied schemas, not arbitrary JSON Schema.'}
(P/'verification/validation_results.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='checks'},indent=2))
sys.exit(0 if summary['failed']==0 else 1)
