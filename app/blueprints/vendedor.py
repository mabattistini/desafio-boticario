from flask import Blueprint, json, request

from app.classes.vendedor import Vendedor
from app.models.vendedor import VendedorModel

vendedor_blueprint = Blueprint('vendedor_blueprint', __name__)

@vendedor_blueprint.route(rule='/create', methods=['POST'])
def create():
    data = json.loads(request.data)
    VendedorModel.find_by_email(data['email'])
    if VendedorModel.find_by_email(data['email']):
        return {'message': "Já existe um vendedor com email '{}'".format(data['email'])}, 400
    if VendedorModel.find_by_cpf(data['cpf']):
        return {'message': "Já existe um vendedor com o cpf '{}'".format(data['cpf'])}, 400
    
    vendedor = Vendedor()
    result = vendedor.insert(data=data)
    return json.dumps(result)

@vendedor_blueprint.route(rule='/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    vendedor = Vendedor()
    sts, rst = vendedor.login(data['email'],data['password'])
    if sts: return rst
    else: return rst, 400
