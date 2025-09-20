from flask import Blueprint, render_template, request, redirect, url_for, flash
from .model import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, logout_user,login_user, current_user
from . import db

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return render_template('login.html')
@auth.route('/login', methods=['GET', 'POST'])
def login_details():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get("remember") else False

    user = User.query.filter_by(email=email).first()

    if not user or  not check_password_hash(user.password ,password):
        return redirect('/login')
    login_user(user, remember=remember)
    

    
    return redirect(url_for('main.logger'))

@auth.route('/register')
def register():
    return render_template('register.html')

@auth.route('/register', methods=["GET","POST"])
def register_details():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    gender = request.form.get('gender')
    password = request.form.get('password')
    

    user = User.query.filter_by(email=email).first()
    if user:
        #flash("exists")
        return redirect('/register')
    
    new_user = User(name=name, email=email, phone=phone, gender=gender, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()

    return redirect('/login')

@auth.route('/profile')
@login_required
def profile():
    return render_template('profile.html', details = current_user )


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

