from flask import Flask, request
from flask_restful import Api, Resource
from flasgger import Swagger

import book_review

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

br = book_review.BookReview()

# POST REVIEW
class PostReview(Resource):
    def post(self):
        """
        Add a new book review.
        ---
        tags:
          - Book Reviews
        parameters:
          - in: body
            name: body
            required: true
            schema:
              type: object
              required:
                - book
                - rating
              properties:
                book:
                  type: string
                rating:
                  type: integer
                notes:
                  type: string
        responses:
          201:
            description: Review added
          400:
            description: Bad request
        """

        data = request.get_json()

        if not data:
            return {"error": "JSON body required"}, 400

        book = data.get("book")
        rating = data.get("rating")
        notes = data.get("notes", "")

        if book is None or rating is None:
            return {"error": "'book' and 'rating' are required"}, 400

        br.add_book_rating(book, rating, notes)

        return {"message": "Book review added successfully"}, 201

# GET ALL REVIEWS
class AllReviews(Resource):
    def get(self):
        """
        Retrieve all book reviews.
        ---
        tags:
          - Book Reviews
        parameters:
          - name: sort
            in: query
            type: string
            required: false
            enum: [ASC, DESC]
          - name: max_records
            in: query
            type: integer
            required: false
        responses:
          200:
            description: Success
        """

        sort = request.args.get("sort")
        max_records = request.args.get("max_records", default=10)

        try:
            max_records = int(max_records)
        except ValueError:
            return {"error": "max_records must be an integer"}, 400

        if sort and sort not in ["ASC", "DESC"]:
            return {"error": "sort must be ASC or DESC"}, 400

        if sort == "ASC":
            data = br.get_book_ratings(sort="ASC", max_records=max_records)
        elif sort == "DESC":
            data = br.get_book_ratings(sort="DESC", max_records=max_records)
        else:
            data = br.get_book_ratings(max_records=max_records)

        return data, 200

# UPPERCASE TEXT
class UppercaseText(Resource):
    def get(self):
        """
        Convert text to uppercase.
        ---
        tags:
          - Text Processing
        parameters:
          - name: text
            in: query
            type: string
            required: true
        responses:
          200:
            description: Success
        """

        text = request.args.get("text")

        if not text:
            return {"error": "text is required"}, 400

        return {"text": text.upper()}, 200

# PROCESS TEXT
class ProcessText(Resource):
    def get(self):
        """
        Process text.
        ---
        tags:
          - Text Processing
        parameters:
          - name: text
            in: query
            type: string
            required: true
          - name: duplication_factor
            in: query
            type: integer
            required: false
          - name: capitalization
            in: query
            type: string
            enum: [UPPER, LOWER, NONE]
        responses:
          200:
            description: Success
        """

        text = request.args.get("text")
        duplication_factor = request.args.get("duplication_factor", default=1)
        capitalization = request.args.get("capitalization")

        if not text:
            return {"error": "text is required"}, 400

        try:
            duplication_factor = int(duplication_factor)
        except ValueError:
            return {"error": "duplication_factor must be an integer"}, 400

        if capitalization:
            capitalization = capitalization.upper()
            if capitalization == "UPPER":
                text = text.upper()
            elif capitalization == "LOWER":
                text = text.lower()
            elif capitalization != "NONE":
                return {"error": "capitalization must be UPPER, LOWER, or NONE"}, 400

        return {"text": text * duplication_factor}, 200

# ROUTES
api.add_resource(PostReview, "/review")
api.add_resource(AllReviews, "/all_reviews")
api.add_resource(ProcessText, "/process")
api.add_resource(UppercaseText, "/uppercase")


if __name__ == "__main__":
    app.run(debug=True)