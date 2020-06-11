from app.helpers.criptografia import Cryptography
from app.models import db


class VendedorModel(db.Model):
    __tablename__ = 'vendedores'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    nome = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(20), nullable=False,unique=True)
    password = db.Column(db.String(255), nullable=False)
    vendas = db.relationship('VendaModel', lazy='dynamic')

    def __init__(self, email, nome, cpf, password):
        self.email = email
        self.nome = nome
        self.cpf = cpf
        self.password = Cryptography(None).sha224(password.encode())

    def json(self):
        return {
            'id': self.id,
            'email': self.email,
            'nome': self.nome,
            'cpf': self.cpf
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_cpf(cls, cpf):
        return cls.query.filter_by(cpf=cpf).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()