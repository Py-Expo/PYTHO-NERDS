#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject, body, recipient_email):
    sender_email = 'ashop1355@gmail.com'  # Update with your email address
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # For TLS encryption
    smtp_username = 'janeshkrishna12@gmail.com'  # Update with your email address
    smtp_password = 'ontacndegigcncpw'# Update with your email password

    # Create a MIMEText object to represent the email body
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'html'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable TLS encryption
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        server.quit()

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeatherBug.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Example usage of send_email function
    subject = ' Weather Forecasting'
    body = '<h1>Hello!</h1><p>Your given city is.</p>'
    recipient_email = 'janeshkrishna12@gmail.com'
    send_email(subject, body, recipient_email)

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
