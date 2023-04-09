import requests
import json


response = requests.post(url = "https://indel.becloud.by/", headers ={"Content-Type" : "application/json"} )
print(response.headers)
print(response.status_code)
print(response.json())