#!/usr/bin/env python3
# Builds a personalized borrower document checklist from checklists/*.json.
# Example:
#   python scripts/build_checklist.py --loan-type va --income w2 rental --purpose purchase
#   python scripts/build_checklist.py --loan-type conventional --income self_employed --purpose refinance --format sms
import argparse
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1] / "checklists"


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def build(loan_type, incomes, purpose, conditions=None):
    items = list(load("base.json")["items"])
    items += load("loan-purpose.json").get(purpose, [])
    items += load("loan-types.json").get(loan_type, [])
    inc = load("income-types.json")
    for i in incomes:
        items += inc.get(i, [])
    if conditions:
        cond = {c["id"]: c for c in load("conditions.json")["items"]}
        items += [cond[c] for c in conditions if c in cond]
    seen, out = set(), []
    for it in items:
        if it["id"] not in seen:
            seen.add(it["id"])
            out.append(it)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--loan-type", default="conventional",
                    choices=["conventional", "fha", "va", "usda", "jumbo"])
    ap.add_argument("--income", nargs="+", default=["w2"],
                    choices=["w2", "self_employed", "1099", "retired", "rental", "support"])
    ap.add_argument("--purpose", default="purchase", choices=["purchase", "refinance"])
    ap.add_argument("--conditions", nargs="*", default=[])
    ap.add_argument("--format", default="md", choices=["md", "sms", "json"])
    a = ap.parse_args()
    items = build(a.loan_type, a.income, a.purpose, a.conditions)

    if a.format == "json":
        print(json.dumps({"docs_outstanding": [i["id"] for i in items], "items": items}, indent=2))
    elif a.format == "sms":
        print("; ".join(i["name"] for i in items))
    else:
        print(f"# Document checklist ({a.loan_type}, {a.purpose}, {', '.join(a.income)})\n")
        for n, i in enumerate(items, 1):
            print(f"{n}. **{i['name']}**: {i['why']}")
            if i.get("where_to_find"):
                print(f"   _Where to find it:_ {i['where_to_find']}")
        print(f"\nTotal items: {len(items)}")


if __name__ == "__main__":
    main()
