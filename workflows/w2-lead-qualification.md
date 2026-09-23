# W2: Lead Qualification

**Called by:** A1, A2, A5, A9 · **Agent:** A3
**Goal:** consistent, fair qualification and a score that drives routing

## Question order
See `agents/a3-qualifier/system-prompt.md` (Q1–Q13). Same questions, same order, every lead.

## Scoring rules
| Score | Rule | Stage | Routing |
|---|---|---|---|
| Hot | Purchase under contract or offers ≤ 30 days; refi with goal + need ≤ 30 days | 3a | A4 book ≤ 24h + LO SMS alert (SMS-LO-01) |
| Warm | Purchase 30–90 days; refi exploring | 3b | A4 book; warm cadence |
| Nurture | Purchase > 90 days; "just curious"; credit "rebuilding" + timeframe > 30 days | 3c | A9 drip; 30-day recheck |
| Refer-Out | Outside licensed states or product not offered | 14 (reason `out_of_footprint` / `product_not_offered`) | Polite close |

## Warm cadence (if not booked on first contact)
| Timing | Channel | Template |
|---|---|---|
| +1 day | SMS | SMS-04 |
| +3 days | Email | EM-02 |
| +5 days | Voice (A2) | script: speed-to-lead follow-up |
| +10 days | SMS | SMS-05 |
| +14 days | → Nurture | n/a |

## Fields written
`loan_purpose`, `property_state`, `property_county`, `occupancy`, `buying_timeframe`, `closing_date`, `est_price_or_value`, `down_payment_pct`, `est_loan_balance`, `refi_goal`, `credit_range_self_reported`, `income_type`, `va_eligible`, `first_time_buyer`, `has_agent`, `agent_name`, `lead_score`

## Compliance note
Scoring factors are limited to timeline, purpose, footprint, and product fit. Review a monthly sample for consistency across all leads.
