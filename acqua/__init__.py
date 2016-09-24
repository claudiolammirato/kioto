import os
from flask import Flask


from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
lm = LoginManager()
lm.login_view = 'admin.login'

#from flask_bootstrap import Bootstrap
#from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager

#bootstrap = Bootstrap()
#db = SQLAlchemy()
#lm = LoginManager()
#lm.login_view = 'admin.login'


##def create_app(config_name):
##    """Create an application instance."""
##    app = Flask(__name__)

    # import configuration
##    cfg = os.path.join(os.getcwd(), 'config', config_name + '.py')
##    app.config.from_pyfile(cfg)
##
    # initialize extensions
    #bootstrap.init_app(acqua)
##    db.init_app(app)
##    lm.init_app(app)

    # import blueprints
 ##   from .admin import admin as admin_blueprint
 ##   app.register_blueprint(admin_blueprint)

 ##   return app