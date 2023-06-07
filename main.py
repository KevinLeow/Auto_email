# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'crusad98@gmail.com'
email_password = ''
email_receiver = ''

subject = 'Auto_Mail'
body = 'Test Test test'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
