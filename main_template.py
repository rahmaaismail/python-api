from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class UppercaseText(Resource):
    def get(self):
        """
        This method responds to the GET request for this endpoint and returns the data in uppercase.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be converted to uppercase
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: string
                                description: The text in uppercase
        """
        text = request.args.get('text')

        return {"text": text.upper()}, 200

class ProcessText(Resource):
    def get(self):
        """
        This method processes text with optional duplication and capitalization.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to process
            - name: duplication_factor
              in: query
              type: integer
              required: false
              description: Number of times to repeat the text
            - name: capitalization
              in: query
              type: string
              required: false
              enum: [UPPER, LOWER, None]
              description: The capitalization style
        responses:
            200:
                description: A successful GET request
                schema:
                    type: object
                    properties:
                        text:
                            type: string
                            description: The processed text
            400:
                description: Invalid input
        """

        text = request.args.get('text')
        duplication_factor = request.args.get('duplication_factor', default=1)
        capitalization = request.args.get('capitalization', default=None)

        # Validate required field
        if not text:
            return {"message": "The 'text' parameter is required."}, 400

        # Validate and convert duplication_factor
        try:
            duplication_factor = int(duplication_factor)
            if duplication_factor < 1:
                return {"message": "duplication_factor must be >= 1"}, 400
        except ValueError:
            return {"message": "duplication_factor must be an integer"}, 400

        # Apply capitalization
        if capitalization:
            capitalization = capitalization.upper()
            if capitalization == "UPPER":
                text = text.upper()
            elif capitalization == "LOWER":
                text = text.lower()
            elif capitalization == "NONE":
                pass
            else:
                return {"message": "capitalization must be UPPER, LOWER, or NONE"}, 400

        # Apply duplication
        result = text * duplication_factor

        return {"text": result}, 200

api.add_resource(ProcessText, "/process")
api.add_resource(UppercaseText, "/uppercase")

if __name__ == "__main__":
    app.run(debug=True)