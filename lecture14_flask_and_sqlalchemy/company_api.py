import http

from flask import Blueprint, Response, request, jsonify
from marshmallow import ValidationError

from database import db
from models.company import Company
from serializers.company import CompanySchema

company_router = Blueprint('company', __name__, url_prefix='/company')


@company_router.route('')
def get():
    company_schema = CompanySchema()

    companies = Company.query.order_by(Company.company_email)
    companies_json = company_schema.dump(companies, many=True)
    return jsonify(companies_json)


@company_router.route('/<int:id_>')
def retrieve(id_):
    company_schema = CompanySchema()
    company = Company.query.filter_by(id=id_).first()
    company_json = company_schema.dump(company)
    return jsonify(company_json)


@company_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)

    company_schema = CompanySchema()
    try:
        company_data = company_schema.load(data)
        new_company = Company(company_name=company_data['company_name'], company_email=company_data['company_email'])
        db.session.add(new_company)
        db.session.commit()

        new_company_json = company_schema.dump(new_company)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_company_json


@company_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)

    schema = CompanySchema()
    try:
        company_data = schema.load(data)
        company = Company.query.filter_by(id=id_).first()
        company.company_name = company_data['company_name']
        company.company_email = company_data['company_email']
        db.session.add(company)
        db.session.commit()

        new_company_json = schema.dump(company)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_company_json


@company_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    Company.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT
