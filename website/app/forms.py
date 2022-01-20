from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    email = EmailField(
        'Email', 
        render_kw={"placeholder": "Введите адрес электронной почты"}, 
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        'Password', 
        render_kw={"placeholder": "Введите пароль"},
        validators=[DataRequired()]
    )

    repeat_password = PasswordField(
        'Repeat Password',
        render_kw={"placeholder": "Повторите пароль"},
        validators=[DataRequired(), EqualTo('password')]
    )
    
    submit = SubmitField('Зарегестрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class LoginForm(FlaskForm):
    email = EmailField(
        'Username', 
        render_kw={"placeholder": "Введите адрес электронной почты"}, 
        validators=[DataRequired()]
    )

    password = PasswordField(
        'Password', 
        render_kw={"placeholder": "Введите пароль"},
        validators=[DataRequired()]
    )

    submit = SubmitField('Войти')
