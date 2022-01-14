from itertools import repeat
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    email = EmailField(
<<<<<<< HEAD
        'Username',
        render_kw={"placeholder": "Введите адрес электронной почты"},
=======
        'Username', 
        render_kw={"placeholder": "Введите адрес электронной почты"}, 
>>>>>>> main
        validators=[DataRequired()]
    )

    password = PasswordField(
<<<<<<< HEAD
        'Password',
=======
        'Password', 
>>>>>>> main
        render_kw={"placeholder": "Введите пароль"},
        validators=[DataRequired()]
    )

    repeat_password = PasswordField(
<<<<<<< HEAD
        'Password',
=======
        'Password', 
>>>>>>> main
        render_kw={"placeholder": "Повторите пароль"},
        validators=[DataRequired()]
    )

<<<<<<< HEAD
    submit = SubmitField('Зарегистрироваться')
=======
    submit = SubmitField('Зарегистрироваться')
>>>>>>> main
