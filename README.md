# 📚 Book Review API

![API Preview](images/swagger_screenshot.png)

A RESTful Book Review API built with Flask, Flask-RESTful, and Flasgger, using Airtable as a lightweight database and deployed on Render.

---

## 🔗 Live API

Swagger Documentation:  
https://ri-book-review-api.onrender.com/apidocs

## 🚀 Overview

This project is a backend API that allows users to:
- Add book reviews
- Retrieve all reviews
- Sort and limit results
- Process text through utility endpoints (uppercase + transformations)

It demonstrates core backend engineering concepts including:
- REST API design
- External database integration (Airtable)
- Environment variable management
- API documentation using Swagger (Flasgger)
- Cloud deployment (Render)
- Basic API testing via Python scripts

---

## 🧰 Tech Stack

- Python 3
- Flask
- Flask-RESTful
- Flasgger (Swagger UI)
- Airtable API
- Gunicorn
- Render

---

## 📦 Project Structure

```
.
├── app.py                   # Main Flask application
├── book_review.py          # Airtable integration layer
├── api_request_test.py     # Manual API testing script
├── requirements.txt        # Dependencies
└── README.md
```

---

## 🔐 Environment Variables

This project requires an Airtable API key.

Set it in your environment:

```
AIRTABLE=your_airtable_api_key
```

---

## 📡 Base URL

```
https://ri-book-review-api.onrender.com
```

---

## 📘 API Endpoints

---

### ➕ Add a Book Review

**POST** `/post_review`

Adds a new book review to Airtable.

#### Request Body:
```json
{
  "book": "The Alchemist",
  "rating": 9,
  "notes": "A meaningful philosophical journey"
}
```

#### Required Fields:
- book (string)
- rating (integer)

#### Response:
```json
{
  "message": "Book review added successfully"
}
```

---

### 📚 Get All Reviews

**GET** `/all_reviews`

Returns all book reviews stored in Airtable.

#### Query Parameters:
- sort: ASC | DESC (optional)
- max_records: integer (optional, default 10)

#### Example:
```
/all_reviews?sort=DESC&max_records=5
```

---

### 🔠 Uppercase Text

**GET** `/uppercase`

#### Query:
- text (required)

#### Example:
```
/uppercase?text=hello
```

#### Response:
```json
{
  "text": "HELLO"
}
```

---

### 🔁 Process Text

**GET** `/process`

#### Query Parameters:
- text (required)
- duplication_factor (optional)
- capitalization (UPPER | LOWER | NONE)

---

## 🧪 API Testing Script (IMPORTANT)

This project includes a manual API testing file:

### 📄 `api_request_test.py`

This script is used to test deployed endpoints directly using Python.

#### Example Usage:

```python
import requests

BASE_URL = "https://ri-book-review-api.onrender.com"

url = f"{BASE_URL}/all_reviews"

params = {
    "max_records": 3,
    "sort": "DESC"
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())
```

#### Why this exists:
- Quick sanity check for deployed API
- Helps debug Airtable connection issues
- Verifies GET/POST requests without Swagger UI
- Useful for development + deployment testing

---

## 🗄️ Database

Uses Airtable to store:
- Book title
- Rating
- Notes
- Timestamp

---

## 📖 Swagger Documentation

Interactive API docs available at:

```
https://ri-book-review-api.onrender.com/apidocs
```

---

## 🚀 Deployment

Deployed on Render with:
- Gunicorn WSGI server
- Environment variables configured in dashboard
- Auto deployment from GitHub

---

## ⚠️ Common Issues

- Missing AIRTABLE key → API fails
- Invalid JSON body → POST request fails
- Render cold start → first request may be slow
- Ensure correct endpoint URLs when testing

---

## 🙌 Credits

Inspired by Keith Galli’s Flask API tutorial series.

---

## 📌 Future Improvements

- Add authentication (API keys / JWT)
- Add update/delete endpoints
- Add pagination for reviews
- Switch Airtable → PostgreSQL
- Add automated tests (pytest + CI pipeline)
- Improve validation + error handling
