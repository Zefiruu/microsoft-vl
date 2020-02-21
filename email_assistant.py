#! /usr/bin/python3
# email_assistant.py - Script containing all important email templates. It will save the template to the User's clipboard.


# Imports #
import sys, pyperclip, shelve


# Agent name #
agent_data = shelve.open('agent_data')
if 'agent' in agent_data:
    agent = agent_data['agent']
else:
    agent = input('As this is your first time using this script, tell me your name: \n')
    agent_data['agent'] = agent

# Emails Section #

OP = 'Hello Team,\n\nThank you for placing your request with us.'
END = 'Best Regards,\n'+ agent + '\nMicrosoft Volume Licensing'

EMAILS = {
# First Notification - Reminder
'r1':'Reminder 1', 

# Last Notification - Closing email
'r2':'Reminder 2', 

# MOF - Incorrect Price
'price': OP + ''' 
Please note whilst processing your request we encountered an issue which requires your attention. The Unit Price for the SKUs mentioned bellow are currently not matching our system:

## SKU ##

We kindly ask you to update and resubmit the MOF amending the issue.

Once the MOF is updated and resubmitted we will gladly proceed with your reqeuest, until then this case will remain on Customer Hold.

''' + END 
}


# Logic #

if len(sys.argv) < 2:

    print('''
r1 -- First Reminder [24h after escalating the issue to Partner]
r2 -- Last notification/Closing e-mail
price -- Incorrect price used in MOF


'''
+agent+ ''', please use the script correctly

Correct Usage:
    ./email_assistant.py [shortcut]
''')
    sys.exit()
else:
    shortcut = sys.argv[1]

pyperclip.copy(EMAILS[shortcut])
print('Template for \''+ shortcut +'\' saved to clipboard.')