import re
from datetime import datetime

from flask import Blueprint, json, request
from flask_jwt import jwt_required

from app.classes.apiboticario import ApiBoticario
from app.classes.venda import Venda
from app.helpers.responses import responseSuccess, responseError
from app.models.venda import VendaModel
from app.models.vendedor import VendedorModel

venda_blueprint = Blueprint('venda_blueprint', __name__)

@venda_blueprint.route(rule='/create', methods=['POST'])
@jwt_required()
def create():
    data = json.loads(request.data)

    cpf = re.sub('[^0-9]', '', data['cpf_vendedor'])
    vendedor = VendedorModel.find_by_cpf(cpf)
    if not vendedor:
        return responseError(f"Vendedor com cpf {data['cpf_vendedor']} não cadastrado")

    data['status'] = "Em validação" if vendedor.cpf != "15350946056" else "Aprovado"

    try:
        data['dataVenda'] = datetime.strptime(data['dataVenda'], '%d/%m/%Y')
    except:
        return responseError(f"A data {data['dataVenda']} é inválida")

    data['vendedor'] = vendedor.id
    del data['cpf_vendedor']

    venda = Venda()

    result = venda.insert(data)
    return responseSuccess('body', result)

@venda_blueprint.route(rule='/edit', methods=['POST'])
@jwt_required()
def update():
    data = json.loads(request.data)

    venda = VendaModel.find_by_id(data['id'])
    if not venda:
        return responseError(f"message: Não há uma venda cadastrada com este id")
    if venda.status != "Em validação":
        return responseError(f"Venda não pode ser alterada, status = {venda.status}")

    cpf = re.sub('[^0-9]', '', data['cpf_vendedor'])
    vendedor = VendedorModel.find_by_cpf(cpf)
    if not vendedor:
        return responseError(f"message: Vendedor com cpf {data['cpf_vendedor']} não cadastrado")

    data['vendedor'] = vendedor.id
    try:
        data['dataVenda'] = datetime.strptime(data['dataVenda'], '%d/%m/%Y')
    except:
        return responseError(f"A data {data['dataVenda']} é inválida")

    venda = Venda()
    result = venda.update(data)

    responseSuccess('body', result)

@venda_blueprint.route(rule='/delete', methods=['POST'])
@jwt_required()
def delete():
    data = json.loads(request.data)

    venda = VendaModel.find_by_id(data['id'])
    if not venda:
        return responseError(f"message: Não há uma venda cadastrada com este id")
    if venda.status != "Em validação":
        return responseError(f"Venda não pode ser excluida, status = {venda.status}")
    try:
        venda.delete_from_db()
        return responseSuccess(field='body', message="Venda excluida com sucesso")
    except:
        return responseError("Ocorreu um erro ao excluir o registro")


@venda_blueprint.route(rule='/list', methods=['GET'])
@jwt_required()
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
@jwt_required()
def listCashBack():

    totalCashback = 0

    vendas = VendaModel.listAll()
    for venda in vendas:
        cpf = re.sub('[^0-9]', '', venda.vendedor.cpf)
        credit = ApiBoticario.get(cpf=cpf)
        totalCashback += credit

    return responseSuccess('body', {"total_cashback": totalCashback})
