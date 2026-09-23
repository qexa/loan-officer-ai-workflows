# W3: Appointment Scheduling & No-Show Recovery

**Agent:** A4 · **Bookable:** Mortgage Consultation (30 min)

## Booking
1. Offer 2–3 slots (Hot: within 24h).
2. Capture phone/video → `appt_type`.
3. Book → stage 4 "Consult Booked."
4. Send **SMS-03** confirmation + **EM-02** with calendar invite and pre-consult checklist.
5. A10 sends the LO a pre-consult brief 30 minutes before.

## Reminders
| Timing | Channel | Template |
|---|---|---|
| 24h before | SMS + email | SMS-06 |
| 2h before | SMS | SMS-07 |

Reply handling: `C` → confirmed · `R` → reschedule flow · other → A1

## No-show recovery
| Timing | Channel | Template |
|---|---|---|
| +10 min | SMS | SMS-08 |
| +1 hour | Voice (A4) | "We missed you" script |
| +1 day | SMS | SMS-09 |
| +3 days | Email | EM-02b |
| +7 days | SMS | SMS-05 |
| +8 days | Move to Nurture; tag `no-show` | n/a |

## After consult
LO marks **Held** → stage 5; send portal link (SMS-10) and start W4 24h timer. LO marks **No-Show** → recovery above.

## KPIs
Booking rate, show rate (target > 80%), reschedule recovery rate.
