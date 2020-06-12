from app.models import db
from app.models.venda import VendaModel


class Venda():

    def insert(self, data):
        venda = VendaModel(**data)
        venda.save_to_db()
        return venda.json()

    def update(self, data):
        venda = VendaModel.find_by_id(data['id'])
        if 'codigo' in data: venda.codigo = data['codigo']
        if 'valor' in data: venda.valor = data['valor']
        if 'dataVenda' in data: venda.dataVenda = data['dataVenda']
        if 'revendedor' in data: venda.revendedor_id = data['revendedor']
        if 'status' in data: venda.status = data['status']

        db.session.commit()

        return {"id": venda.id,
                "codigo": venda.codigo,
                "valor": venda.valor,
                "data_venda": venda.dataVenda,
                "revendedor_id": venda.revendedor_id,
                "revendedor": venda.revendedor.nome,
                "status": venda.status}
