import requests
from flask import json


class ApiBoticario:

    @classmethod
    def get(cls, cpf):
        headers = {"token": 'ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm'}
        url = f"https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf={cpf}"
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            response = json.loads(response.text)
        try:
            credit = float(response['body']['credit'])
        except:
            credit = 0
        return credit
