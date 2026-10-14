from pathlib import Path
import json
A=Path(__file__).resolve().parents[1]
R=A.parents[1]
def check(v,s,p='$'):
 t=s.get('type'); ts={'object':dict,'array':list,'string':str}
 if t and not isinstance(v,ts[t]): raise ValueError(p+' wrong type')
 if t=='object':
  for k in s.get('required',[]):
   if k not in v: raise ValueError(p+' missing '+k)
  if s.get('additionalProperties') is False and not set(v)<=set(s.get('properties',{})): raise ValueError(p+' extra field')
  for k,q in s.get('properties',{}).items():
   if k in v: check(v[k],q,p+'.'+k)
 elif t=='array':
  for i,x in enumerate(v): check(x,s.get('items',{}),p+'['+str(i)+']')
for folder,contract in [('cases','input_schema.json'),('responses','output_schema.json')]:
 s=json.loads((R/'core'/contract).read_text())
 for f in sorted((A/folder).glob('*.json')):
  check(json.loads(f.read_text()),s);print('PASS',folder+'/'+f.name)
print('Checks cover the supplied schema keyword subset, not general JSON Schema certification.')
