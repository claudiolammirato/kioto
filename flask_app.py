import os
from flask import Flask, session

from admin import admin

app = Flask(__name__)
app.secret_key = 'claudio'
#regsitrare blueprint
app.register_blueprint(admin, url_prefix='/blue')

@app.route('/')
def index():
  return "Hello nice"

if __name__ == '__main__':
	app.run(debug=True)