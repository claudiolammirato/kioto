from flask import render_template, redirect, url_for, request, abort, session
from flask_login import login_required, login_user, logout_user, current_user
from ..models import User, Acqdim
from . import admin

from .forms import LoginForm, RegisterForm, Acqdimension
from dropbox.client import DropboxOAuth2Flow, DropboxClient


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
        Acqdim.deldim()

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
        Acqdim.addim(form.height.data, form.lenght.data, form.width.data, current_user)
        return redirect(url_for('admin.acqdimension'))

    return render_template('acqdimension.html', form=form)

@admin.route('/datafish')
def datafish():
    return render_template('datafish.html')


'''UPLOAD PER SCHEDA
@admin.route('/upload')
@login_required
def upload():

    return render_template('upload.html')

@admin.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        #path = 'cla'
        file = request.files['file']

        client = DropboxClient(session['access_token'])

        filename = secure_filename(file.filename)

        # Actual uploading process
        result = client.put_file('/' + filename, file.read())

        path = result['path'].lstrip('/')
    return redirect(url_for('admin.success', filename=path))

@admin.route('/success/<path:filename>')
def success(filename):
    return u'File successfully uploaded as /%s' % filename
'''

#DOWNLOAD DROPBOX  "The items in the basket are %s and %s" % (x,y)
@admin.route('/download', methods = ['GET', 'POST'])
def download():
    if request.method == 'POST':
        try:
            client = DropboxClient(session['access_token'])
            # Actual downloading process
            f, metadata = client.get_file_and_metadata('/%s.jpg' % (current_user.username))
            out = open('acqua/static/user/%s.jpg' % (current_user.username), 'wb')
            out.write(f.read())
            out.close()
            #print metadata
        except:
            print'nonloggato'
        return redirect(url_for('admin.index'))

    return render_template('download.html')

#DROPBOX  ACCESSO
DROPBOX_APP_KEY = 'io55a1kjwn30ulf'
DROPBOX_APP_SECRET = '5el0cfljm1ebct5'

@admin.route('/dropbox')
def dropbox():
    if not 'access_token' in session:
        return redirect(url_for('admin.dropbox_auth_start'))
    return redirect(url_for('admin.index'))

@admin.route('/dropbox-auth-start')
def dropbox_auth_start():
    return redirect(get_auth_flow().start())

@admin.route('/dropbox-auth-finish')
def dropbox_auth_finish():
    try:
        access_token, user_id, url_state = get_auth_flow().finish(request.args)
    except:
        abort(400)
    else:
        session['access_token'] = access_token
    return redirect(url_for('admin.index'))

def get_auth_flow():
    redirect_uri = url_for('admin.dropbox_auth_finish', _external=True)
    return DropboxOAuth2Flow(DROPBOX_APP_KEY, DROPBOX_APP_SECRET, redirect_uri,session, 'dropbox-auth-csrf-token')

@admin.route('/dropboxlogout')
def dropboxlogout():
    try:
        session.pop('access_token')
    except:
        print'nonloggato'

    return redirect(url_for('admin.index'))

#FINE AUTH DROPBOX