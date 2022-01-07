from flask import render_template
from app import app

@app.route('/')
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    return render_template('registration.html')

