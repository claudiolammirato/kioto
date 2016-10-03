from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(1, 16)])
    password = PasswordField('Password', validators=[DataRequired()])
    #remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')

class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(1, 16)])
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Password must match!!!')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class Acqdimension(Form):
    height = StringField('Height')
    lenght = StringField('Lenght')
    width = StringField('Width')
    liters = StringField('Liters')
    submit = SubmitField('save')