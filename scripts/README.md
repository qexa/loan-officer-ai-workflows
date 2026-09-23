# Scripts

Pure Python 3.9+, no dependencies.

| Script | Purpose |
|---|---|
| `validate.py` | Validates all JSON; scans templates for banned phrases (rates, approval promises, SSN requests, wiring); checks SMS length, opt-out language, wire-fraud template, and that every agent prompt includes the shared rules. Runs in CI. |
| `build_checklist.py` | Generates a personalized document checklist (Markdown, SMS text, or JSON with `docs_outstanding` IDs). |
