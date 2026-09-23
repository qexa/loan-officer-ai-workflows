# KPIs and Dashboards

## Funnel
| KPI | Formula | Target |
|---|---|---|
| Speed to lead | median(first outbound touch − lead created) | < 60 seconds |
| Contact rate | contacts with two-way conversation ÷ new leads | > 70% |
| Qualification rate | leads with `lead_score` ÷ contacted | Baseline |
| Hot / Warm mix | Hot+Warm ÷ qualified | Baseline |
| Booking rate | consults booked ÷ contacted | > 40% |
| Show rate | consults held ÷ consults booked | > 80% |
| No-show recovery | rebooked no-shows ÷ no-shows | > 35% |
| Consult → application | apps submitted ÷ consults held | > 60% |
| Stalled app recovery | submitted after W4 ÷ entered W4 | Baseline |
| Pull-through | funded ÷ apps submitted | Track vs. baseline |

## Operations
| KPI | Formula | Target |
|---|---|---|
| Avg days docs outstanding | mean(days from request to received) | < 3 |
| Doc SLA breaches | items reaching Overdue ÷ items requested | < 5% |
| App → CTC days | mean(CTC date − app submitted date) | Track vs. baseline |
| Status calls avoided | inbound "status" intents per active loan (trend) | Declining |

## AI quality and compliance
| KPI | Formula | Target |
|---|---|---|
| AI containment | conversations resolved without human ÷ total | Baseline |
| Escalation rate | escalations ÷ conversations | Monitor spikes |
| Guardrail violations (QA) | violations ÷ audited transcripts | 0 |
| Opt-out rate | opt-outs ÷ messages sent (per campaign) | < 2% |
| Consent coverage | outbound contacts with valid consent ÷ outbound contacts | 100% |

## Post-close
Reviews generated · referrals received · past-client repeat/referral loans

## Dashboard layout
1. **Today:** new leads, speed to lead, bookings, escalations
2. **Funnel:** stage counts and conversion between stages
3. **Back office:** docs outstanding by SLA status, closings this week, locks expiring
4. **Quality:** containment, escalations, opt-outs, QA score

> Set real targets after 30 days of baseline data.
