from flask import render_template, redirect, request, flash, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app import app

from app.managers.gaussian_NB_manager import GaussianNBManager
from app.managers.pandas_manager import PandasManager
from app.managers.db_manager import DBManager
from app.managers.network_manager import NetworkManager
from app.forms import RegistrationForm, LoginForm

import time

@app.route('/', methods=['GET', 'POST'])
@app.route('/main', methods=['GET', 'POST'])
@login_required
def main():
    network_manager = NetworkManager()
    if request.method == "POST":
        user_answer = network_manager.get_user_answer()
        weather = network_manager.get_weather()
        user_id = network_manager.get_user_id()
        current_time = time.strftime('%A %B, %d %Y %H:%M:%S')
        DBManager().save_data (
            user_id=user_id,
            time=current_time,
            user_answer=user_answer,
            weather=weather
        )
        flash('Информация добавлена')
        redirect(url_for('main'))
    ip = request.remote_addr
    print(ip)
    city = network_manager.get_city()
    username = network_manager.get_user_username()
    avatar = network_manager.get_user_avatar()
    pressure: int = network_manager.get_weather().pressure

    user_id = NetworkManager().get_user_id()
    data = PandasManager().get_data(user_id)
    gaussian_NB_Manager = GaussianNBManager(data, pressure)
    return render_template(
        "main.html",
        city=city,
        username=username,
        avatar=avatar
    )

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = RegistrationForm()
    if form.validate_on_submit():
        DBManager().save_user(form.username.data, form.email.data, form.password.data)
        flash('Поздравляем, вы зарегестрированы!')
        return redirect(url_for('login'))
    return render_template('registration.html', title='Регистрация', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = LoginForm()
    if form.validate_on_submit():
        email: str = form.email.data
        user = DBManager().get_user(email)
        if user is None or not user.check_password(form.password.data):
            flash('Неправильный логи или пароль')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('main'))
    return render_template('login.html', title='Вход', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main'))
