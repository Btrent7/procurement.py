# import smtplib
# from email.mime.text import MIMEText

# subject = "Part Number"
# body = "Hello! Test."
# sender = "email@gmail.com"
# recipients = "email@reliablesprinkler.com"
# password = "pass_word1"

# def send_email (subject, body, sender, recipients, password):
#     msg = MIMEText(body)
#     msg = ['Subject'] = subject
#     msg = ['From'] = sender
#     msg = ['To'] = recipients
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
#         smtp_server.login(sender, password)
#         smtp_server.sendmail(sender, recipients, msg.as_string())
#     print("Message Sent!") 

import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError 
SCOPES = [ "https://www.googleapis.com/auth/gmail.send"]
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=0)
service = build('gmail', 'v1', credentials=creds)
message = MIMEText("Hello! Test.")
message['to'] = 'email@reliablesprinkler.com'
message['subject'] = 'Title'
create_message =  {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
try:
    message = (service.users().messages().send(userId="me", body=create_message).execute())
    print(F'sent message!')
except HTTPError as error:
    print(F'An error occured {error}')
    message = None
