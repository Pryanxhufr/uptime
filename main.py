import time
import requests

url = "https://dmbot-lhr9.onrender.com"

while True:
    try:
        requests.get(url)
    except:
        pass  # Ignore all errors
    time.sleep(5)
