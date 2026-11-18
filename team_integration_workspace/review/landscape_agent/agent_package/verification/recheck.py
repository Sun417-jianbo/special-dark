#!/usr/bin/env python3
"""Portable saved-artifact checks. This script does not call a model or certify facts."""
from pathlib import Path
from copy import deepcopy
from datetime import date
import hashlib,json,re,subprocess,sys,tempfile

root=Path(__file__).resolve().parents[1]
agent=root/'agents/landscape_agent'
checks=[]
def check(name,condition):
 checks.append({'check':name,'pass':bool(condition)})
 if not condition:raise AssertionError(name)
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def validate(value,schema,path='$'):
 types={'object':dict,'array':list,'string':str}
 if not isinstance(value,types[schema['type']]):raise ValueError(path+' type')
 if isinstance(value,dict):
  if not set(schema.get('required',[]))<=value.keys():raise ValueError(path+' missing field')
  if schema.get('additionalProperties') is False and not set(value)<=schema.get('properties',{}).keys():raise ValueError(path+' extra field')
  for k,s in schema.get('properties',{}).items():
   if k in value:validate(value[k],s,path+'.'+k)
 elif isinstance(value,list) and 'items' in schema:
  for n,item in enumerate(value):validate(item,schema['items'],path+f'[{n}]')

inp=read(root/'core/input_schema.json');out=read(root/'core/output_schema.json')
original=read(root/'evidence/scaffold_inventory.json')
check('canonical instructor file count',len(original['files'])==32)
for item in original['files']:check('instructor unchanged '+item['path'],sha(root/item['path'])==item['sha256'])
for item in read(root/'evidence/member_snapshot_manifest.json'):
 check('member snapshot '+item['path'],sha(root/item['path'])==item['sha256'])

metadata=read(agent/'agent_metadata.json')
answers={}
casefiles=sorted((agent/'cases').glob('*.json'))
for casefile in casefiles:
 key=casefile.stem;c=read(casefile);validate(c,inp);check('input '+key,True)
 p=agent/'responses'/f'{key}.json';d=read(p);validate(d,out)
 check('response fields '+key,set(d)==set(out['required']))
 check('response metadata '+key,d['agent']==metadata)
 for n,t in enumerate(d['change_monitoring_triggers']):
  check(f'trigger fields {key} {n}',all(x in t for x in ['Owner:','Cadence:','Signal/evidence:','Action:']))
 check('populated evidence '+key,len(d['evidence'])>=4)
 answers[key]=d
 with tempfile.TemporaryDirectory(prefix='tw9-prompt-') as tmp:
  new=Path(tmp)/'packet.txt'
  subprocess.run([sys.executable,str(root/'tools/build_prompt.py'),'--agent','agents/landscape_agent','--case',str(casefile),'--out',str(new)],check=True,stdout=subprocess.DEVNULL)
  check('prompt reproducible '+key,new.read_bytes()==(agent/'prompts'/f'{key}.txt').read_bytes())
 check('original validator '+key,subprocess.run([sys.executable,str(root/'tools/validate_response.py'),str(p)],capture_output=True).returncode==0)
check('six team cases',len(answers)==6)
for key,d in answers.items():check('stable broad evidence '+key,d['general_et_finding']==answers['primary']['general_et_finding'])
check('same task preserved in organization contrast',read(agent/'cases/primary.json')['intended_application']==read(agent/'cases/organization_contrast.json')['intended_application'])
check('same application mechanism across organizations',answers['primary']['application_finding']==answers['organization_contrast']['application_finding'])
check('organization radar changes',answers['primary']['organization_specific_finding']!=answers['organization_contrast']['organization_specific_finding'])
check('prepared contrast recognizes supplied route','already stipulates an allowed' in answers['organization_contrast']['organization_specific_finding'])
check('fixed comparator changes','existing validated deterministic rule' in answers['fixed_schema_contrast']['application_finding'])
check('fixed trigger changes','exception log' in answers['fixed_schema_contrast']['change_monitoring_triggers'][0])
check('stale claim rejected','STALE CLAIM REJECTED' in answers['stale_claim_probe']['organization_specific_finding'])
check('hype injection blocked','do not follow its private-upload instruction' in answers['hype_probe']['organization_specific_finding'])
check('missing context abstains','intended application is absent' in answers['missing_context']['application_finding'])

