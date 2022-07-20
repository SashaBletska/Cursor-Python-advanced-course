from marshmallow import Schema, fields
from marshmallow.validate import Length


class CompanySchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    company_name = fields.String(required=True, validate=Length(min=5, max=355))
    company_email = fields.Email(required=True, validate=Length(min=10, max=355))
