import smtplib
from email.mime.text import MIMEText

# Function to send email alerts
def send_email_alert(subject, body):
    sender_email = 'your_email@example.com'
    receiver_email = 'recipient_email@example.com'
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email

    # Connect to SMTP server and send email
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(sender_email, 'your_password')
        server.sendmail(sender_email, receiver_email, message.as_string())

# Example usage of sending email alert
try:
    # Data processing code
    logging.info('Data processing successful.')
except Exception as e:
    logging.error(f'Error processing data: {e}')
    send_email_alert('Data Processing Error', f'An error occurred while processing data: {e}')
