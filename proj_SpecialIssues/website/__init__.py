from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
#postgresql://special_issues_db_user:HO2o6PokfdzY3tOdreIbDP6Na2ZBNCWI@dpg-cp2hg1ev3ddc73cmchs0-a.oregon-postgres.render.com/special_issues_db
app.config['SECRET_KEY']='123456789'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from website.adm import rotas
from website.users import users_rotas
