from database import db


class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.String(300), nullable=False)
    company_email = db.Column(db.String(300), nullable=False, unique=True)

