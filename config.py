import os

DEBUG = True
PORT = 5000
HOST = "0.0.0.0"
SECRET_KEY = "o8-jEsz5fMEMY0hwIjwzfiuF0pYdvP0a0ckToSZuMtk="

TIME_TOKEN_EXPIRATION   = 10

DATABASE = os.path.dirname((__file__))+ os.path.sep +'boticario.db'

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+DATABASE
