import sqlite3

from app.helpers.criptografia import Cryptography
from config import DATABASE

conn = sqlite3.connect(DATABASE)

sql = '''INSERT INTO USERS (USERNAME, NAME, PASSWORD) VALUES (?,?,?)'''

cur = conn.cursor()
password = Cryptography(None).sha224(b'pwdboticario')
cur.execute(sql, ('usrboticario','usuario de autenticacao',password))
conn.commit()
print(cur.lastrowid)
conn.close()