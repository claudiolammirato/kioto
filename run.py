#!/usr/bin/env python
from flask import Flask
from acqua import db, lm


app = Flask(__name__, template_folder='acqua/templates', static_folder='acqua/static')

app.config['SECRET_KEY'] = 'top secret!'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data-dev.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://spwouivjmdveza:9ucBuMeVKqJ9SdRbadnMhhVleb@ec2-54-235-195-226.compute-1.amazonaws.com:5432/dat2m7ridmqocm'

db.init_app(app)
lm.init_app(app)

# import blueprints
from acqua.admin import admin as admin_blueprint

app.register_blueprint(admin_blueprint)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(debug=True)
