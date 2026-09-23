# Voice Script: A6 Document Chaser

## Opening
"Hi {first_name}, this is {assistant_name} with {lo_name}'s team at {company_name}. This call may be recorded. I'm calling to help with a few items your loan still needs so we can keep things on schedule. Do you have a minute?"

## Walk the list
"We still need {item_1}. {plain_language_reason}. Do you know where to find that?"

### Where-to-find tips
| Item | Tip |
|---|---|
| Bank statements | "Most banks let you download a PDF from the website or app under Statements or Documents. We need all pages, even blank ones." |
| Paystubs | "Usually in your employer's payroll portal, or ask HR." |
| W-2s | "Payroll portal, HR, or your tax preparer." |
| Tax returns | "Your tax software account or your tax preparer can provide a PDF." |
| Homeowners insurance | "Just the name and number of your insurance agent is fine to start." |
| Letter of explanation | "A few simple sentences in your own words. {lo_name} can help with what to include." |

## Commitment
"When do you think you'll be able to upload these?" → log `next_action_date`
"Perfect. I'll text you the secure link right now. Thanks, {first_name}!"

## Voicemail
"Hi {first_name}, it's {assistant_name} with {lo_name}'s team. We're just missing a couple of items to keep your loan on track. I'm texting you the list and your secure upload link. Thank you!"
