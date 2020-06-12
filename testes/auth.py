import requests
from flask import json
from config import urls


class Auth:
    def __init__(self):
        self.url = urls['auth']

    def authenticate(self, username, password):
        headers = {'Content-Type': 'application/json'}
        body = '{"username": "%(username)s","password": "%(password)s"}' % {'username': username, 'password': password}
        print("Autenticando e recebendo o token de acesso")
        req = requests.post(self.url, headers=headers, data=body)
        if req.status_code == 200:
            return json.loads(req.text)['access_token']
        else:
            return False



