from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_dropbox import Dropbox

db = SQLAlchemy()
lm = LoginManager()
lm.login_view = 'admin.login'
dropbox = Dropbox()


