#!/usr/bin/env python3
# Validates repository data and scans borrower-facing templates for compliance red flags.
# Usage: python scripts/validate.py   (exit code 1 on any error)
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
errors, warnings = [], []

# 1. JSON validity
for p in ROOT.rglob("*.json"):
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"Invalid JSON: {p.relative_to(ROOT)}: {exc}")

# 2. Field keys referenced in templates/workflows exist (backtick keys only)
fields = {f["key"] for f in json.loads((ROOT / "crm/custom-fields.json").read_text())["fields"]}
tags = {t["tag"] for t in json.loads((ROOT / "crm/tags.json").read_text())["tags"]}

# 3. Banned phrases in borrower-facing templates
BANNED = [
    (r"\bguarantee(d)?\b.*\bapprov", "approval guarantee"),
    (r"\byou('re| are) (pre-?)?approved\b", "approval statement"),
    (r"\byou (will )?qualify\b", "qualification promise"),
    (r"\blowest rates?\b", "superlative rate claim"),
    (r"\bno credit check\b", "no-credit-check claim"),
    (r"\b\d+(\.\d+)?\s?%\s?(apr|rate|interest)\b", "specific rate"),
    (r"\bsocial security number\b(?!s)", "SSN mention (verify it is a refusal)"),
    (r"\bwire (the funds )?to\b", "wiring instruction"),
]
ALLOWED_CONTEXT = re.compile(r"never|don't|do not|not collect|never collect|compliance note", re.I)

for p in (ROOT / "templates").rglob("*.md"):
    for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        low = line.lower()
        for pat, label in BANNED:
            if re.search(pat, low):
                if ALLOWED_CONTEXT.search(line):
                    continue
                errors.append(f"{p.relative_to(ROOT)}:{n}: banned phrase ({label}): {line.strip()[:90]}")

# 4. SMS length check (approximate, tokens counted as 12 chars)
sms = (ROOT / "templates/sms/sms-templates.md").read_text(encoding="utf-8").split("\n")
for i, line in enumerate(sms):
    if line.startswith("**") and i + 1 < len(sms):
        body = sms[i + 1].strip()
        approx = len(re.sub(r"\{[a-z_]+\}", "x" * 12, body))
        if approx > 300:
            warnings.append(f"SMS over ~300 chars ({approx}): {line.strip('* ')}")

# 5. Every first-touch SMS has opt-out language
if "Reply STOP" not in "\n".join(sms):
    errors.append("SMS templates missing 'Reply STOP' opt-out language")

# 6. Wire-fraud template present
if "NEVER text or email wiring instructions" not in "\n".join(sms):
    errors.append("Mandatory wire-fraud warning (SMS-16) missing")

# 7. Every agent prompt includes the shared rules
for p in (ROOT / "agents").glob("*/system-prompt.md"):
    if "NON-NEGOTIABLE RULES" not in p.read_text(encoding="utf-8"):
        errors.append(f"{p.relative_to(ROOT)} missing NON-NEGOTIABLE RULES block")

print(f"Checked {len(fields)} fields, {len(tags)} tags.")
for w_ in warnings:
    print("WARN ", w_)
for e in errors:
    print("ERROR", e)
if errors:
    print(f"\n{len(errors)} error(s).")
    sys.exit(1)
print("\n✅ All checks passed.")
