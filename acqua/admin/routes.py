from flask import render_template, redirect, url_for, request
from flask_login import login_required, login_user, logout_user
from ..models import User
from . import admin
from .forms import LoginForm, RegisterForm


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.verify_password(form.password.data):
            return redirect(url_for('admin.login', **request.args))
        login_user(user) #form.remember_me.data)
        return redirect(request.args.get('next') or url_for('admin.index'))
    return render_template('login.html', form=form)

@admin.route('/register', methods=['GET', 'POST'])
def register():
    form1 = RegisterForm()
    if form1.validate_on_submit():
        #User.register('john', 'cat', 'john.cat@aol.com')
        User.register(form1.username.data, form1.password.data, form1.email.data)
        return redirect(url_for('admin.login'))
    return render_template('register.html', form = form1)


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.index'))


@admin.route('/')
def index():
    return render_template('index.html')


@admin.route('/protected')
@login_required
def protected():
    return render_template('protected.html')
