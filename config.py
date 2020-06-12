import os

DEBUG = True
PORT = 5000
HOST = "0.0.0.0"
SECRET_KEY = "o8-jEsz5fMEMY0hwIjwzfiuF0pYdvP0a0ckToSZuMtk="

TIME_TOKEN_EXPIRATION = 10

DATABASE = os.path.dirname((__file__)) + os.path.sep + 'boticario.db'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE

## Configurações de teste

host = f"http://127.0.0.1:{PORT}"

urls = {
    "auth": host + "/auth",
    "cadastrar_vendedor": host + "/vendedor/create",
    "login_vendedor": host + "/vendedor/login",
    "cadastrar_venda": host + "/venda/create",
    "alterar_venda": host + "/venda/edit",
    "excluir_venda": host + "/venda/delete",
    "vendas_cadastradas": host + "/venda/list",
    "cashback_acumulado": host + "/venda/cashback",
}
