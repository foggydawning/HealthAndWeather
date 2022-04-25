import time

from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from app import app
from app.forms import LoginForm, RegistrationForm
from app.managers.db_manager import DBManager
from app.managers.gaussian_NB_manager import GaussianNBManager
from app.managers.network_manager import NetworkManager


@app.route("/", methods=["GET", "POST"])
@app.route("/main", methods=["GET", "POST"])
@login_required
def main():
    network_manager = NetworkManager()
    city = network_manager.get_city()
    username = network_manager.get_user_username()
    avatar = network_manager.get_user_avatar()

    predict_message = "К сожалению, у нас не получается составить прогноз на сегодня"

    cur_weather = network_manager.get_cur_weather()
    if cur_weather is None:
        print("Невозможно определить текущую погоду")
    else:
        user_id = network_manager.get_user_id()
        if request.method == "POST":
            user_answer = network_manager.get_user_answer()
            current_time = time.strftime("%A %B, %d %Y %H:%M:%S")
            DBManager().save_data(
                user_id=user_id,
                time=current_time,
                user_answer=user_answer,
                weather=cur_weather,
            )
            redirect(url_for("main"))

        user_id = NetworkManager().get_user_id()
        data = DBManager().get_data(user_id)

        gaussian_NB_Manager = GaussianNBManager(data=data, cur_weather=cur_weather)
        predict = gaussian_NB_Manager.get_predict()
        predict_message = "Сообщение с предсказанием"
        print(predict.is_high_pressure, predict.is_head_hurts, predict.well_being)
    template = render_template(
        "main.html",
        city=city,
        username=username,
        avatar=avatar,
        predict_message=predict_message,
    )
    return template


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for("login"))
    form = RegistrationForm()
    if form.validate_on_submit():
        DBManager().save_user(form.username.data, form.email.data, form.password.data)
        flash("Поздравляем, вы зарегестрированы!")
        return redirect(url_for("login"))
    return render_template("registration.html", title="Регистрация", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main"))
    form = LoginForm()
    if form.validate_on_submit():
        email: str = form.email.data
        user = DBManager().get_user(email)
        if user is None or not user.check_password(form.password.data):
            flash("Неправильный логи или пароль")
            return redirect(url_for("login"))
        login_user(user)
        return redirect(url_for("main"))
    return render_template("login.html", title="Вход", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main"))
