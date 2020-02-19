#! python3
# tenant_creation.py - Script to facilitate the creation of tenants in Magnum by adding the case number to the start of the teant's enrolment.

# Imports #
import sys, pyperclip

# Variables #
user_clipboard = pyperclip.paste()          # Variable containing user's clipboard
user_list = user_clipboard.split()          # Converting user's clipboard to a list
clt = user_list[0]                          # CLT number
enrolment_list = user_list[1:]              # List with only enrolments
parsed_list = []                            # Final list with CLT_ENROLMENT

# Logic #
for enrolment in enrolment_list: # Loop adding CLT_ to each enrolment
    parsed_list.append(clt + '_' + enrolment)

pyperclip.copy('\n'.join(parsed_list)) # Saving final list to clipboard as string