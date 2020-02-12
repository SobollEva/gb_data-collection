import requests
import json

auth_url = 'https://api.github.com'
url = 'https://api.github.com/users/sobolleva/repos'
params = {'username': 'sobolleva',
          'password': '***********'}

# github authentication
auth_response = requests.get(auth_url, params=params)

if auth_response.ok:
    auth_data = json.loads(auth_response.text)
    with open('github_auth.json', 'w', encoding='utf-8') as ff:
        json.dump(auth_data, ff)
else:
    print('Sorry, something went wrong')

# getting my github repositories
response = requests.get(url, params=params)
if response.ok:
    data = json.loads(response.text)
    with open('github_repo.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)
else:
    print('Sorry, something went wrong')
