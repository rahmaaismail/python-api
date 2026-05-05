import requests

base_url = 'http://127.0.0.1:5000/uppercase'

params = {'text': 'hello world'}

response = requests.get(base_url, params = params)

print(response)