# POS Mapping

| POS event | CRM update | Workflow |
|---|---|---|
| Invite sent | `portal_link` | n/a |
| Application started | `application_status` = Started; stage `app_started` | W4 timer (2h) |
| Section completed | `sections_remaining` (optional) | EM-03 personalization |
| Application submitted | `application_status` = Submitted; stage `app_submitted` | W6 MS-01, W5 initial list |
| Document uploaded | Remove matching ID from `docs_outstanding` | W5 SMS-14 |
| All documents received | Remove tag `docs-outstanding` | Thank-you |

**Security:** only event metadata flows to the CRM. Documents stay in the POS.
