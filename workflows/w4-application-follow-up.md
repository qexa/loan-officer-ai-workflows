# W4: Application Follow-Up

**Agent:** A5
**Trigger:** `application_status` = Started for 2h, or stage = Consult Held for 24h with `application_status` = Not Started
**Exit:** `application_status` = Submitted, opt-out, or "not ready"

| Timing | Channel | Template / Action |
|---|---|---|
| +2 hours | SMS | SMS-11 resume link |
| Day 1 | Email | EM-03 "Here's where you left off" |
| Day 2 | Voice | A5 help call |
| Day 4 | SMS | SMS-10 + LO task "Personal call" |
| Day 7 | Email | EM-04 final friendly note |
| Day 8 | Stage → Nurture; tag `app-stalled`; recheck in 30 days | n/a |

## Branches
- Borrower requests help → A4 books a 15-minute help call
- Borrower says using another lender → tag, stage 14 reason `chose_other_lender`, A9 nurture
- Borrower says not ready → A9 nurture with `next_action_date` +30d

## Fields
`application_status`, `next_action`, `next_action_date`, tag `app-stalled`
