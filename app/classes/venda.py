from app.models import db
from app.models.venda import VendaModel


class Venda():

    def insert(self, data):
        venda = VendaModel(**data)
        venda.save_to_db()
        return venda.json()

    def update(self, data):
        venda = VendaModel.find_by_id(data['id'])
        venda.codigo = data['codigo']
        venda.valor = data['valor']
        venda.dataVenda = data['dataVenda']
        venda.vendedor_id = data['vendedor']
        venda.status = data['status']
        db.session.commit()
        return {"id": venda.id,
                "codigo": venda.codigo,
                "valor": venda.valor,
                "data_venda": venda.dataVenda,
                "vendedor_id": venda.vendedor_id,
                "vendedor": venda.vendedor.nome,
                "status": venda.status}
