import http

from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from database import db
from models.book import Book
from serializers.book import BookSchema

book_router = Blueprint('book', __name__, url_prefix='/book')


@book_router.route('')
def get():
    book_schema = BookSchema()

    books = Book.query.order_by(Book.book_title)
    books_json = book_schema.dump(books, many=True)
    return jsonify(books_json)


@book_router.route('/<int:id_>')
def retrieve(id_):
    book_schema = BookSchema()
    book = Book.query.filter_by(id=id_).first()
    book_json = book_schema.dump(book)
    return jsonify(book_json)


@book_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)

    book_schema = BookSchema()
    try:
        book_data = book_schema.load(data)
        new_book = Book(book_title=book_data['book_title'], book_description=book_data['book_description'])
        db.session.add(new_book)
        db.session.commit()

        new_book_json = book_schema.dump(new_book)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_book_json


@book_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)

    schema = BookSchema()
    try:
        book_data = schema.load(data)
        book = Book.query.filter_by(id=id_).first()
        book.book_name = book_data['book_title']
        book.book_email = book_data['book_description']
        db.session.add(book)
        db.session.commit()

        new_book_json = schema.dump(book)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_book_json


@book_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    Book.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT
