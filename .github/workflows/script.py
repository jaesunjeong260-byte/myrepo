import requests
import datetime

response = requests.get("https://github.com")
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("result.txt", "a", encoding="utf-8") as f:
    f.write(f"[{now}] {response.text}\n")
print(f"Saved: {response.text}")
