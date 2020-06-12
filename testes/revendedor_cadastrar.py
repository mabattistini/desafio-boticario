import requests
from flask import json

from config import urls
from testes.auth import Auth

token = Auth().authenticate(username="usrboticario", password="pwdboticario")
if token:
    print(f"solicitando a alteração da venda")
    url = urls['cadastrar_revendedor']
    headers = {'Authorization': f'JWT {token}'}
    payload = {"email":"revendedor100@provedor.com.br","nome": "revendedor teste","cpf": "153.509.460-56","password": "teste"}
    req = requests.post(url, headers=headers, data=json.dumps(payload))
    print(req.text)
