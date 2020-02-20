#! /usr/bin/python3
# email_assistant.py - Script containing all important email templates. It will save the template to the User's clipboard.


# Imports #
import sys, pyperclip

# Variables #
OP = '''
Hello Team,

Thank you for placing your request with us.
'''
END = '''
Best Regards,
AGENT
Microsoft Volume Licensing
'''
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
    print('Correct Usage:\n ./email_assistant.py [shortcut]')
    sys.exit()
else:
    shortcut = sys.argv[1]

pyperclip.copy(EMAILS[shortcut])
print('Template for \''+ shortcut +'\' saved to clipboard.')