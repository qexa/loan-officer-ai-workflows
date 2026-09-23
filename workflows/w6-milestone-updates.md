# W6: Milestone Updates

**Agent:** A7 · **Trigger:** LOS milestone webhook → stage change

| Milestone | Template | Borrower | Agents/Title* |
|---|---|---|---|
| Application submitted | MS-01 | ✅ | Buyer's agent |
| Appraisal ordered | MS-02 | ✅ | Listing agent (access) |
| Appraisal received | MS-03 | ✅ status only | Buyer's agent (status) |
| Submitted to underwriting | MS-04 | ✅ | Buyer's agent |
| Conditional approval | MS-05 | ✅ | Buyer's agent |
| Clear to close | MS-06 | ✅ | All |
| Closing Disclosure sent | MS-07 | ✅ | n/a |
| Funded | MS-08 | ✅ | All |

*Only when `partner_updates_consent` = true.

## Rules
- Status only. No values, conditions, amounts, rates, or adverse news.
- Backward movement → no borrower message; LO task.
- Suppress duplicate milestones within 24 hours.
