import os
from pyairtable import Api

class BookReview:
    def __init__(self):
        self.api = Api(os.environ['AIRTABLE'])
        self.table = self.api.table('appw6GK8gy1eD3GRv', 'tblJKS4QesCeH4B9n')

    def get_book_ratings(self, sort=None, max_records=10):

        params = {"max_records": max_records}

        if sort == "ASC":
            params["sort"] = ["Rating"]
        elif sort == "DESC":
            params["sort"] = ["-Rating"]

        return self.table.all(**params)

    def add_book_rating(self, book_title, book_rating, notes = None):
        fields = {'Book': book_title, 'Rating': book_rating, 'Notes': notes}
        self.table.create(fields=fields)


if __name__ == '__main__':
    br = BookReview()
    get_book_ratings = br.get_book_ratings(sort="DESC", max_records = 1)
    print(get_book_ratings)
