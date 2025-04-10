import time
import requests

url = "https://apis-3kns.onrender.com/?product_id=3"

while True:
    try:
        response = requests.get(url)
        print(response)
    except:
        pass  # Ignore all errors
    time.sleep(40)
