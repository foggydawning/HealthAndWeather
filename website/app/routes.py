import flask_login
from flask import render_template, redirect, request, flash, url_for
from app import app, db
from app.weather import Weather
from app.ipdata_manager import IpdataManager
from app.openweather_manager import OpenweatherManager
from app.forms import RegistrationForm, LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Data


def save_values(value1: int, value2: int, value3: int):
    print(value1, value2, value3)

@app.route('/')
@app.route('/main', methods=['GET', 'POST'])
@login_required
def main():
    if request.method == "POST":
        ipdata_manager = IpdataManager()
        openweather_manager = OpenweatherManager()

        lat, long = ipdata_manager.get_lat_and_lon("188.242.175.115")
        weather: Weather = openweather_manager.get_weather(lat, long)

        user_answer = request.form
        user_id = flask_login.current_user.id
        data = Data(
            user_id=user_id,
            well_being=user_answer.get("radio1"),
            is_head_hurts=user_answer.get("radio2"),
            is_high_pressure=user_answer.get("radio3"),
            temperature=weather.temperature,
            pressure=weather.pressure,
        )
        db.session.add(data)
        db.session.commit()
        flash('Информация добавлена')



        redirect(url_for('main'))
    return render_template("main.html", title='Домашняя страница')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.email.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Поздравляем, вы зарегестрированы!')
        return redirect(url_for('login'))
    return render_template('registration.html', title='Регистрация', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.email.data).first()
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
