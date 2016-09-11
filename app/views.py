from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    message = 'hello claudio!'
    return render_template('index.html', message=message)

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":

    return render_template('register.html')
