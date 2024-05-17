from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///specialissues.db'
app.config['SECRET_KEY']='123456789'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from website.adm import rotas
from website.users import users_rotas
