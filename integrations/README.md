# Integrations

| Doc | Purpose |
|---|---|
| [los-mapping.md](los-mapping.md) | LOS milestone → pipeline stage mapping and field sync |
| [pos-mapping.md](pos-mapping.md) | POS application and document events |
| [calendar.md](calendar.md) | Calendar sync and bookable settings |
| [lead-sources.md](lead-sources.md) | Inbound lead source mapping and consent handling |
| [sample-payloads/](sample-payloads/) | Example webhook payloads for testing |

**Pattern:** LOS/POS → webhook (native, Zapier, or Make) → CRM contact update by `los_loan_number` (fallback: phone, then email) → stage change → workflow fires.
