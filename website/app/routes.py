from flask import render_template, redirect, request, flash, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app import app

from app.db_manager import DBManager
from app.network_manager import NetworkManager
from app.forms import RegistrationForm, LoginForm


@app.route('/')
@app.route('/main', methods=['GET', 'POST'])
@login_required
def main():
    if request.method == "POST":
        user_answer = NetworkManager().get_user_answer()
        weather = NetworkManager().get_weather()
        user_id = NetworkManager().get_user_id()
        current_time = str("12.03.2022")
        DBManager().save_data (
            user_id=user_id,
            time=current_time,
            user_answer=user_answer,
            weather=weather
        )
        flash('Информация добавлена')
        redirect(url_for('main'))
    return render_template("main.html", title='Домашняя страница')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        DBManager().save_user(form.email.data, form.password.data)
        flash('Поздравляем, вы зарегестрированы!')
        return redirect(url_for('login'))
    return render_template('registration.html', title='Регистрация', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = DBManager().get_user(email)
        if user is None or not user.check_password(form.password.data):
            flash('Неправильный логи или пароль')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('main'))
    return render_template('login_page.html', title='Вход', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main'))
