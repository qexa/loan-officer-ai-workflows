# Document Checklists

Machine-readable checklists that A6 combines into a personalized list:

`base` + `loan-purpose[purchase|refinance]` + `loan-types[type]` + `income-types[each income type]` + any active `conditions`

Each item has an `id` (stored in `docs_outstanding`), a borrower-friendly `name`, a plain-language `why`, and a `where_to_find` tip.

Build one from the command line:

```bash
python scripts/build_checklist.py --loan-type va --income w2 rental --purpose purchase
python scripts/build_checklist.py --loan-type conventional --income self_employed --purpose refinance --format sms
```

Duplicates across lists are removed automatically (first occurrence wins).
