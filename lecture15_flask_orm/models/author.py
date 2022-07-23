from database import db


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_name = db.Column(db.String(300), nullable=False)
    author_email = db.Column(db.String(300), nullable=False, unique=True)
    book_id = db.Column(db.String(300), db.ForeignKey("books.id"))

