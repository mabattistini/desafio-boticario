
from werkzeug.security import safe_str_cmp
from app.models.user import UserModel
from app.helpers.criptografia import Cryptography


def autenticate(username, password):
    user = UserModel.query.filter_by(username=username).first()
    if user and safe_str_cmp(user.password, Cryptography(None).sha224(password.encode())):
        return user
    else:
        return None


def identify(payload):
    user_id = payload['identity']
    user = UserModel.query.get(user_id)
    return user
