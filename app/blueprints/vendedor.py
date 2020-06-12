import re

from flask import Blueprint, json, request

from app.classes.vendedor import Vendedor
from app.helpers.responses import responseError, responseSuccess
from app.models.vendedor import VendedorModel

vendedor_blueprint = Blueprint('vendedor_blueprint', __name__)

@vendedor_blueprint.route(rule='/create', methods=['POST'])
def create():
    data = json.loads(request.data)
    cpf = re.sub('[^0-9]', '', data['cpf'])
    VendedorModel.find_by_email(data['email'])
    if VendedorModel.find_by_email(data['email']):
        return responseError(f"Já existe um vendedor com email '{data['email']}'")
    if VendedorModel.find_by_cpf(cpf):
        return responseError(f"Já existe um vendedor com o cpf '{cpf}'")
    
    vendedor = Vendedor()
    result = vendedor.insert(data=data)
    return responseSuccess("body", result)

@vendedor_blueprint.route(rule='/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    vendedor = Vendedor()
    sts, result = vendedor.login(data['email'],data['password'])
    if sts: return responseSuccess("body", result)
    else: return responseError(result)
