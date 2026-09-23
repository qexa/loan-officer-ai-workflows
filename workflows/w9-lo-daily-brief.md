# W9: LO Daily Brief

**Schedule:** weekdays 7:30 AM (LO local) · **Agent:** A10 · **Delivery:** email (full) + SMS (5-line summary)

## Data pulled
| Section | Query |
|---|---|
| Urgent | Open tasks tagged `escalation` or priority Urgent; `doc_sla_status` = Overdue; tag `closing-this-week` with open tasks |
| Today | Bookings today |
| Hot leads | `lead_score` = Hot, created last 24h |
| Stalled | tag `app-stalled`; stage 5 > 24h without app |
| Docs | `docs_outstanding` not empty, sorted by `next_action_date` |
| Locks | `lock_expiration_date` ≤ 7 days |
| Closings | `closing_date` this week |
| Metrics | Yesterday's KPIs |

## Sample SMS
```
☀️ Brief for Tue 9/22
🔴 2 urgent (1 closing-week issue)
📅 4 consults (first 9:30)
🔥 3 new hot leads, 2 booked
📄 6 files w/ docs out, 1 overdue
Full brief in your inbox.
```
