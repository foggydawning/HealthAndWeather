from flask import render_template, flash
from werkzeug.utils import redirect
from app import app
from app.forms import RegistrationForm


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect("/index")
    return render_template('registration.html', title='Registration', form=form)
