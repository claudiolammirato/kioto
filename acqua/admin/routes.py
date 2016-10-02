from flask import render_template, redirect, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
from ..models import User, Acqdim, addim, deldim
from . import admin
from .forms import LoginForm, RegisterForm, Acqdimension


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


@admin.route('/acqdimension', methods=['GET','POST'])
@login_required
def acqdimension():
    form = Acqdimension()
    if request.method == 'GET':
        #height = Acqdim.query.order_by(Acqdim.height.desc()).all()
        #for x in height:
            #print x.height, x.users, x.lenght, x.width
        deldim()

        h = Acqdim.query.filter_by(users=current_user).first()
        if h:
            form.height.data = h.height
            form.lenght.data = h.lenght
            form.width.data = h.width
            form.liters.data = h.height * h.width * h.lenght / 1000
        else:
            form.height.data = 'NA'
            form.lenght.data = 'NA'
            form.width.data = 'NA'

    if form.validate_on_submit():
        user = User.query.filter_by(username=current_user.username).first()
        #print user
        #print form.height.data
        addim(form.height.data, form.lenght.data, form.width.data, current_user)
        return redirect(url_for('admin.acqdimension'))

    return render_template('acqdimension.html', form=form)
