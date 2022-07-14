import http

from flask import Blueprint, Response, request

from db.db_book import BookDB

book_router = Blueprint('book', __name__, url_prefix='/book')
db = BookDB()


@book_router.route('')
def get():
    books = db.get_all()
    # return jsonify(users)
    # return make_response(jsonify(users), http.HTTPStatus.OK, {"custom": "header"})
    return Response(str(books))


@book_router.route('/<int:book_id>')
def retrieve(book_id):
    book = db.retrieve_by_id(book_id)
    return book


@book_router.route('', methods=['POST'])
def create():
    name = request.json.get("name")
    author = request.json.get("author")
    pages = request.json.get("pages")
    new_book = db.add(name, author, pages)
    if not new_book:
        return "Book already exists", http.HTTPStatus.BAD_REQUEST
    else:
        return new_book, http.HTTPStatus.CREATED


@book_router.route('/<int:book_id>', methods=['PUT'])
def update(book_id):
    name = request.json.get("name")
    author = request.json.get("author")
    pages = request.json.get("pages")
    update_book = db.update_by_id(book_id, name, author, pages)
    if not update_book:
        return "Book with this id doesn't exist", http.HTTPStatus.BAD_REQUEST
    else:
        return update_book, http.HTTPStatus.CREATED


@book_router.route('/<int:book_id>', methods=['DELETE'])
def delete(book_id):
    db.delete_by_id(book_id)
    return {}, http.HTTPStatus.NO_CONTENT
