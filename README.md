



# Remote Keylogger with Self Deployment  

This project is an advanced demonstration of a keylogger's functionality combined with remote deployment. The code logs keystrokes, sends the logs to a remote server, and includes a mechanism for distributing the keylogger code via email.  

## Features  

- **Keystroke Logging**: Captures and timestamps keystrokes.  
- **Remote Storage**: Sends logged keystrokes to the developer's system or server.  
- **Email Distribution**: Includes functionality to send the keylogger code to a receiver via email.  

## Disclaimer  

This project is for **educational purposes only**. Unauthorized use of such software can lead to legal consequences and ethical violations. Ensure you have explicit consent before deploying or testing this software.  

### Intended Use Cases  

- Demonstrating phishing awareness in controlled environments.  
- Educating on ethical hacking techniques.  
- Cybersecurity research in a lab setting.  

## Requirements  

- Python 3.x  
- Libraries:  
  - `pynput`  
  - `smtplib`  
  - `email`

## Setup Instructions for Ethical Keylogger (Educational Use Only)

### Prerequisites
1. **Python Installation**: Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/).
2. **Required Libraries**: Install the necessary Python libraries by running:
   ```bash
   pip install pynput
   ```

### Setting Up the Project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Configure Email Settings**:
   Open the script file (`keylogger.py`) and update the following placeholders:
   - `email_user`: Your sender email address.
   - `email_password`: App password for the sender's email.
   - `email_send`: The recipient's temporary email address (e.g., Maildrop).

3. **Enable App Passwords** (if applicable):
   - For **Outlook** users, refer to [Outlook App Password Setup](https://support.microsoft.com/).
   - For **Gmail** users, enable "App Passwords" in your Google account settings under Security.

4. **Verify Log File Configuration**:
   The keylogger logs keystrokes to a file named `log.txt` in the same directory. Ensure you have write permissions for the directory.


### Running the Keylogger
1. **Start the Script**:
   Execute the script in your terminal:
   ```bash
   python keylogger.py
   ```
2. The keylogger will:
   - Log keystrokes to `log.txt` every 60 seconds.
   - Send logs via email every 5 minutes.

3. **Stop the Script**:
   Use `Ctrl + C` in the terminal to terminate the script.

## How It Works  

1. **Keylogger**: Logs keystrokes locally and sends them to the developer's system.  
2. **Email Distribution**: Attaches the keylogger code to an email and sends it to the receiver ( manual installation ).  

## Ethical Practices  

This project is designed to educate about the risks of phishing and malware. It should only be used:  
- In controlled environments.  
- With explicit permission from all participants.  
- As part of ethical hacking or cybersecurity awareness campaigns.
- Avoid committing email credentials or sensitive data to the repository.
-  Any misuse is strictly discouraged.

Misuse of this software is strictly prohibited.  

## License  

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.  


