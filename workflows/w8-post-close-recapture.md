# W8: Post-Close & Recapture

**Trigger:** stage 13 Funded · **Agent:** A9 · Tag `past-client`

| Timing | Channel | Template |
|---|---|---|
| Day 1 | SMS + email | SMS-18, EM-08 thank-you + review request |
| Day 30 | SMS | SMS-19 check-in + referral ask |
| Month 6 | Email | EM-09 homeowner tips |
| Annual (funded date) | Email + SMS | EM-10 home anniversary |
| Ongoing | Email | Quarterly homeowner newsletter |

## Rate-watch (internal)
Nightly job compares a market-rate reference to `note_rate`. If the gap meets the LO's configured threshold → tag `rate-watch` + LO task. **No automated borrower rate messaging.**

## Limits
Referral asks max 2/year. Honor opt-outs everywhere.
