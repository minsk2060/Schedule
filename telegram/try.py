import ssl
import requests
from urllib3 import exceptions
u="https://192.168.250.11/standard/default.php"

try:
    print(requests.get(url=u).status_code)
    print('fgh')
except :
    print("123")
else:
    print("42")
