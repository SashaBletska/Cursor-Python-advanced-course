from marshmallow import Schema, fields
from marshmallow.validate import Length


class AuthorSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    author_name = fields.String(required=True, validate=Length(min=5, max=355))
    author_email = fields.Email(required=True, validate=Length(min=10, max=355))
    book_id = fields.Integer(required=False)
