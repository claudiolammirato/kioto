from flask import Flask, render_template, request,session, redirect, url_for,g, Blueprint
from .models import Users


#creare blueprint
admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/claudio')
def index():
    #message = 'hello claudio!'
    #return render_template('index.html', message=message)
    return 'claudio'

@admin.before_request
def before_request():
    g.user=None
    if 'user' in session:
        g.user = session ['user']

@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        session.pop('user', None)

        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            return redirect(url_for('admin.protected'))

    return render_template('login.html')

@admin.route('/protected')
def protected():
    if g.user:
        return render_template('protected.html')

@admin.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return redirect(url_for('admin.login'))

@admin.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']
    return 'Not Logged In!'
