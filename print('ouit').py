import requests
from pprint import pprint

#username
username='finnveloz'
#url
url=f'https://api.github.com/users/{username}'
user_data=requests.get(url).json
print(user_data)