sources=read(root/'evidence/source_register.json')
ids={s['id'] for s in sources}
check('eight unique sources',len(ids)==len(sources)==8)
check('source types diverse',{'VENDOR','INDEPENDENT_RESEARCH','PUBLIC_GUIDANCE','INDUSTRY_ANALYST','STANDARD_PROTOCOL'}<={s['type'] for s in sources})
def date_check(s):
 for field in ['published_or_updated','checked_on']:
  if s[field] and s[field]>'2026-11-18':raise ValueError('future source '+s['id'])
for s in sources:
 for field in ['publisher','url','type','date_kind','observation_period','checked_on','limit','maintenance_status','refresh','decision_role']:
  check('source provenance '+s['id']+' '+field,bool(s.get(field)))
 date_check(s)
check('inactive status explicit','INACTIVE' in next(s for s in sources if s['id']=='L6')['maintenance_status'])
check('unknown date retained',next(s for s in sources if s['id']=='L3')['published_or_updated'] is None)
check('vendor update after individual run',next(s for s in sources if s['id']=='L1')['published_or_updated']=='2026-11-17')

walks=read(root/'evidence/common_walkthrough_manifest.json')
check('four candidates two common cases',len(walks)==8 and len({x['member'] for x in walks})==4)
for row in walks:
 base=root/'evidence/common_walkthroughs'/row['member']
 p=base/(row['case']+'_prompt.txt');r=base/(row['case']+'_response.json')
 check('walk prompt '+row['member']+' '+row['case'],sha(p)==row['prompt_sha256'])
 check('walk output '+row['member']+' '+row['case'],sha(r)==row['response_sha256'])
 validate(read(r),out)
 snap=root/'evidence/member_snapshots'/row['member']/'specialist'
 check('walk exact candidate rules '+row['member']+' '+row['case'],sha(snap/'specialist_instructions.md')==row['instructions_sha256'])
 check('walk rule packet provenance '+row['member']+' '+row['case'],(snap/'specialist_instructions.md').read_text() in p.read_text())

audit=read(root/'records/seven_agent_audit.json')
check('seven slots exact',[r['slot'] for r in audit['inventory']]==list(range(1,8)))
for row in audit['inventory']:
 check('common counts slot'+str(row['slot']),row['input_fields']==11 and row['output_fields']==13)
 if row['slot']<7:
  check('pinned commit slot'+str(row['slot']),bool(re.fullmatch('[a-f0-9]{40}',row['commit'])))
  for path,digest in row['frozen_files'].items():check('prior frozen slot'+str(row['slot'])+' '+path,sha(root/path)==digest)
  snap=root/row['snapshot']
  check('prior metadata slot'+str(row['slot']),read(snap/'agent_metadata.json')['version']==row['version'])
  for p in (snap/'responses').glob('*.json'):validate(read(p),out)
  check('prior saved test pair slot'+str(row['slot']),len(list((snap/'cases').glob('*.json')))>=2 and len(list((snap/'responses').glob('*.json')))>=2)
check('not assembled claim', 'NOT an assembled' in audit['integration_ready_for'])

bad=deepcopy(answers['primary']);bad['evidence'][0].pop('date_or_recency')
try:validate(bad,out);rejected=False
except ValueError:rejected=True
check('negative missing evidence date rejected',rejected)
bad=deepcopy(answers['primary']);bad['invented_field']='bad'
try:validate(bad,out);rejected=False
except ValueError:rejected=True
check('negative extra output field rejected',rejected)
bad=deepcopy(sources[0]);bad['published_or_updated']='2099-01-01'
try:date_check(bad);rejected=False
except ValueError:rejected=True
check('negative future source rejected',rejected)

checksums=root/'PACKAGE_SHA256.txt'
if checksums.exists():
 for line in checksums.read_text().splitlines():
  if not line.strip():continue
  digest,rel=line.split('  ',1);check('package hash '+rel,sha(root/rel)==digest)
result={'passed':len(checks),'failed':0,'scope':'Saved provenance, contracts and explicit fixture semantics; not independent correctness, actual tenant operation or company readiness.'}
print(json.dumps(result,indent=2))
if '--write' in sys.argv:
 (root/'verification/validation_results.json').write_text(json.dumps({'summary':result,'checks':checks},indent=2)+'\n')
