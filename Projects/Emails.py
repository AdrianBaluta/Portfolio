import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Adrian Baluta'
email['to'] = '*********@yahoo.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.mail.yahoo.com', port=465) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('*******@yahoo.com', '********')
    smtp.send_message(email)
    print('all good!')