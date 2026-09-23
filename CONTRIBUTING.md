# Contributing

Thanks for helping loan officers spend less time on admin.

## Ways to contribute
- **Loan officers and processors:** real-world edge cases, better borrower wording, missing documents or conditions
- **Compliance professionals:** corrections, state-specific notes, review of scripts and templates
- **Automation builders:** platform translations (GoHighLevel, HubSpot, Salesforce, Retell, Vapi), integration mappings, scripts

## Ground rules
1. **Never commit real borrower data.** Use obviously fake examples (Jane Sample, 555-0100).
2. **Keep the guardrails.** Contributions that let an AI quote rates, promise approval, collect SSNs, or skip consent will not be merged.
3. **Use canonical names.** Agents A1 to A10, workflows W1 to W9, fields and tags from `crm/`, tokens from the README.
4. **Run the validator** before opening a PR:
   ```bash
   python scripts/validate.py
   ```
5. **Plain language** in anything borrower-facing (about an 8th-grade reading level).

## Pull request process
1. Fork and create a branch: `feature/short-description`
2. Make changes and run `python scripts/validate.py`
3. Update `CHANGELOG.md` under an "Unreleased" heading
4. Open a PR using the template and describe the compliance impact, if any
