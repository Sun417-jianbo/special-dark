from pathlib import Path
import json
R=Path(__file__).resolve().parents[3];A=Path(__file__).resolve().parents[1]
def check(v,s):
 t=s.get('type');types={'object':dict,'array':list,'string':str}
 if t: assert isinstance(v,types[t])
 if t=='object':
  assert set(s.get('required',[]))<=set(v)
  if s.get('additionalProperties') is False: assert set(v)<=set(s.get('properties',{}))
  for k,p in s.get('properties',{}).items():
   if k in v:check(v[k],p)
 if t=='array':
  for x in v:check(x,s.get('items',{}))
for group,schema in [('cases','input_schema.json'),('responses','output_schema.json')]:
 for p in (A/group).glob('*.json'):
  check(json.loads(p.read_text()),json.loads((R/'core'/schema).read_text()));print('PASS',p.name)
print('Checks only the schema keywords used by these contracts, not general JSON Schema certification.')
