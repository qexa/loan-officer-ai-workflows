# FAQ

**Can the AI take a loan application?**
No. Taking an application is licensed activity, and collecting all six TRID items starts the Loan Estimate clock. The AI qualifies with self-reported ranges and hands off to the POS and the licensed LO.

**What if a borrower insists on a rate quote?**
The AI explains that rates depend on the borrower's full profile, offers the earliest consult slot, and creates a Hot task for the LO.

**Will borrowers know they're talking to AI?**
Yes. Every call opens with a disclosure, and the AI answers honestly if asked.

**What about Spanish-speaking borrowers?**
Configure a Spanish variant of A1 and the templates, reviewed by a fluent speaker and compliance. Serve every language with the same qualification criteria.

**Does this replace my processor?**
No. It removes the chasing and status calls so your processor can focus on the file.

**Which LOS/POS systems are supported?**
Anything that can send webhooks or connect through Zapier or Make. See `integrations/`.

**Can I use this on a platform other than Votel.ai?**
Yes. The prompts, workflows, templates, and data model are platform-agnostic. The deployment guide uses Votel.ai terminology.

**How do I use this with Claude?**
Paste `docs/claude-project-instructions.md` into a Claude Project's instructions and upload the repo files as knowledge.
