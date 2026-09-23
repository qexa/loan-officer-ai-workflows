# W5: Document Collection & Conditions

**Agent:** A6
**Trigger:** LOS needs list or conditions change (webhook) → updates `docs_outstanding`; tag `docs-outstanding` or `conditions-open`

## Steps
1. Build the personalized list: `scripts/build_checklist.py` logic (base + loan type + income types + conditions).
2. Send **SMS-12** + **EM-05** with the item list and `{portal_link}`.
3. Chase cadence while any item is outstanding:

| Touch | Timing | Channel | Template |
|---|---|---|---|
| 1 | Day 0 | SMS + email | SMS-12, EM-05 |
| 2 | +48h | SMS | SMS-13 |
| 3 | +96h | Email | EM-06 |
| 4 | +120h | Voice | A6 help call |
| 5+ | every 48h | alternate | SMS-13 / EM-06 |

4. On upload webhook: remove item, send **SMS-14** ("Got it! X items left"), notify processor.
5. When the list is empty: remove tag, send thank-you, stage advances per LOS.

## SLA and escalation
| Condition | Action |
|---|---|
| Item outstanding 5 days | `doc_sla_status` = At Risk; LO task |
| 3 days before lock expiry or closing | `doc_sla_status` = Overdue; urgent LO task + SMS to LO |
| Borrower can't obtain item | LO task |
| Document received via SMS/email | Redirect to portal; notify processor to handle insecure receipt |

## Security
Documents are NEVER requested or accepted by SMS/email.
