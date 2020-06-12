from app.models import db


class VendaModel(db.Model):
    __tablename__ = 'vendas'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    dataVenda = db.Column(db.Date, nullable=False)
    revendedor_id = db.Column(db.Integer, db.ForeignKey('revendedores.id'), nullable=False)
    status = db.Column(db.String(10), nullable=True)
    revendedor = db.relationship('RevendedorModel')

    def __init__(self, codigo, valor, dataVenda, revendedor, status):
        self.codigo = codigo
        self.valor = valor
        self.dataVenda = dataVenda
        self.revendedor_id = revendedor
        self.status = status

    def json(self):
        return {"id": self.id,
                "codigo": self.codigo,
                "valor": self.valor,
                "data_venda": self.dataVenda,
                "revendedor_id": self.revendedor_id,
                "revendedor": self.revendedor.nome,
                "status": self.status}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def listAll(cls):
        return cls.query.all()


