from flask import Flask, render_template, request,session, redirect, url_for,g

app = Flask(__name__)

@app.route('/')
def index():
    message = 'hello claudio!'
    return render_template('index.html', message=message)

@app.before_request
def before_request():
    g.user=None
    if 'user' in session:
        g.user = session ['user']

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        session.pop('user', None)
        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            return redirect(url_for('protected'))

    return render_template('login.html')

@app.route('/protected')
def protected():
    if g.user:
        return render_template('protected.html')

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']
    return 'Not Logged In!'