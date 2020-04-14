import requests
API_URL = 'http://127.0.0.1:5000/'
login = requests.get('http://127.0.0.1:5000/login', auth=('user', 'password'))
jsonlogin = login.json()
for token, key in jsonlogin.items():
    response = requests.get('{}/files?token={}'.format(API_URL, key))

print(response.json())
