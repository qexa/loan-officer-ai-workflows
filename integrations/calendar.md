# Calendar Integration

- **Provider:** Google Calendar or Microsoft Outlook, two-way sync
- **Bookable:** "Mortgage Consultation," 30 min, phone or video
- **Buffers:** 15 min after; 2h minimum notice; 30-day booking window
- **Hot lead holds:** optional two 30-minute daily "hot lead" blocks the Scheduler can release
- **Team routing:** round-robin or by `property_state` licensing; skip LOs not licensed in that state
- **Video link:** auto-generate (Zoom, Google Meet, Teams) into the invite
- **Time zones:** book in the borrower's time zone; show both zones in LO invite
- **Invite title:** `Mortgage Consult: {first_name} {last_name} ({loan_purpose})`
- **Invite body:** pre-consult brief link from A10 (no sensitive data)
