# W1: Inbound Loan Inquiry

**Trigger:** inbound call, web chat, or SMS to the main number
**Agents:** A1 → A3 → A4 → A8
**Goal:** every inquiry gets a helpful answer and a clear next step

## Steps
| # | Action | Detail |
|---|---|---|
| 1 | Answer | A1 greets with AI + recording disclosure |
| 2 | Lookup | Search contact by phone; if found, load stage and fields |
| 3 | Identify intent | New lead / existing borrower / partner / vendor / unclear |
| 4a | New lead | Capture name, mobile, email, consent → A3 Qualifier |
| 4b | Existing borrower | Verify (name + phone or loan #) → status from `stage_plain_language` → doc link if needed |
| 4c | Partner | Capture details → tag `realtor-partner` → transfer or high-priority task |
| 4d | Vendor | Message only; tag `vendor` |
| 5 | Route by score | Hot/Warm → A4; Nurture → A9; Refer-Out → polite close |
| 6 | Recap | SMS-02 + EM-01 (if booked, A4 sends SMS-03 instead) |
| 7 | Update | A8 writes note, fields, tags, stage |

## Branches
- Caller requests a human → escalation rules (transfer in hours, else urgent task)
- Caller objects to recording → stop recording where supported, offer human callback
- Non-English caller → Spanish variant if configured; else callback task noting language

## Fields & tags
`lead_source`, `loan_purpose`, consent fields, qualification fields, `last_contact_date`, `next_action` · Tags: score tag, `realtor-partner`, `vendor`, `escalation`

## SLA
Answer rate 100%. Hot lead → LO alert within 1 minute.

## Failure handling
Transfer fails → apologize, create urgent task, promise callback time. Lookup fails → treat as new and flag for dedupe.
