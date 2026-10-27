#!/usr/bin/env python3
"""Recheck saved artifacts. This script never invokes a model or edits a response."""
from pathlib import Path
import hashlib, json, subprocess, sys

ROOT=Path(__file__).resolve().parents[1]
checks=[]
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def record(name,condition):checks.append({'check':name,'passed':bool(condition)})
def load(rel):return json.loads((ROOT/rel).read_text())
def valid(data,schema):
    """Validate the keywords used by these two frozen contracts, not arbitrary JSON Schema."""
    types={'object':dict,'array':list,'string':str}
    if schema.get('type') in types and not isinstance(data,types[schema['type']]):return False
    if isinstance(data,dict):
        if any(k not in data for k in schema.get('required',[])):return False
        props=schema.get('properties',{})
        if schema.get('additionalProperties') is False and any(k not in props for k in data):return False
        return all(valid(v,props[k]) for k,v in data.items() if k in props)
    if isinstance(data,list) and 'items' in schema:return all(valid(v,schema['items']) for v in data)
    return True
for line in (ROOT/'FROZEN_CORE_SHA256.txt').read_text().splitlines():
    if line.strip():
        expected,rel=line.split(None,1);p=ROOT/rel.strip()
        record('frozen '+rel,p.is_file() and h(p)==expected)
for row in load('evidence/scaffold_inventory.json')['original_files']:
    record('original scaffold '+row['path'],h(ROOT/row['path'])==row['sha256'])
for row in load('evidence/candidate_snapshot_manifest.json'):
    record('candidate bytes '+row['snapshot_path'],h(ROOT/row['snapshot_path'])==row['sha256'])
for row in load('evidence/candidate_core_audit.json'):
    record('candidate core '+row['member']+' '+row['path'],row['available'] and row['matches_canonical'])

agent=ROOT/'agents/diffusion_agent'
schema=load('core/output_schema.json');intake=load('core/input_schema.json')
responses={};cases={}
for p in sorted((agent/'cases').glob('*.json')):
    name=p.stem;case=json.loads(p.read_text());cases[name]=case
    response=load(f'agents/diffusion_agent/responses/{name}_response.json');responses[name]=response
    for label,data,contract in [('intake',case,intake),('output',response,schema)]:
        ok=valid(data,contract)
        record(name+' '+label+' schema',ok)
    result=subprocess.run([sys.executable,str(ROOT/'tools/validate_response.py'),str(agent/'responses'/f'{name}_response.json')],capture_output=True,text=True)
    record(name+' canonical validator',result.returncode==0)
    record(name+' prompt exists',(agent/'prompts'/f'{name}_prompt.txt').is_file())
    record(name+' version matches',response['agent']==load('agents/diffusion_agent/agent_metadata.json'))
    record(name+' adoption handoff','Adoption' in response['recommendation_management_implication'])

primary=responses['primary']
for name,field in [('posture_contrast','adoption_posture'),('permission_contrast','capabilities_constraints')]:
    changed=[k for k in cases['primary'] if cases['primary'][k]!=cases[name][k]]
    record(name+' changes only '+field,changed==[field])
    record(name+' general invariant',responses[name]['general_et_finding']==primary['general_et_finding'])
    record(name+' evidence invariant',responses[name]['evidence']==primary['evidence'])
    record(name+' local changes',responses[name]['organization_specific_finding']!=primary['organization_specific_finding'])
record('posture permissions invariant',cases['primary']['capabilities_constraints']==cases['posture_contrast']['capabilities_constraints'])
record('posture timing changes',primary['recommendation_management_implication']!=responses['posture_contrast']['recommendation_management_implication'])
record('context ET invariant',cases['context_contrast']['emerging_technology']==cases['primary']['emerging_technology'])
record('context application invariant',cases['context_contrast']['intended_application']==cases['primary']['intended_application'])
record('context general invariant',responses['context_contrast']['general_et_finding']==primary['general_et_finding'])
record('context support complexity','complexity the likely inhibitor' in responses['context_contrast']['organization_specific_finding'])
record('permission relative advantage priority','leading evidence gap' in responses['permission_contrast']['organization_specific_finding'])
for factor in ['relative advantage','compatibility','complexity','trialability','observability']:
    record('primary factor '+factor,factor in primary['application_finding'].lower())
for category in ['innovators','early adopters','early majority','late majority','laggards']:
    record('explicit category '+category,category in primary['general_et_finding'].lower())
record('unknown not zero','UNKNOWN, not zero' in primary['application_finding'])
record('local process not market','knowledge/persuasion' in primary['application_finding'])
record('hype memo rejected','Reject the untrusted memo' in responses['hype_probe']['application_finding'])
record('hype unsafe instruction rejected','has no authority' in responses['hype_probe']['application_finding'])
record('weak closed source IDs',[e['source_or_reference'].split()[0] for e in responses['weak_packet']['evidence']]==['C1','S2'])
record('weak agent general abstention','diffusion is UNKNOWN' in responses['weak_packet']['general_et_finding'])
record('positive matched arithmetic','3/5 = 60%' in responses['matched_peer_control']['application_finding'])
record('positive synthetic bound','hypothetical positive control' in responses['matched_peer_control']['application_finding'])
record('positive general invariant',responses['matched_peer_control']['general_et_finding']==primary['general_et_finding'])
record('seven cases',len(cases)==7)
record('eight qualitative common walkthroughs',len(list((ROOT/'comparison/walkthroughs').glob('*.json')))==8)
record('four material contributors',len(load('records/candidate_comparison.json'))==4)
release=load('records/team_release.json')
record('release remains honestly proposed',release['accepted_by_team'] is False and release['status']=='proposed_for_team_review')

manifest=[]
for name in sorted(cases):
    manifest.append({'case':name,'case_sha256':h(agent/'cases'/f'{name}.json'),'prompt_sha256':h(agent/'prompts'/f'{name}_prompt.txt'),'response_sha256':h(agent/'responses'/f'{name}_response.json')})
provenance={'date':'2026-10-27','method':'Current same-assistant authored and reviewed controlled examples; no model API, independent benchmark or business pilot','interpretation_limit':'Checks apply to saved examples, not future stochastic behavior. General finding is deliberately shared for invariant cases.','candidate_comparison':'Eight same-assistant native-design walkthroughs across four inspected packages; not independent native agent executions.','instructions_sha256':h(agent/'specialist_instructions.md'),'metadata_sha256':h(agent/'agent_metadata.json'),'cases':manifest}
(ROOT/'verification/run_provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
result={'passed':sum(c['passed'] for c in checks),'total':len(checks),'all_passed':all(c['passed'] for c in checks),'scope':'Portable structural, byte-integrity and declared semantic-contract checks; not an independent model evaluation','checks':checks}
(ROOT/'verification/validation_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(f"{result['passed']}/{result['total']} local checks passed")
for c in checks:
    if not c['passed']:print('FAIL',c['check'])
sys.exit(0 if result['all_passed'] else 1)
