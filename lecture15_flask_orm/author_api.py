import http

from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from database import db
from models.author import Author
from models.book import Book
from serializers.author import AuthorSchema

author_router = Blueprint('author', __name__, url_prefix='/author')


@author_router.route('')
def get():
    author_schema = AuthorSchema()

    authors = Author.query.order_by(Author.author_email)
    authors_json = author_schema.dump(authors, many=True)
    return jsonify(authors_json)


@author_router.route('/<int:id_>')
def retrieve(id_):
    author_schema = AuthorSchema()
    author = Author.query.filter_by(id=id_).first()
    author_json = author_schema.dump(author)
    return jsonify(author_json)


@author_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)

    author_schema = AuthorSchema()
    try:
        author_data = author_schema.load(data)
        new_author = Author(author_name=author_data['author_name'], author_email=author_data['author_email'])
        db.session.add(new_author)
        db.session.commit()

        new_author_json = author_schema.dump(new_author)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_author_json


@author_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)

    schema = AuthorSchema()
    try:
        author_data = schema.load(data)
        author = Author.query.filter_by(id=id_).first()
        author.author_name = author_data['author_name']
        author.author_email = author_data['author_email']
        db.session.add(author)
        db.session.commit()

        new_author_json = schema.dump(author)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_author_json


@author_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    Author.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT


@author_router.route('/<int:id_>/<int:book_id>', methods=['POST'])
def add_book(id_, book_id):
    author = Author.query.filter_by(id=id_).first()
    if book := Book.query.filter_by(id=book_id).first():
        author.book_id = book.id
        db.session.add(author)
        db.session.commit()
        schema = AuthorSchema()
        new_author_json = schema.dump(author)
        return new_author_json, http.HTTPStatus.OK
    else:
        return {"No group found"}, http.HTTPStatus.BAD_REQUEST
