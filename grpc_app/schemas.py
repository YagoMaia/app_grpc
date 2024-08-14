from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField, EmailField

class MyForm(FlaskForm):
    """
    Classe responsável por criar um formulário para fazer o login
    """
    email = EmailField("Email", validators=[validators.DataRequired()])
    password = PasswordField("Senha", validators=[validators.DataRequired()]) 
    submit = SubmitField("Submit")

class FormGetUser(FlaskForm):
    user_id = StringField("Id Usuário", validators=[validators.DataRequired()])
    submit = SubmitField("Submit")

class FormNewUser(FlaskForm):
    """
    Classe responsável por criar um formulário para inserir dados no usuário a ser inserido
    """
    name = StringField("Nome", validators=[validators.DataRequired()])
    email = EmailField("Email", validators=[validators.DataRequired()])
    submit = SubmitField("Submit")
    
class FormUpdateUser(FlaskForm):
    """
    Classe responsável por criar um formulário para inserir dados no usuário a ser inserido
    """
    name = StringField("Nome", validators=[validators.DataRequired()])
    email = EmailField("Email", validators=[validators.DataRequired()])
    submit = SubmitField("Submit")
    
class FormDeleteUser(FlaskForm):
    """
    Classe responsável por criar um formulário para inserir dados no usuário a ser inserido
    """
    user_id = StringField("Id Usuário", validators=[validators.DataRequired()])
    submit = SubmitField("Submit")

class User(UserMixin):
    """
    Classe do usuário
    """
    def __init__(self, email = None, name = None, id = None):
        self.email = email
        self.name = name
        self.id = id