import requests
try:
    res = requests.get("https://google.com", timeout=5)
except:
    print("No connection.")

try:
    res = requests.get("https://www.baidu.com", timeout=5)
except:
    print("No connection.")

print(res.ok)
print(res.content)
