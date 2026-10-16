import time
import requests

url = "http://natas17.natas.labs.overthewire.org/"
response_times = []

print("[*] Calculating baseline response time...")

for i in range(5):
    response = requests.get(url)
    duration = response.elapsed.total_seconds()
    response_times.append(duration)
    print(f"Request {i+1}: {duration:.3f} seconds")
    # small pause to avoid hitting rate limits
    time.sleep(0.5)

average_time = sum(response_times) / len(response_times)
print(f"\n[+] Average Baseline Response Time: {average_time:.3f} seconds")