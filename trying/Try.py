import requests
from ssl import SSLCertVerificationError


url="https://192.168.250.11/standard/datapoint/frameset.php?Locale=1049&Object=8388620&Type=2&Name=PV_1_1_Supply_Max&Card=CommandPriorities&Refresh=30"

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8',
'Connection':'keep-alive',
'Cookie': "Precision=2; ShowDescription=1; rememberUser=Olimpik%23edede274df75d64387cbb8aa1e8daaf4%23on; Locale=1033; TimeStampOfLastDisplay=%3CDateTimeStamp%3E%3CDateTime%3E%3CDate%3E2023-06-08Th%3C%2FDate%3E%3CTime%3E14%3A56%3A36.00%3C%2FTime%3E%3C%2FDateTime%3E%3C%2FDateTimeStamp%3E",
'Host':'192.168.250.11',
'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
'Sec-Ch-Ua-Mobile' : '?0',
'Sec-Ch-Ua-Platform' : '"Windows"',
'Sec-Fetch-Dest' : 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests' : '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79',
}
r = requests.get(url, headers = headers)
print(r.status_code, "ок")