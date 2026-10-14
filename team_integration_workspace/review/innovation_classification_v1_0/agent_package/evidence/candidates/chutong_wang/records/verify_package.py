#!/usr/bin/env python3
"""Verify preserved contracts and the six-run evidence chain, not analytical truth."""
from pathlib import Path
import json,hashlib,subprocess,sys
A=Path(__file__).resolve().parents[1];R=A.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
errors=[]
serialization=[]
for line in (R/'FROZEN_CORE_SHA256.txt').read_text().splitlines():
 expected,rel=line.split('  ',1)
 if not (R/rel).is_file() or sha(R/rel)!=expected:errors.append('Frozen file mismatch: '+rel)
def check(value,schema,path):
 types={'object':dict,'array':list,'string':str}
 if schema.get('type') in types and not isinstance(value,types[schema['type']]):errors.append(path+': wrong type');return
 if isinstance(value,dict):
  for key in schema.get('required',[]):
   if key not in value:errors.append(path+': missing '+key)
  if schema.get('additionalProperties') is False:
   for key in value.keys()-schema.get('properties',{}).keys():errors.append(path+': extra '+key)
  for key,sub in schema.get('properties',{}).items():
   if key in value:check(value[key],sub,path+'.'+key)
 if isinstance(value,list) and 'items' in schema:
  for i,v in enumerate(value):check(v,schema['items'],path+f'[{i}]')
schema=json.loads((R/'core/output_schema.json').read_text());inschema=json.loads((R/'core/input_schema.json').read_text())
prov=json.loads((A/'records/run_provenance.json').read_text())
if {(x['cycle'],x['case']) for x in prov['runs']}!={(v,c) for v in [1,2] for c in ['primary','contrast_1','contrast_2']}:errors.append('Missing or duplicate expected run identity')
checks=[]
for x in prov['runs']:
 v=x['cycle'];c=x['case'];p=A/f'responses/cycle_{v}/{c}_response.json';case=A/f'cases/{c}.json';prompt=A/f'prompts/cycle_{v}/{c}_prompt.txt'
 response=json.loads(p.read_text());inputdata=json.loads(case.read_text())
 check(response,schema,str(p.relative_to(A)));check(inputdata,inschema,str(case.relative_to(A)))
 if response['agent']['version']!=x['specialist_version']:errors.append('Response version mismatch: '+str(p))
 for path,key in [(p,'response_sha256'),(case,'case_sha256'),(prompt,'prompt_sha256')]:
  if sha(path)!=x[key]:
   data=path.read_bytes()
   if data.endswith(b'\n') and hashlib.sha256(data[:-1]).hexdigest()==x[key]:
    serialization.append(str(path.relative_to(A))+': one appended final newline; original execution hash matches before that byte')
   else:errors.append('Provenance hash mismatch: '+str(path))
 packet=prompt.read_text();pv='0.1' if v==1 else '0.2'
 if (A/f'revisions/specialist_instructions_v{pv}.md').read_text() not in packet:errors.append('Prompt does not contain versioned instructions: '+str(prompt))
 if json.loads(packet.split('# CASE CONTEXT\n',1)[1].split('\n\n# REQUIRED OUTPUT SCHEMA',1)[0])!=inputdata:errors.append('Prompt/case mismatch: '+str(prompt))
 if (R/'core/common_instructions.md').read_text() not in packet:errors.append('Prompt/common rule mismatch')
 result=subprocess.run([sys.executable,str(R/'tools/validate_response.py'),str(p)],capture_output=True,text=True)
 if result.returncode:errors.append('Course validator failed: '+str(p))
 checks.append({'cycle':v,'case':c,'course_validator':result.stdout.strip(),'schema':'checked','provenance':'checked'})
report={'status':'FAILED' if errors else 'PASSED','frozen_core':'checked including frozen tools','runs':checks,'errors':errors,'serialization_normalizations':serialization,'limits':'Structural integrity and evidence-chain checks only. No claim of factual correctness, chart-tool execution, business outcomes or model reliability.'}
(A/'records/validation_results.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
raise SystemExit(bool(errors))
