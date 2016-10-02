#!/usr/bin/env python
from flask import Flask
from acqua import db, lm, dropbox

app = Flask(__name__, template_folder='acqua/templates', static_folder='acqua/static')

app.config['SECRET_KEY'] = 'top secret!'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data-dev.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://spwouivjmdveza:9ucBuMeVKqJ9SdRbadnMhhVleb@ec2-54-235-195-226.compute-1.amazonaws.com:5432/dat2m7ridmqocm'
app.config['DROPBOX_KEY'] = 'io55a1kjwn30ulf'
app.config['DROPBOX_SECRET'] = '5el0cfljm1ebct5'
app.config['DROPBOX_ACCESS_TYPE'] = 'acqua'

db.init_app(app)
lm.init_app(app)
dropbox.init_app(app)

# import blueprints
from acqua.admin import admin as admin_blueprint

app.register_blueprint(admin_blueprint)

#mytable1 = TableCreator("mytable1")

#table = mytable1(another_column='claudio')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.commit()

        #db.session.add(table)
        #db.session.commit()

        #result = mytable1.query.all()
        #print result[1].another_column
    app.run(debug=True)
