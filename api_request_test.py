import requests

# base_url = 'https://ri-book-review-api.onrender.com/process_text'
base_url = 'http://127.0.0.1:5000/reviews'

body = {'book': 'Matilda', 'rating': 9}

response = requests.post(base_url, json=body)

print(response.json())
