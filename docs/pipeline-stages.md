# Pipeline Stages

Machine-readable version: [`crm/pipeline.json`](../crm/pipeline.json)

| # | Stage | Entry criteria | Automation fired | Exit |
|---|---|---|---|---|
| 1 | New Inquiry | Contact created from any source | A2 Speed-to-Lead | Two-way contact |
| 2 | Contacted | Two-way conversation logged | A3 Qualifier | Score assigned |
| 3a | Qualified: Hot | `lead_score` = Hot | LO SMS alert; A4 book within 24h | Booked |
| 3b | Qualified: Warm | `lead_score` = Warm | A4 book; light cadence | Booked or Nurture |
| 3c | Qualified: Nurture | `lead_score` = Nurture | A9 drip; 30-day recheck | Re-engaged |
| 4 | Consult Booked | Appointment created | W3 confirmations and reminders | Held / no-show |
| 5 | Consult Held | LO marks held | Portal link sent; W4 24h timer | App started |
| 6 | Application Started | POS status = started | W4 if not submitted in 24h | Submitted |
| 7 | Application Submitted | POS/LOS = submitted | Milestone msg; initial doc list (W5) | Docs requested |
| 8 | Processing: Docs Outstanding | Needs list open | W5 Document Chaser | Needs list clear |
| 9 | Submitted to Underwriting | LOS milestone | Milestone msg | Decision |
| 10 | Conditional Approval | LOS milestone | Milestone msg; W5 on conditions | Conditions clear |
| 11 | Clear to Close | LOS milestone | Milestone msg; W7 starts | Closing set |
| 12 | Closing Scheduled | `closing_date` set | W7 closing coordination | Funded |
| 13 | Funded / Closed Won | LOS funded | W8 post-close | n/a |
| 14 | Lost / Withdrawn / Not Qualified | Manual or automated | Capture reason; A9 Nurture | Re-engaged |

## Lost reasons (required when moving to stage 14)
`chose_other_lender` · `not_ready` · `not_qualified_now` · `property_fell_through` · `unresponsive` · `out_of_footprint` · `product_not_offered` · `other`
