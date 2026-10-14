"""Read-only checks of evidence integrity and the frozen contracts. No model API."""
from pathlib import Path
import hashlib, json, subprocess, sys
# Validate only schema keywords present in the frozen course contracts.
class FrozenContractValidator:
 def __init__(self,schema): self.schema=schema
 def validate(self,value): self._check(value,self.schema,'$')
 def _check(self,value,schema,where):
  kinds={'object':dict,'array':list,'string':str}
  if 'type' in schema: assert isinstance(value,kinds[schema['type']]),where+' type mismatch'
  if isinstance(value,dict):
   for key in schema.get('required',[]): assert key in value,where+' missing '+key
   props=schema.get('properties',{})
   if schema.get('additionalProperties') is False: assert set(value)<=set(props),where+' extra keys'
   for key,item in value.items():
    if key in props:self._check(item,props[key],where+'.'+key)
  if isinstance(value,list) and 'items' in schema:
   for index,item in enumerate(value):self._check(item,schema['items'],where+'['+str(index)+']')
agent=Path(__file__).resolve().parents[1]
root=agent.parents[1]
schema=json.loads((root/'core/output_schema.json').read_text())
input_schema=json.loads((root/'core/input_schema.json').read_text())
output_validator=FrozenContractValidator(schema);input_validator=FrozenContractValidator(input_schema)
checks=[]
def ok(label): checks.append(label);print('PASS:',label)
r=subprocess.run([sys.executable,str(root/'tools/check_frozen_core.py')],capture_output=True,text=True)
assert r.returncode==0,r.stdout+r.stderr
ok(r.stdout.strip())
for case in ['primary','contrast_1','contrast_2']:
 data=json.loads((agent/f'cases/{case}.json').read_text());input_validator.validate(data)
 ok('Common input schema: '+case)
versions={1:'1.0',2:'1.1'}
for cycle in [1,2]:
 folder=agent/f'tests/cycle_{cycle}'
 manifest=json.loads((folder/'run_manifest.json').read_text())
 generals=[]
 for case in ['primary','contrast_1','contrast_2']:
  response=folder/f'{case}_response.json';data=json.loads(response.read_text());output_validator.validate(data)
  assert data['agent']['version']==versions[cycle]
  r=subprocess.run([sys.executable,str(root/'tools/validate_response.py'),str(response)],capture_output=True,text=True)
  assert r.returncode==0,r.stdout+r.stderr
  item=next(x for x in manifest['cases'] if x['case']==case)
  prompt=agent/f'tests/prompts/cycle_{cycle}/{case}.txt'
  assert hashlib.sha256(prompt.read_bytes()).hexdigest()==item['prompt_sha256']
  assert hashlib.sha256(response.read_bytes()).hexdigest()==item['response_sha256']
  text=prompt.read_text();case_text=text.split('# CASE CONTEXT\n',1)[1].split('# REQUIRED OUTPUT SCHEMA',1)[0]
  assert json.loads(case_text)==json.loads((agent/f'cases/{case}.json').read_text()),'Input changed across cycles'
  assert (folder/'specialist_instructions.md').read_text() in text,'Prompt does not contain archived instructions'
  generals.append(data['general_et_finding'])
  if cycle==2:assert response.read_bytes()==(agent/f'responses/{case}_response.json').read_bytes()
  ok(f'Cycle {cycle} {case}: frozen validator, strict schema, versions, input and archive hashes')
 assert len(set(generals))==1
 ok(f'Cycle {cycle}: general technology finding remains identical across contexts')
assert json.loads((agent/'cases/primary.json').read_text())['emerging_technology']==json.loads((agent/'cases/contrast_1.json').read_text())['emerging_technology']
ok('Primary and contrast hold technology constant')
print(f'\n{len(checks)} structural/integrity checks passed. These do not prove factual validity or business performance. See the qualitative review separately.')
