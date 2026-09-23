# AI Agents

Each folder contains a paste-ready `system-prompt.md` with configuration, the full prompt (including the shared non-negotiable rules), field mappings, and a test checklist.

| ID | Agent | Type | Channels | Calls |
|---|---|---|---|---|
| A1 | [Receptionist](a1-receptionist/) | Primary | Inbound voice, chat, SMS reply | A3, A4 |
| A2 | [Speed-to-Lead](a2-speed-to-lead/) | Primary | Outbound voice, SMS | A3, A4 |
| A3 | [Qualifier](a3-qualifier/) | Subagent | Any | n/a |
| A4 | [Scheduler](a4-scheduler/) | Subagent | Any | n/a |
| A5 | [Application Follow-Up](a5-app-follow-up/) | Primary | SMS, email, voice | A4 |
| A6 | [Document Chaser](a6-document-chaser/) | Primary | SMS, email, voice | n/a |
| A7 | [Milestone Messenger](a7-milestone-messenger/) | Primary | SMS, email | n/a |
| A8 | [CRM Updater](a8-crm-updater/) | Background | None (writes CRM) | n/a |
| A9 | [Nurture & Recapture](a9-nurture-recapture/) | Primary | Email, SMS | A4 |
| A10 | [LO Copilot](a10-lo-copilot/) | Internal | SMS/email/chat to LO | n/a |

## Shared rules
Every prompt ends with the same NON-NEGOTIABLE RULES block so behavior stays consistent across agents. If you change it, update all ten prompts together so they stay in sync.

## Global variables used
`{company_name}` `{company_nmls}` `{lo_name}` `{lo_nmls}` `{lo_phone}` `{booking_link}` `{licensed_states}` `{products_offered}` `{handoff_hours}` `{assistant_name}` (default "Ava")
