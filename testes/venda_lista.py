import requests

from config import urls
from testes.auth import Auth


token = Auth().authenticate(username="usrboticario", password="pwdboticario")
if token:
    print("solicitando a relação de vendas cadastradas")
    url = urls['vendas_cadastradas']
    headers = {'Authorization': f'JWT {token}'}
    req = requests.get(url, headers=headers)
    print(req.text)

