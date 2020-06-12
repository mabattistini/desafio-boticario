import requests
from flask import json

from config import urls
from testes.auth import Auth

token = Auth().authenticate(username="usrboticario", password="pwdboticario")
if token:
    print(f"solicitando a alteração da venda")
    url = urls['cadastrar_venda']
    headers = {'Authorization': f'JWT {token}'}
    payload = {"codigo": "produto1209", "valor": 15.50, "dataVenda": "03/01/2020",
               "cpf_vendedor": "153.509.460-56"}
    req = requests.post(url, headers=headers, data=json.dumps(payload))
    print(req.text)
