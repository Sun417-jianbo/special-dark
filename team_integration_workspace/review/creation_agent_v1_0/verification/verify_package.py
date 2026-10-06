#!/usr/bin/env python3
"""Validate saved artifacts; does not call a model or certify analytical truth."""
from pathlib import Path
import copy, hashlib, json, subprocess, sys, tempfile

class FrozenSchemaValidator:
    """Enforce the type/required/properties/items rules used by these two schemas.

    This is deliberately not a general JSON Schema implementation. Unknown
    schema keywords fail closed so a future architecture change needs review.
    """
    def __init__(self, schema):
        self.schema = schema
    def iter_errors(self, value):
        yield from self._errors(self.schema, value, '$')
    def _errors(self, schema, value, path):
        supported={'$schema','title','type','required','properties','items','additionalProperties'}
        if set(schema)-supported:
            yield f'{path}: unsupported schema keywords {set(schema)-supported}'
            return
        typ=schema.get('type')
        classes={'object':dict,'array':list,'string':str}
        if typ not in classes or not isinstance(value,classes[typ]):
            yield f'{path}: expected {typ}'
            return
        if typ=='object':
            for key in schema.get('required',[]):
                if key not in value: yield f'{path}: missing {key}'
            props=schema.get('properties',{})
            if schema.get('additionalProperties') is False:
                for key in set(value)-set(props): yield f'{path}: unexpected {key}'
            for key,sub in props.items():
                if key in value: yield from self._errors(sub,value[key],path+'.'+key)
        elif typ=='array':
            for i,item in enumerate(value):
                yield from self._errors(schema['items'],item,f'{path}[{i}]')

ROOT = Path(__file__).resolve().parents[1]
checks = []
def check(name, ok, detail):
    checks.append(dict(check=name, passed=bool(ok), detail=detail))
def run(*args):
    return subprocess.run([sys.executable, *map(str,args)], cwd=ROOT, text=True, capture_output=True)
def read(rel):
    return json.loads((ROOT/rel).read_text())

out_schema = FrozenSchemaValidator(read('core/output_schema.json'))
in_schema = FrozenSchemaValidator(read('core/input_schema.json'))
meta = read('agents/creation_agent/agent_metadata.json')
core = run('tools/check_frozen_core.py')
check('frozen core', core.returncode == 0, core.stdout.strip()+core.stderr.strip())
(ROOT/'evidence/frozen_core_check.txt').write_text(core.stdout+core.stderr)
responses = {}
cases = {}
source_urls = {s['url'] for s in read('evidence/source_register.json')}
for name in ('primary','contrast','missing_context','unsupported_claims'):
    cp = f'agents/creation_agent/cases/{name}.json'
    rp = f'agents/creation_agent/responses/{name}_response.json'
    cases[name] = c = read(cp)
    responses[name] = r = read(rp)
    errors = list(in_schema.iter_errors(c))
    check(name+' input schema', not errors, errors)
    errors = list(out_schema.iter_errors(r))
    check(name+' strict output schema', not errors, errors)
    course = run('tools/validate_response.py',rp)
    check(name+' course validator', course.returncode == 0, course.stdout.strip()+course.stderr.strip())
    check(name+' metadata', r['agent'] == meta, 'Response metadata must exactly match agent_metadata.json')
    evidence_urls = {url for url in source_urls if any(url in e['source_or_reference'] for e in r['evidence'])}
    check(name+' source linkage', evidence_urls == source_urls, 'All six registered source URLs appear; support requires human inspection')
    check(name+' case reference', any(e['source_or_reference']==cp for e in r['evidence']), cp)
    categories=('Scientific and technical','Economic and resource','Social and user-demand','Institutional and regulatory','Market and competitive')
    check(name+' five category coverage', all(x in r['general_et_finding'] for x in categories), 'Coverage only; labels do not prove causality or completeness')
    prompt = run('tools/build_prompt.py','--agent','agents/creation_agent','--case',cp,'--out',f'agents/creation_agent/prompts/{name}.txt')
    check(name+' prompt construction', prompt.returncode == 0, 'Build only, not a model invocation')

