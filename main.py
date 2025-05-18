import time
import requests

url1 = "https://api-fjm4.onrender.com/"
url2 = "https://imgbot-3y9h.onrender.com"

while True:
    try:
        response1 = requests.get(url1)
        print("URL1:", response1)

        #response2 = requests.get(url2)
        #print("URL2:", response2)
    except:
        pass  # Ignore all errors
    time.sleep(40)
