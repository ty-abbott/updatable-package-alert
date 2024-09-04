import os
import smtplib
from email.message import EmailMessage
#import ssl
os.system('apt update')
os.system('apt list --upgradable > upgradable.txt')
if os.path.getsize('upgradable.txt') != 0:
    from_address = os.environ.get('bot_email')
    to_address = os.environ.get('to_email')
    smtp_server = 'smtp.gmail.com'
    port = 465
    auth_token = os.environ.get('bot_password')
    subject = 'upgradable packages'
    with open ('upgradable.txt', 'r') as file:
        body = file.read()
    
    em = EmailMessage()
    em['From'] = from_address
    em['To'] = to_address
    em['Subject'] = subject
    em.set_content(body)
     
   # context = ssl.create_default_context
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(from_address, auth_token)
        server.sendmail(from_address, to_address, em.as_string())

