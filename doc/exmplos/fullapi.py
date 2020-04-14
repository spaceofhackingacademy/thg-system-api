import requests
API_URL = 'http://127.0.0.1:5000/'
login = requests.get('http://127.0.0.1:5000/login', auth=('user', 'password'))
jsonlogin = login.json()
for token, key in jsonlogin.items():
    pass
print("voce tem que usar o token desse jeito aqui\nsua rota?token={}".format(key))


headers = {'UserAPI-Key': key}

response = requests.get(
    '{}/files?token={}'.format(API_URL, key), headers=headers)

print(response.json())

dsa = "get_token.py"
with open("get_token.py") as fp:
    content = fp.read()

response = requests.post(
    '{}/files/{}?token={}'.format(API_URL, dsa, key), headers=headers, data=content
)

print(response.status_code)


response = requests.get(
    '{}/files/dsa?token={}'.format(API_URL, key), headers=headers
)

print(response.text)
