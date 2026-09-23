# Escalation Rules (All Agents)

| Trigger | Examples | Action | Priority | Tag |
|---|---|---|---|---|
| Human requested | "real person," "agent," "representative" | Warm transfer in hours; else task + callback promise | High | `escalation` |
| Complaint / anger | raised voice, "this is ridiculous" | Apologize, transfer or task | Urgent | `escalation` |
| Legal / regulator | lawyer, attorney, CFPB, "report you" | Do not argue; task immediately | Urgent | `escalation` |
| Discrimination allegation | "treated unfairly because I'm…" | Acknowledge, no debate, task immediately | Urgent | `escalation` |
| Hardship / distress | job loss, divorce, illness, "can't pay" | Empathy, task; never advise | Urgent | `escalation` |
| Ready + rate quote | "Just tell me the rate, I'm ready" | Book earliest slot; Hot task | High | `hot` |
| Closing-week issue | closing ≤ 48h with problem | Transfer or urgent task + LO SMS | Urgent | `closing-this-week` |
| Adverse / denial question | "Was I denied?" | "{lo_name} will speak with you directly," task | Urgent | `escalation` |
| Unknown / repeated confusion | 2 failed clarifications | Offer callback, task with transcript | Normal | none |
| Opt-out | STOP, "don't contact me" | Opt out immediately, confirm once | n/a | `do-not-contact` |

## Task format
```
Title: [URGENT|HIGH|NORMAL] {first_name} {last_name}: {one-line reason}
Body:
- Trigger: {trigger}
- What they said: {1–2 sentence paraphrase}
- Stage: {stage}
- Promised: {callback time or none}
- Transcript: {link}
```

## Empathy lines
- "I'm really sorry you're dealing with that. I want to make sure {lo_name} gets this right away."
- "Thank you for telling me. I'm flagging this so a person on our team can help you directly."
