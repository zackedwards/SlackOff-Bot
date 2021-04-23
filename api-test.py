import requests
link = 'https://sheetdb.io/api/v1/7a4208wp8ee6d'
r = requests.get(link).json()
for i in r:
    print(i['type'])