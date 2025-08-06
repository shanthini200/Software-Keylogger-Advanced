# Software-Keylogger-Advanced
Software keylogger Sending Logs With email and Anonymously

## Remote Keylogger with Self Deployment

This project is an advanced demonstration of a keylogger's functionality combined with remote deployment. The code logs keystrokes, sends the logs to a remote server, and includes a mechanism for distributing the keylogger code via email.

## Features

- Keystroke Logging: Captures and timestamps keystrokes.
- Remote Storage: Sends logged keystrokes to the developer's system or server.
- Email Distribution: Includes functionality to send the keylogger code to a receiver via email.

## Disclaimer

This project is for educational purposes only. Unauthorized use of such software can lead to legal consequences and ethical violations. Ensure you have explicit consent before deploying or testing this software.

## Intended Use Cases

- Demonstrating phishing awareness in controlled environments.
- Educating on ethical hacking techniques.
- Cybersecurity research in a lab setting.
  
## Requirements

**Python 3.x**
**Libraries:**
- pynput
- smtplib
- email

## Setup Instructions for Ethical Keylogger (Educational Use Only)

## Prerequisites

**Python Installation:** Ensure Python 3.x is installed on your system. You can download it from python.org.
**Required Libraries:** Install the necessary Python libraries by running:
```
pip install pynput
```
## Setting Up the Project

**Clone the Repository:**
```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
**Configure Email Settings:** Open the script file (keylogger.py) and update the following placeholders:

- **email_user:** Your sender email address.
- **email_password:** App password for the sender's email.
- **email_send:** The recipient's temporary email address (e.g., Maildrop).
  
**Enable App Passwords (if applicable):**

- For Outlook users, refer to Outlook App Password Setup (https://support.microsoft.com/).
- For Gmail users, enable "App Passwords" in your Google account settings under Security.
- Verify Log File Configuration: The keylogger logs keystrokes to a file named log.txt in the same directory. Ensure you have write permissions for the directory.

## Running the Keylogger

**Start the Script:** Execute the script in your terminal:
```
python keylogger.py
```
**The keylogger will:**

Log keystrokes to log.txt every 60 seconds.
Send logs via email every 5 minutes.

**Stop the Script:** Use Ctrl + C in the terminal to terminate the script.

## How It Works

- **Keylogger:** Logs keystrokes locally and sends them to the developer's system.
- **Email Distribution:** Attaches the keylogger code to an email and sends it to the receiver ( manual installation ).
- **send_keylog_email.py:** Sends the saved log.txt to other device via temporary email.
- **keylogger_with_email.py:** Sends the keylogger file(current file) to other device - can be sent with temporary mail providers.
- **warning!** The file cannot be send via authorised mail providers as it may detect virus, can cause damage .

## Ethical Practices
This project is designed to educate about the risks of phishing and malware. It should only be used:

- In controlled environments.
- With explicit permission from all participants.
- As part of ethical hacking or cybersecurity awareness campaigns.
- Avoid committing email credentials or sensitive data to the repository.
- Any misuse is strictly discouraged.
- Misuse of this software is strictly prohibited.

## License
This Project is Licensed Under Apache.2.0.
