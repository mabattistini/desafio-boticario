from werkzeug.security import safe_str_cmp

from app.helpers.criptografia import Cryptography
from app.models.vendedor import VendedorModel


class Vendedor():

    def insert(self, data):
        vendedor = VendedorModel(**data)
        vendedor.save_to_db()
        return vendedor.json()

    def login(self, email, password):
        vendedor = VendedorModel.find_by_email(email)
        if vendedor and safe_str_cmp(vendedor.password, Cryptography(None).sha224(password.encode())):
            return True, vendedor.json()
        else:
            return False, "Email ou senha não conferem"
