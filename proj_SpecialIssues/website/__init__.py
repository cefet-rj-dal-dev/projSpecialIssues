from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///specialissues.db"
db = SQLAlchemy(app)

from website.adm import rotas
