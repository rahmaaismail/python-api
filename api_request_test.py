import requests

base_url = 'https://ri-book-review-api.onrender.com/process'

params = {
    'text': 'hello world',
    'duplication_factor': 2,
    'capitalization': 'UPPER'
}

response = requests.get(base_url, params=params)

print(response.status_code)
print(response.json())