import requests
url = 'http://localhost:8000'
myobj = {'nome': 'Franciele', 'idade': '28'}
x = requests.post(url, json=myobj)
print(x.text)