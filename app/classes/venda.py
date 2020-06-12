from app.models import db
from app.models.venda import VendaModel


class Venda():

    def insert(self, data):
        venda = VendaModel(**data)
        venda.save_to_db()
        return venda.json()

    def update(self, data):
        venda = VendaModel.find_by_id(data['id'])
        if data['codigo'] is not None: venda.codigo = data['codigo']
        if data['valor'] is not None:venda.valor = data['valor']
        if data['dataVenda'] is not None:venda.dataVenda = data['dataVenda']
        if data['revendedor'] is not None:venda.revendedor_id = data['revendedor']
        if data['status'] is not None:venda.status = data['status']
        db.session.commit()
        return {"id": venda.id,
                "codigo": venda.codigo,
                "valor": venda.valor,
                "data_venda": venda.dataVenda,
                "revendedor_id": venda.revendedor_id,
                "revendedor": venda.revendedor.nome,
                "status": venda.status}
