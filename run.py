#!/usr/bin/env python
import os
from flask import Flask
#from acqua import create_app, db
from acqua.models import User
from acqua import db, lm


app = Flask(__name__, template_folder='acqua/templates')

app.config['SECRET_KEY'] = 'top secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data-dev.sqlite3'


# import configuration
#cfg = os.path.join(os.getcwd(), 'config', config_name + '.py')
#app.config.from_pyfile(cfg)

# initialize extensions
# bootstrap.init_app(acqua)
db.init_app(app)
lm.init_app(app)



# import blueprints
from acqua.admin import admin as admin_blueprint

app.register_blueprint(admin_blueprint)

if __name__ == '__main__':
    #app = create_app('development')
    with app.app_context():
        db.create_all()
        db.session.commit()
        #if User.query.filter_by(username='john').first() is None:
        #    User.register('john', 'cat', 'john.cat@aol.com')
    app.run(debug=True)