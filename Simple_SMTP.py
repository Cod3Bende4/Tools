# I wanted to send mails/alerts using python code and I made this script to do so. Feel free to use it.
''' 
  Note: I have created 'email_pass.txt' (to get my username and password so that i don't have to store it in my code keeping format as email:pass and 
  'recipients.txt' for storing multiple emails each in new line
'''

# Common Problems
'''If you are getting username and password not accepted, Check follwing: 

* Have you allowed for less secure apps?  Please do so, and see if that helps.  https://myaccount.google.com/lesssecureapps
* You may also need to clear a "captcha".  (You usually have only a 10 minute window after clearing the captcha, depending on what you are doing) https://accounts.google.com/DisplayUnlockCaptcha
* If using 2 Step Verification in Gmail, you may need an application  password. https://support.google.com/accounts/answer/185833?hl=en
* Use "recent" mode if you are using POP3 on multiple devices.  https://support.google.com/mail/answer/7104828?hl=en 
'''

#Import Libraries
from smtplib import SMTP
import datetime, os

# Get,Set all variables

Mail_Server = 'smtp.gmail.com' #You can use other SMTP Servers as well
list_of_recipients = []
with open('email_pass.txt','r') as cred:
    from_addr,password = cred.readline().split(':')
    cred.close()
with open('recipients.txt','r') as temp:
    list_of_recipients = temp.read().split('\n')
    temp.close()

os.system('cls')
print(5*'-'+'Started SMTP Server'+5*'-'+'\n')
print (f'Using {from_addr} for sending mails....')

# Setting up mail template

subj = "Test Msg"
date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )

smtp = SMTP(Mail_Server,25)
smtp.set_debuglevel(0)
smtp.connect(Mail_Server, 587)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
smtp.login(from_addr,password)

for recipient in list_of_recipients:
    # Tried using multiple text formatting in single line, Guess what it works.
    message_text = f'Time and Date: %s\n\nHello,\nThis is a mail from your simple SMTP server.\n\nBye.' %(date)
    msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_addr, recipient, subj, date, message_text )
    print('Sending message to {}'.format(recipient))
    smtp.sendmail(from_addr, recipient, msg)
    print('_*_*_*_Success_*_*_*_')
print(5*'-'+'Closing SMTP Server'+5*'-'+'\n')
smtp.quit()
print(5*'-'+'Closed SMTP Server'+5*'-')
