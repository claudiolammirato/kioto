from flask import Flask
from admin import views, admin
from admin.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///databases/test.db'


db.init_app(app)
with app.app_context():
    # Extensions like Flask-SQLAlchemy now know what the "current" app
    # is while within this block. Therefore, you can now run........
    db.create_all()

app.register_blueprint(admin, url_prefix='/admin')