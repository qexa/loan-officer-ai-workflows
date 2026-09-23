# Workflows

Every workflow spec follows the same structure: **Trigger → Entry conditions → Steps (timing, channel, template, agent) → Branches → Exit → SLA → Fields & tags updated → Failure handling.**

| ID | Workflow | Agents | Templates |
|---|---|---|---|
| [W1](w1-inbound-inquiry.md) | Inbound Loan Inquiry | A1, A3, A4, A8 | SMS-02, EM-01 |
| [W2](w2-lead-qualification.md) | Lead Qualification | A3 | n/a |
| [W3](w3-appointment-scheduling.md) | Scheduling & No-Show Recovery | A4 | SMS-03 to SMS-09, EM-02 |
| [W4](w4-application-follow-up.md) | Application Follow-Up | A5 | SMS-10, SMS-11, EM-03, EM-04 |
| [W5](w5-document-collection.md) | Document Collection & Conditions | A6 | SMS-12 to SMS-14, EM-05, EM-06 |
| [W6](w6-milestone-updates.md) | Milestone Updates | A7 | MS-01 to MS-08 |
| [W7](w7-closing-coordination.md) | Closing Coordination | A7 | SMS-15 to SMS-17, EM-07 |
| [W8](w8-post-close-recapture.md) | Post-Close & Recapture | A9 | SMS-18, SMS-19, EM-08 to EM-10 |
| [W9](w9-lo-daily-brief.md) | LO Daily Brief | A10 | n/a |

## Global gates (apply to every outbound step)
1. `dnc_flag` = false and no `do-not-contact` tag
2. SMS step: `sms_consent` = true · Voice step: `voice_ai_consent` = true · Email marketing: `email_opt_in` = true (transactional loan emails excepted)
3. Current time within the contact's allowed window (default 9 AM–7 PM local, Mon–Sat)
4. If a gate fails: skip the step, try the next allowed channel, and log the skip
