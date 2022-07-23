from marshmallow import Schema, fields
from marshmallow.validate import Length


class BookSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    book_title = fields.String(required=True, validate=Length(min=5, max=355))
    book_description = fields.String(required=True, validate=Length(min=5, max=500))
