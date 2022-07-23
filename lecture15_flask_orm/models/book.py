from database import db


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_title = db.Column(db.String(300), nullable=False, unique=True)
    book_description = db.Column(db.String(500), nullable=False)