fixed = ('emerging_technology','intended_application','business_need','management_question','time_horizon')
check('matched primary contrast inputs', all(cases['primary'][k]==cases['contrast'][k] for k in fixed), list(fixed))
check('controlled historical finding', len({r['general_et_finding'] for r in responses.values()})==1, 'Intentionally reused history; NOT independent repeatability')
check('contextual finding changes', responses['primary']['organization_specific_finding'] != responses['contrast']['organization_specific_finding'], 'Read field contents for substantive meaning')
check('missing context regression', responses['missing_context']['organization_specific_finding'].startswith('WITHHELD:') and len(responses['missing_context']['abstention_or_more_information_needed']) >= 3, 'Presence assertion only; not an independent semantic assessment')
check('unsupported premise regression', sum(s.startswith('REJECTED:') for s in responses['unsupported_claims']['contrary_evidence_or_limitations']) == 3, 'Three explicit rejected premises in saved example')
snapshots = read('evidence/candidate_snapshot_manifest.json')
bad = [s['path'] for s in snapshots if not (ROOT/s['path']).is_file() or hashlib.sha256((ROOT/s['path']).read_bytes()).hexdigest()!=s['sha256']]
check('candidate snapshot integrity', not bad, {'files_checked':len(snapshots),'mismatches':bad})

# Negative controls prove what the validators do and do not check.
with tempfile.TemporaryDirectory(prefix='tw3-negative-controls-') as td:
    bad_extra=copy.deepcopy(responses['primary']); bad_extra['unsupported_extra_key']='not permitted'
    f=Path(td)/'extra_key.json'; f.write_text(json.dumps(bad_extra))
    basic=run('tools/validate_response.py',f)
    strict_errors=list(out_schema.iter_errors(bad_extra))
    check('extra key negative control', basic.returncode==0 and bool(strict_errors), 'Basic validator accepts extra key; strict frozen-schema validation rejects it. Frozen tool intentionally unchanged.')
    bad_missing=copy.deepcopy(responses['primary']); del bad_missing['general_et_finding']
    f=Path(td)/'missing_key.json'; f.write_text(json.dumps(bad_missing))
    basic=run('tools/validate_response.py',f)
    check('missing key negative control', basic.returncode!=0 and bool(list(out_schema.iter_errors(bad_missing))), 'Both validators reject missing required history field')
    bad_type=copy.deepcopy(responses['primary']); bad_type['evidence'][0]['claim']=99
    check('wrong evidence type negative control', bool(list(out_schema.iter_errors(bad_type))), 'Strict validator rejects numeric evidence claim')

for candidate in ('yufei_cai','chutong_wang'):
    for name in ('primary','contrast'):
        p=run('tools/build_prompt.py','--agent',f'evidence/candidate_snapshots/{candidate}',
              '--case',f'agents/creation_agent/cases/{name}.json',
              '--out',f'comparison_prompts/{candidate}_{name}.txt')
        check(candidate+' '+name+' comparison prompt',p.returncode==0,'Packet for same-assistant controlled walkthrough; not an independent invocation')
        response=read(f'comparison_responses/{candidate}_{name}.json')
        errors=list(out_schema.iter_errors(response))
        check(candidate+' '+name+' comparison schema',not errors,errors)
        check(candidate+' '+name+' comparison metadata',response['agent']==read(f'evidence/candidate_snapshots/{candidate}/agent_metadata.json'),'Candidate design identifier, not authorship of this new response')

for candidate in ('yufei_cai','chutong_wang'):
    first=read(f'comparison_responses/{candidate}_primary.json')
    second=read(f'comparison_responses/{candidate}_contrast.json')
    check(candidate+' controlled contrast', first['general_et_finding']==second['general_et_finding'] and first['organization_specific_finding']!=second['organization_specific_finding'], 'Deliberately controlled history with distinct organizational findings; no repeatability claim')

result={'checked_on':'2026-10-06','scope':'Saved-artifact structural and regression checks; not model reliability or team approval',
        'checks':checks,'passed':sum(x['passed'] for x in checks),'total':len(checks)}
dest=ROOT/'verification/validation_results.json'
dest.write_text(json.dumps(result,indent=2)+'\n')
print(f"{result['passed']}/{result['total']} checks passed")
for x in checks:
    if not x['passed']: print('FAILED',x)
sys.exit(0 if all(x['passed'] for x in checks) else 1)
