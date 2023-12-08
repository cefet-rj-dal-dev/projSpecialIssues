from website import db, app, bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
class SPI(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    editora = db.Column(db.String, unique=False, nullable=False)
    revista = db.Column(db.String, unique=False, nullable=False)
    titulo = db.Column(db.String, unique=False, nullable=False)
    link = db.Column(db.String, unique=True, nullable=False)
    prazo = db.Column(db.Date, unique=False, nullable=False)
    datanot = db.Column(db.Date, unique=False, nullable=False)
    detalhes = db.Column(db.String, unique=False, nullable=False)

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String, unique=True, nullable=False)
    senha = db.Column(db.String, unique=True, nullable=False)
    
    
with app.app_context():

    db.create_all()
