from itertools import repeat
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
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


    submit = SubmitField('Зарегистрироваться')
    