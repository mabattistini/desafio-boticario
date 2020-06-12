import re

from flask import Blueprint, json, request

from app.classes.revendedor import Revendedor
from app.helpers.responses import responseError, responseSuccess
from app.models.revendedor import RevendedorModel

revendedor_blueprint = Blueprint('revendedor_blueprint', __name__)

@revendedor_blueprint.route(rule='/create', methods=['POST'])
def create():
    data = json.loads(request.data)
    cpf = re.sub('[^0-9]', '', data['cpf'])
    RevendedorModel.find_by_email(data['email'])
    if RevendedorModel.find_by_email(data['email']):
        return responseError(f"Já existe um revendedor com email '{data['email']}'")
    if RevendedorModel.find_by_cpf(cpf):
        return responseError(f"Já existe um revendedor com o cpf '{cpf}'")
    
    revendedor = Revendedor()
    result = revendedor.insert(data=data)
    return responseSuccess("body", result)

@revendedor_blueprint.route(rule='/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    revendedor = Revendedor()
    sts, result = revendedor.login(data['email'],data['password'])
    if sts: return responseSuccess("body", result)
    else: return responseError(result)
