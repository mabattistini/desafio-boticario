# -*- coding: utf-8 -*-

from cryptography.fernet import Fernet
import hashlib

class Cryptography:

    def __init__(self,key):
        if key is not None:
            self.key = key
            self.cipher_suite = Fernet(key)

    def encryption(self,text):
        cipher_text = self.cipher_suite.encrypt(text)
        return cipher_text

    def decryption(self,text):
        plain_text = self.cipher_suite.decrypt(text)
        return plain_text



    def sha224(self,text):
        r = hashlib.sha224(text).hexdigest()
        return r
