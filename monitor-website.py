import time

import linode_api4
import requests
import smtplib
import os
import paramiko
import schedule

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS", "EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD", "EMAIL_PASSWORD")
LINODE_TOKEN = os.environ.get("LINODE_TOKEN", "LINODE_TOKEN")

response = requests.get('https://www.google.com')


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


def restart_container():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("IP_ADDRESS", username="USERNAME", key_filename="PATH_TO_KEY")
    stdin, stdout, stderr = ssh.exec_command("docker start {ID}")
    print(stdout.readlines())
    ssh.close()
    print("Application restarted!")


def restart_server_and_container():
    print("Rebooting Linode instance...")
    client = linode_api4.LinodeClient(
        LINODE_TOKEN
    )
    nginx_server = client.load(linode_api4.Instance, 26425590)
    nginx_server.reboot()
    while True:
        if nginx_server.status == "running":
            time.sleep(5)
            restart_container()
            break


def monitor_application():
    try:
        if response.status_code == 200:
            print('Application is running successfully!')
        else:
            print('Application is down. Fix it!')
            send_notification(
                'Subject: Application is down!\n\nApplication is down. Fix it!'
            )
            restart_container()

    except Exception as e:
        print(e)
        send_notification(
            'Subject: Application is accessible at all!\n\nApplication is down. Fix it!'
        )

        restart_server_and_container()


schedule.every(5).minutes.do(monitor_application)

while True:
    schedule.run_pending()
