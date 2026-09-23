# LOS Mapping

Milestone names vary by LOS and lender configuration. Map your LOS milestones to these canonical stages.

| Canonical stage | Encompass (typical) | Arive (typical) | LendingPad (typical) | Fields synced |
|---|---|---|---|---|
| app_submitted | Started / Qualification | Application | Application | `los_loan_number`, `application_status`=Submitted |
| processing_docs | Processing | Processing | Processing | `docs_outstanding` from needs list |
| underwriting | Submittal | Submitted to UW | Submitted | n/a |
| conditional_approval | Approval / Cond. Approval | Approved w/ Conditions | Conditionally Approved | `docs_outstanding` from conditions |
| clear_to_close | Ready to Close / CTC | Clear to Close | CTC | n/a |
| closing_scheduled | Docs Out / Closing | Closing | Closing | `closing_date` |
| funded | Funding / Completion | Funded | Funded | `funded_date`, `note_rate` |
| lost | Adverse / Withdrawn | Withdrawn / Denied | Withdrawn / Denied | `lost_reason` (no borrower message) |

> Verify exact milestone names in your LOS configuration before go-live.

## Also sync
- `lock_expiration_date` on lock
- `assigned_processor`
- Needs list / conditions → `docs_outstanding` (map LOS condition names to checklist IDs; unmapped items → `loe_general` + LO task)

## Rules
- LOS is the source of truth; its stage overwrites the CRM stage.
- Adverse/denied/withdrawn from LOS → stage `lost`, **no automated borrower message**, LO task.
- Backward milestone → no borrower message, LO task.
