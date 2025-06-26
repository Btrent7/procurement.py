import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError 

# GMAIL creditials
SCOPES = [ "https://www.googleapis.com/auth/gmail.send"]
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=0)
service = build('gmail', 'v1', credentials=creds)

# Message Variables
message = MIMEText("Hello! Test.")
message['to'] = 'email@reliablesprinkler.com'
message['subject'] = 'Title'
create_message =  {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

# Send Email
try:
    message = (service.users().messages().send(userId="me", body=create_message).execute())
    print(F'sent message!')
except HTTPError as error:
    print(F'An error occured {error}')
    message = None

# Confirm Finish
print("Process Complete!")
