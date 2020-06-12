import requests
from flask import json

from config import urls
from testes.auth import Auth

token = Auth().authenticate(username="usrboticario", password="pwdboticario")
if token:
    print(f"solicitando a alteração da venda")
    url = urls['alterar_venda']
    headers = {'Authorization': f'JWT {token}'}
    payload = {"id": 3, "codigo": "produto209", "valor": 700.67, "dataVenda": "02/01/2020",
               "cpf_revendedor": "153.509.460-56" }
    req = requests.post(url, headers=headers, data=json.dumps(payload))
    print(req.text)
