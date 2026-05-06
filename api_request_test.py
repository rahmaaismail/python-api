import requests

BASE_URL = "https://ri-book-review-api.onrender.com"

def test_get_reviews():
    url = f"{BASE_URL}/all_reviews"
    params = {
        "max_records": 3,
        "sort": "DESC"
    }

    response = requests.get(url, params=params)

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())


def test_post_review():
    url = f"{BASE_URL}/post_review"
    body = {
        "book": "The Alchemist",
        "rating": 9,
        "notes": "A classic!"
    }

    response = requests.post(url, json=body)

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())


if __name__ == "__main__":
    test_get_reviews()
    # test_post_review()