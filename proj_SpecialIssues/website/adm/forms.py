from wtforms import Form, BooleanField, StringField, PasswordField, validators, DateField
class RegistrationForm(Form):
    editora = StringField('Editora', [validators.Length(min=4, max= 25)])
    revista = StringField('Revista', [validators.Length(min=6, max= 100)])
    titulo = StringField('Título da Special Issue', [validators.Length(min=6, max= 500)])
    link = StringField('Website (link)', [validators.Length(min=6, max= 50)])
    prazo = StringField('Prazo de Submissão', [validators.Length(min=6, max= 35)])
    datanot = StringField('Data de notificação', [validators.Length(min=6, max= 10)]) #datefield?
    detalhes = StringField('Detalhes', [validators.Length(min=6, max= 5000)])

class login(Form):
    usuario = StringField('Usuário', [validators.Length(min=4, max= 25)])
    senha = PasswordField('Senha', [validators.DataRequired()])










    #--------para registrar senhas por uma pagina de registros----------#
    #password = PasswordField('Digite a senha', [validators.DataRequired(), validators.EqualTo('confirmar', message= 'As senhas não coincidem')])
    #confirm = PasswordField('Digite novamente a senha')
    #accept_tos = BooleanField('I accept the TOS'[validators.DataRequired()])
