"""Parse .env-style text and apply local key policies."""
from __future__ import annotations
def parse(text:str)->tuple[dict[str,str],list[str]]:
 values={};duplicates=[]
 for line in text.splitlines():
  line=line.strip()
  if not line or line.startswith('#') or '=' not in line:continue
  key,value=line.split('=',1);key=key.strip()
  if key in values:duplicates.append(key)
  values[key]=value.strip()
 return values,duplicates
def check(text:str,required:list[str],forbidden:list[str])->dict:
 values,duplicates=parse(text);return {'missing':sorted(set(required)-set(values)),'forbidden':sorted(set(forbidden)&set(values)),'blank':sorted(key for key,value in values.items() if not value),'duplicates':sorted(set(duplicates))}
if __name__=='__main__':
 import json,sys;p=json.load(sys.stdin);print(json.dumps(check(p['text'],p.get('required',[]),p.get('forbidden',[])),indent=2))
