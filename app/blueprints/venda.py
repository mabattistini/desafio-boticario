import re
from datetime import datetime

from flask import Blueprint, json, request

from app.classes.apiboticario import ApiBoticario
from app.classes.venda import Venda
from app.classes.vendedor import Vendedor
from app.helpers.responses import responseSuccess
from app.models.venda import VendaModel
from app.models.vendedor import VendedorModel

venda_blueprint = Blueprint('venda_blueprint', __name__)


@venda_blueprint.route(rule='/create', methods=['POST'])
def create():
    data = json.loads(request.data)

    vendedor = VendedorModel.find_by_cpf(data['cpf_vendedor'])
    if not vendedor:
        return {"message": f"Vendedor com cpf {data['cpf_vendedor']} não cadastrado"}, 400

    data['status'] = "Em validação" if vendedor.cpf != "153.509.460-56" else "Aprovado"

    try:
        data['dataVenda'] = datetime.strptime(data['dataVenda'], '%d/%m/%Y')
    except:
        return {"message": f"A data {data['dataVenda']} é inválida"}

    data['vendedor'] = vendedor.id
    del data['cpf_vendedor']

    venda = Venda()

    result = venda.insert(data)
    print(result)

    return result


@venda_blueprint.route(rule='/edit', methods=['POST'])
def update():
    data = json.loads(request.data)

    venda = VendaModel.find_by_id(data['id'])
    if not venda:
        return {"message": f"message: Não há uma venda cadastrada com este id"}, 400
    if venda.status != "Em validação":
        return {"message": f"Venda não pode ser alterada, status = {venda.status}"}, 400

    vendedor = VendedorModel.find_by_cpf(data['cpf_vendedor'])
    if not vendedor:
        return {"message": f"message: Vendedor com cpf {data['cpf_vendedor']} não cadastrado"}, 400

    data['vendedor'] = vendedor.id
    try:
        data['dataVenda'] = datetime.strptime(data['dataVenda'], '%d/%m/%Y')
    except:
        return {"message": f"A data {data['dataVenda']} é inválida"}

    venda = Venda()
    result = venda.update(data)

    return result


@venda_blueprint.route(rule='/delete', methods=['POST'])
def delete():
    data = json.loads(request.data)

    venda = VendaModel.find_by_id(data['id'])
    if not venda:
        return {"message": f"message: Não há uma venda cadastrada com este id"}, 400
    if venda.status != "Em validação":
        return {"message": f"Venda não pode ser excluida, status = {venda.status}"}, 400
    try:
        venda.delete_from_db()
        return {"message": "Venda excluida com sucesso"}
    except:
        return {"message": "Ocorreu um erro ao excluir o registro"}


@venda_blueprint.route(rule='/list', methods=['GET'])
def list():
    result = []
    vendas = VendaModel.listAll()
    for venda in vendas:
        vendaJson = venda.json()
        cpf = re.sub('[^0-9]', '', venda.vendedor.cpf)
        credit = ApiBoticario.get(cpf=cpf)
        try:
            percent = round(((venda.valor / credit) * 100), 2)
        except:
            percent = 0
        vendaJson['cashback'] = credit
        vendaJson['percent_cashback'] = percent
        result.append(vendaJson)

    return responseSuccess('body',result)

@venda_blueprint.route(rule='/cashback', methods=['GET'])
def listCashBack():

    totalCashback = 0

    vendas = VendaModel.listAll()
    for venda in vendas:
        cpf = re.sub('[^0-9]', '', venda.vendedor.cpf)
        credit = ApiBoticario.get(cpf=cpf)
        totalCashback += credit

    #totalCashback = round(totalCashback,2)

    return responseSuccess('body', {"total_cashback": totalCashback})
