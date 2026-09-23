# Deployment Guide: Votel.ai / AutoAnswer.app

This guide builds the full system in phases. Each phase ends with a checkpoint. Terms follow Votel.ai conventions; translate for other platforms as needed.

## Prerequisites
- [ ] Votel.ai account (or AutoAnswer.app sub-account) with AI agents, voice, SMS, email, and workflows enabled
- [ ] LO information: name, photo, bio, NMLS ID, company NMLS ID, licensed states, products
- [ ] Calendar (Google or Outlook) with availability rules
- [ ] LOS and POS admin access or API/webhook credentials
- [ ] Compliance officer contact for approvals

---

## Phase 1: Foundation (Weeks 1–2)
1. **Start A2P 10DLC registration** (brand + campaign). Do this first; approval takes time.
2. **Buy or port a local phone number.** Enable call recording.
3. **Create custom fields** from `crm/custom-fields.json`. Keep the exact keys; every prompt and workflow references them.
4. **Create tags** from `crm/tags.json`.
5. **Create the pipeline** "Residential Loans" from `crm/pipeline.json`.
6. **Connect the calendar** and create a bookable "Mortgage Consultation" (30 min, phone or video, 15-min buffer, 2-hour minimum notice).
7. **Build the lead form** with TCPA consent language from `docs/compliance-guardrails.md`. Map to fields and set `consent_source` to the page URL.
8. **Create global variables** for `company_name`, `company_nmls`, `lo_name`, `lo_nmls`, `lo_phone`, `booking_link`.

✅ *Checkpoint:* a test form submission creates a contact with consent fields populated and lands in stage 1.

## Phase 2: Front Office (Weeks 2–4)
1. Create **A3 Qualifier** and **A4 Scheduler** as subagents (prompts in `agents/`).
2. Create **A1 Receptionist**; attach A3 and A4; load `agents/a1-receptionist/knowledge-base.md`; configure escalation transfer number.
3. Create **A2 Speed-to-Lead**; attach A3 and A4.
4. Build **W1** (inbound), **W2** (qualification routing), **W3** (booking, reminders, no-show recovery) from `workflows/`.
5. Load SMS/email templates from `templates/`.

✅ *Checkpoint:* run scenarios T1 to T10 from `tests/call-scenarios.md`.

## Phase 3: Follow-Up (Weeks 4–5)
1. Create **A5 Application Follow-Up** and build **W4**.
2. Create **A9 Nurture & Recapture** and load the 12-month drip from `templates/email/nurture-drip.md`.

✅ *Checkpoint:* a contact moved to "Application Started" with no submission triggers W4 at +2h.

## Phase 4: Back Office (Weeks 5–7)
1. Connect LOS and POS using `integrations/` mappings (native, Zapier, or Make).
2. Create **A6 Document Chaser**; load `checklists/*.json`; build **W5**.
3. Create **A7 Milestone Messenger**; build **W6**.
4. Build **W7** closing coordination.

✅ *Checkpoint:* post `integrations/sample-payloads/los-milestone.json` to the webhook; stage and borrower message update correctly.

## Phase 5: Intelligence (Weeks 7–8)
1. Create **A8 CRM Updater**; trigger on call end and conversation close.
2. Create **A10 LO Copilot**; build **W9** as a weekday 7:30 AM scheduled task.
3. Build **W8** post-close.
4. Build dashboards from `dashboards/kpis.md`.

## Phase 6: QA and Launch (Weeks 8–9)
1. Run all 30 scenarios in `tests/call-scenarios.md`. Target 100% pass on guardrail scenarios.
2. Compliance officer signs off on scripts, templates, consent language.
3. Pilot with one LO for 2 weeks. Review 10 transcripts per week with `tests/qa-rubric.md`.
4. Tune the knowledge base and go live.

## Phase 7: Productize (Week 10+)
Save the configured account as a snapshot. See `packaging/`.
