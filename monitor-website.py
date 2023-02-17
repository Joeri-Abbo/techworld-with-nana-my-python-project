import requests
import smtplib
import os

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS", "EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD", "EMAIL_PASSWORD")


def send_notification(msg):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(
            EMAIL_ADDRESS,
            EMAIL_ADDRESS,
            msg
        )


response = requests.get('https://www.google.com')
try:
    if response.status_code == 200:
        print('Application is running successfully!')
    else:
        print('Application is down. Fix it!')
        send_notification(
            'Subject: Application is down!\n\nApplication is down. Fix it!'
        )

except Exception as e:
    print(e)
    send_notification(
        'Subject: Application is accessible at all!\n\nApplication is down. Fix it!'
    )
