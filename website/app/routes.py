from flask import render_template, redirect
from app import app
from app.forms import RegistrationForm, LoginForm

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect("/index")
    return render_template('registration.html', title='Registration', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect("/index")
    return render_template('login_page.html', title='Login', form=form)
