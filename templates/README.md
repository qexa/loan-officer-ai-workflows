# Templates

| Folder | Contents |
|---|---|
| [sms/](sms/) | SMS-01 to SMS-19, MS-01 to MS-08, SMS-LO-01 |
| [email/](email/) | EM-01 to EM-10, nurture drip (12 months), footer |
| [voice-scripts/](voice-scripts/) | Receptionist, outbound, doc chaser, guardrail responses |

## Rules
- **SMS:** under 300 characters; include `{company_name}`; first message to a contact includes "Reply STOP to opt out."
- **Email:** subject + preview text; LO signature with NMLS; company NMLS; Equal Housing Opportunity (see `email/footer.md`).
- **Never** include rates, payments, approval language, SSN requests, or wiring instructions. `scripts/validate.py` scans for these.
