import requests
from flask import json

from config import urls
from testes.auth import Auth

token = Auth().authenticate(username="usrboticario", password="pwdboticario")
if token:
    print(f"solicitando a alteração da venda")
    url = urls['alterar_venda']
    headers = {'Authorization': f'JWT {token}'}
    payload = {"id": 4, "codigo": "produto209", "valor": 115.67, "dataVenda": "02/01/2020",
               "cpf_revendedor": "153.509.460-56", "status": "Aprovado"}
    req = requests.post(url, headers=headers, data=json.dumps(payload))
    print(req.text)
