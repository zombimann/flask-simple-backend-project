import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://zombi:C0mpradors*@localhost/mydb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
