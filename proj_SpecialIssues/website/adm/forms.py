from wtforms import Form, StringField, validators, PasswordField
from wtforms.fields import DateField

class RegistrationForm(Form):
    editora = StringField('Editora', [validators.Length(min=4, max=100)])
    revista = StringField('Revista', [validators.Length(min=6, max=100)])
    titulo = StringField('Título da Special Issue', [validators.Length(min=6, max=500)])
    link = StringField('Website (link)', [validators.Length(min=6, max=500)])
    prazo = DateField('Prazo de Submissão')
    datanot = DateField('Data de notificação')
    detalhes = StringField('Detalhes', [validators.Length(min=1, max=5000)])

class login(Form):
    usuario = StringField('Usuário', [validators.Length(min=4, max= 25)])
    senha = PasswordField('Senha', [validators.DataRequired()])








