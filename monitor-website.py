import requests

response = requests.get('https://www.google.com')
if response.status_code == 200:
    print('Application is running successfully!')
else:
    print('Application is down. Fix it!')
