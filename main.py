import time
import requests

url = "https://dmbot-ms86.onrender.com"

while True:
    try:
        response = requests.get(url)
        print(response)
    except:
        pass  # Ignore all errors
    time.sleep(10)
