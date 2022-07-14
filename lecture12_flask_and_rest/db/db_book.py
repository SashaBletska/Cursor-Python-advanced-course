class BookDB:
    books = [{"book_id": 1, "name": "test", "author": "test test", "pages": 555}]

    def get_all(self):
        return self.books

    def retrieve_by_id(self, book_id):
        for book in self.books:
            if book["book_id"] == book_id:
                return book
        return None

    def add(self, name, author, pages):
        book = {
            "book_id": self.books[-1]['book_id'] + 1,
            "name": name,
            "author": author,
            "pages": pages
        }
        self.books.append(book)
        return book

    def update_by_id(self, book_id, name, author, pages):
        # TODO: refactor
        for book in self.books:
            if book["book_id"] == book_id:
                book["name"] = name
                book["author"] = author
                book["pages"] = pages
                return book
        return None

    def delete_by_id(self, book_id):
        self.books = [book for book in self.books if book["book_id"] != book_id]
