from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from models import Usuario


class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(message="El nombre de usuario es obligatorio")])
    password = PasswordField('Contraseña', validators=[DataRequired(message="La contraseña es obligatoria")])
    submit = SubmitField('Iniciar Sesión')


class RegistrationForm(FlaskForm):
    username = StringField('Usuario', validators=[
        DataRequired(message="El nombre de usuario es obligatorio"),
        Length(min=3, max=64, message="El nombre de usuario debe tener entre 3 y 64 caracteres")
    ])
    email = EmailField('Correo Electrónico', validators=[
        DataRequired(message="El correo electrónico es obligatorio"),
        Email(message="Por favor, introduce un correo electrónico válido")
    ])
    password = PasswordField('Contraseña', validators=[
        DataRequired(message="La contraseña es obligatoria"),
        Length(min=8, message="La contraseña debe tener al menos 8 caracteres")
    ])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[
        DataRequired(message="Por favor, confirma tu contraseña"),
        EqualTo('password', message="Las contraseñas deben coincidir")
    ])
    submit = SubmitField('Registrarse')

    def validate_username(self, username):
        user = Usuario.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Este nombre de usuario ya está en uso. Por favor, elige otro.')

    def validate_email(self, email):
        user = Usuario.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Este correo electrónico ya está registrado. Por favor, utiliza otro.')
