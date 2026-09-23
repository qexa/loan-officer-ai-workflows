# Compliance Guardrails

> ⚠️ **Framework, not legal advice.** Rules vary by state and change over time. Have the lender's compliance officer or counsel approve every script, template, consent form, and workflow before launch, and re-review at least annually.

## 1. SAFE Act and NMLS licensing
**Rule:** Only NMLS-licensed MLOs may take a residential mortgage loan application or offer or negotiate rates and terms.

**Enforcement:**
- Every agent prompt includes a PROHIBITED block: no rates, APRs, payments, fees, approval odds, or term negotiation.
- Standard deflection scripts (`templates/voice-scripts/guardrail-responses.md`).
- Weekly transcript audit (`tests/qa-rubric.md`).
- `scripts/validate.py` scans templates for banned phrases.

## 2. TRID (TILA-RESPA Integrated Disclosure)
**Rule:** Receipt of six items (name, income, SSN, property address, estimated property value, loan amount) constitutes an application and starts the 3-business-day Loan Estimate clock.

**Enforcement:** AI agents **never collect SSNs**. Qualification captures self-reported ranges only. The formal application happens in the POS.

## 3. TCPA
**Rule:** The FCC treats AI-generated voices as "artificial or prerecorded voice." Calls using them to mobile numbers, and marketing texts, require prior express written consent. Consent can be revoked by any reasonable means.

**Enforcement:**
- Consent checkbox on every form, with timestamp, source URL, and exact disclosure language stored in `sms_consent_timestamp`, `consent_source`, `voice_ai_consent`.
- Every outbound workflow step checks consent before sending.
- STOP, UNSUBSCRIBE, CANCEL, END, QUIT, and plain-language revocations ("don't text me") trigger opt-out.
- Internal Do Not Call list and national DNC scrub for marketing outreach.

**Sample consent language (have counsel approve):**
> By checking this box, I agree that {company_name} and its loan officers may contact me about my mortgage inquiry at the number provided, including by calls and texts using automated technology and artificial or AI-generated voices. Consent is not a condition of any purchase or loan. Message and data rates may apply. Reply STOP to opt out.

## 4. Quiet hours
Federal minimum: no calls/texts before 8:00 AM or after 9:00 PM in the recipient's local time. Several states are stricter (narrower hours, Sunday/holiday limits, attempt caps). Default in this system: **9:00 AM to 7:00 PM local, Monday to Saturday**, configurable per state.

## 5. Call recording and AI disclosure
Some states require all-party consent to record. Every call opens with an AI assistant disclosure and a recording notice. If the caller objects, stop recording (or end the recorded portion) and offer a human callback.

## 6. A2P 10DLC
Carriers require brand and campaign registration for business texting on 10-digit numbers. Register before launch; approval can take 1 to 3 weeks. Sample messages submitted must match actual usage.

## 7. ECOA / Regulation B / Fair Housing Act
**Rule:** No discrimination on the basis of race, color, religion, national origin, sex, marital status, age, receipt of public assistance, good-faith exercise of consumer credit rights, familial status, or disability.

**Enforcement:**
- One qualification script (W2), same questions, same order, for every lead.
- Scoring uses only timeline, loan purpose, property facts, and self-reported ranges.
- Agents never ask about protected characteristics and never steer toward or away from products or neighborhoods.
- Monthly fair-lending review of a transcript sample.

## 8. Adverse action
The AI never communicates denials, counteroffers, or adverse decisions. It creates an urgent task for the LO, who handles required notices.

## 9. GLBA Safeguards Rule
- No NPI in SMS/email.
- Secure portal for all documents.
- Least-privilege access, MFA, vendor agreements, retention policy.

## 10. UDAAP and advertising
No "guaranteed approval," "lowest rate," "no credit check," or similar claims. Include company name, NMLS IDs where required, and the Equal Housing Opportunity statement in marketing email.

## 11. State licensing
Agents only engage on properties in states where the LO is licensed. Other states are politely referred out (tag `refer-out`).

## Enforcement matrix

| Guardrail | Prompt | Workflow gate | Template scan | QA audit |
|---|---|---|---|---|
| No rates / approval | ✅ | | ✅ | ✅ |
| No SSN | ✅ | | ✅ | ✅ |
| Consent | | ✅ | | ✅ |
| Quiet hours | | ✅ | | |
| AI/recording disclosure | ✅ | | | ✅ |
| Fair lending | ✅ | | | ✅ |
| No adverse action | ✅ | | ✅ | ✅ |
| Wire fraud warning | | ✅ | ✅ | |
