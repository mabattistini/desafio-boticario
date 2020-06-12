from werkzeug.security import safe_str_cmp

from app.helpers.criptografia import Cryptography
from app.models.revendedor import RevendedorModel


class Revendedor():

    def insert(self, data):
        revendedor = RevendedorModel(**data)
        revendedor.save_to_db()
        return revendedor.json()

    def login(self, email, password):
        revendedor = RevendedorModel.find_by_email(email)
        if revendedor and safe_str_cmp(revendedor.password, Cryptography(None).sha224(password.encode())):
            return True, revendedor.json()
        else:
            return False, "Email ou senha não conferem"
