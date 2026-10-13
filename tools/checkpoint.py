#!/usr/bin/env python3
"""Validate checkpoint integrity and create a portable checkpoint; no generation."""
import argparse, hashlib, json, pathlib, re, sys, zipfile
root=pathlib.Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument("--check",action="store_true")
p.add_argument("--production-ready",action="store_true")
p.add_argument("--bundle",type=pathlib.Path)
a=p.parse_args()
s=json.loads((root/"issues/04/status.json").read_text())
d=json.loads((root/"issues/04/production/QA dependencies.json").read_text())
script=(root/s["script"]["path"]).read_bytes()
pages=[int(x) for x in re.findall(rb"^## PAGE (\d+)",script,re.M)]
errors=[]
if pages != list(range(1,23)): errors.append("Script must contain Pages 1–22 in order")
actual=hashlib.sha256(script).hexdigest()
if actual!=s["script"]["source_reported_sha256"]: errors.append("Script differs from recorded original hash")
if a.production_ready:
 for item in d["requirements"]:
  if not item["path"] or not (root/item["path"]).is_file(): errors.append("Missing actual input: "+item["id"])
 if not s["production_ready"]: errors.append("Production readiness not established")
 if s["edit_count"] is None: errors.append("Historical edit count unknown")
 if s["usage_authorization"] is None: errors.append("Current usage authorization absent")
if errors:
 print("\n".join(errors)); sys.exit(1)
entries=[]
for f in sorted(root.rglob("*")):
 if f.is_file() and ".git" not in f.parts and "__pycache__" not in f.parts:
  entries.append({"path":str(f.relative_to(root)),"sha256":hashlib.sha256(f.read_bytes()).hexdigest(),"size":f.stat().st_size})
if a.bundle:
 with zipfile.ZipFile(a.bundle,"w",zipfile.ZIP_DEFLATED) as z:
  for e in entries: z.write(root/e["path"],"super-dukie/"+e["path"])
  z.writestr("CHECKPOINT-MANIFEST.json",json.dumps({"kind":"migration_checkpoint","production_ready":s["production_ready"],"files":entries},indent=2))
 print(str(a.bundle.resolve()))
print("Checkpoint integrity passed; production readiness "+str(s["production_ready"]))
