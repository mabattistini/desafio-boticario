import requests
from flask import json

from config import urls
from testes.auth import Auth

while True:
    try:
       id = int(input("Digite o id da venda "))
       break
    except:
        print("Id inválido")


token = Auth().authenticate(username="usrboticario", password="pwdboticario")
if token:
    print(f"solicitando a exclusão da venda de id = {id}")
    url = urls['excluir_venda']
    headers = {'Authorization': f'JWT {token}'}
    payload = {"id": id}
    req = requests.post(url, headers=headers, data=json.dumps(payload))
    print(req.text)

