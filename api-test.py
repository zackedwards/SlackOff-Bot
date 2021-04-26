import requests
import random
link = 'https://sheetdb.io/api/v1/7a4208wp8ee6d'
r = requests.get(link).json()
number = random.randint(0,len(r)-10)
new_link=link+'?limit=10&offset='+str(number)
print(requests.get(new_link).json())