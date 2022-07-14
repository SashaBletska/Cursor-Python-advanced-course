import http

from flask import Blueprint, Response, request

from db.db_user import UserDB

user_router = Blueprint('user', __name__, url_prefix='/user')
db = UserDB()


@user_router.route('')
def get():
    users = db.get_all()
    # return jsonify(users)
    # return make_response(jsonify(users), http.HTTPStatus.OK, {"custom": "header"})
    return Response(str(users))


@user_router.route('/<string:email>')
def retrieve(email):
    user = db.retrieve_by_email(email)
    return user


@user_router.route('', methods=['POST'])
def create():
    name = request.json.get("name")
    email = request.json.get("email")
    password = request.json.get("password")
    new_user = db.add(name, email, password)
    if not new_user:
        return "User already exists", http.HTTPStatus.BAD_REQUEST
    else:
        return new_user, http.HTTPStatus.CREATED


@user_router.route('/<string:email>', methods=['PUT'])
def update(email):
    name = request.json.get("name")
    password = request.json.get("password")
    update_user = db.update_by_email(email, name, password)
    if not update_user:
        return "User with this email doesn't exist", http.HTTPStatus.BAD_REQUEST
    else:
        return update_user, http.HTTPStatus.CREATED


@user_router.route('/<string:email>', methods=['DELETE'])
def delete(email):
    db.delete_by_email(email)
    return {}, http.HTTPStatus.NO_CONTENT
