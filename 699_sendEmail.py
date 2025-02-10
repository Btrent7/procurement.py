import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load data from Excel
data = pd.read_excel('data.xlsx')  # Adjust the path and filename as needed

# Drop rows where any of the important columns are NaN (empty)
data_cleaned = data.dropna(subset=['Item Number', 'Description', 'List Price'])

# Get the most recent row (last row with data)
last_row = data_cleaned.iloc[-1]  # This will give the last non-empty row

# Extract values for email content
item_number = last_row['Item Number']
description = last_row['Description']
list_price = last_row['List Price']

# Email server setup
SMTP_SERVER = 'smtp.gmail.com'  # Example: Gmail SMTP
SMTP_PORT = 587
SENDER_EMAIL = 'your_email@gmail.com'
SENDER_PASSWORD = 'your_password'  # Better to use App Password for security

# Prepare the email message
recipient_email = 'recipient@example.com'  # Adjust the recipient email as needed
subject = f"Item Details: {item_number}"  # Example subject
message_body = f"""
Dear Customer,

Here are the details of the most recent item:

Item Number: {item_number}
Description: {description}
List Price: ${list_price}

Best regards,
Your Company Name
"""

# Create the email
msg = MIMEMultipart()
msg['From'] = SENDER_EMAIL
msg['To'] = recipient_email
msg['Subject'] = subject

# Attach the message body
msg.attach(MIMEText(message_body, 'plain'))

try:
    # Connect to the SMTP server
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Secure the connection
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        
        # Send the email
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, recipient_email, text)
        print(f"Email sent to {recipient_email}")

except Exception as e:
    print(f"Failed to send email to {recipient_email}: {str(e)}")
