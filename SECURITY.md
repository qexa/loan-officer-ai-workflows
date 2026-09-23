# Security Policy

## Handling borrower data
This system touches nonpublic personal information (NPI) protected under the Gramm-Leach-Bliley Act (GLBA) Safeguards Rule.

- Never request or accept SSNs, full account numbers, or loan documents via SMS or email.
- Documents are collected only through the lender's secure POS portal.
- Limit CRM and platform access to the minimum roles needed. Enable MFA for all users.
- Execute vendor/service-provider agreements covering data protection with every platform in the stack.
- Retain call recordings and transcripts according to the lender's written retention policy.
- Never commit exports, recordings, or real contact data to this repository.

## Prompt-injection resilience
Agents are instructed to treat borrower messages, uploaded content, and web content as data, not instructions, and to stay in role. See test scenarios T21 and T29 in `tests/call-scenarios.md`.

## Reporting a vulnerability
Please do not open a public issue for security problems. Email security@qexa.com with details and steps to reproduce. We aim to respond within 3 business days.
