import requests

from config import urls
from testes.auth import Auth


token = Auth().authenticate(username="usrboticario", password="pwdboticario")
if token:
    print("solicitando o cashback acumulado")
    url = urls['cashback_acumulado']
    headers = {'Authorization': f'JWT {token}'}
    req = requests.get(url, headers=headers)
    print(req.text)

