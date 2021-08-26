
from flask import render_template,redirect,url_for, flash,request, session
from .forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, login_required
from ..models import User
from .. import db, mail
from app import login_manager
from . import auth
from flask_mail import Message
from ..email import mail_message





# login route
@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            print(login_form.remember.data)
            login_user(user,remember=login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or Password')

    return render_template('login.html',login_form = login_form)
#logout user route
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        mail_message("Welcome to watchlist","email/welcome_user",user.email,user=user)
        return redirect(url_for('auth.login'))


    return render_template('register.html',registration_form = form)

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth.login'))