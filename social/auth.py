from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from .models import User
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from datetime import datetime
auth = Blueprint("auth", __name__)

@auth.route("/sign_up", methods=['POST', 'GET'])
def sign_up():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_pass = request.form["confirm_pass"]

        user = User.query.filter_by(username=username).first()
        if user:
            flash("Username already exists, please login with your password.", category='user_exists')
            return redirect(url_for('auth.login'))
        if password != confirm_pass:
            flash("Password doesn't match", category='passnotmatch')
        else:
            new_user = User(username=username, password=password, date=datetime.now())
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created Successfully", category='success')
            return redirect(url_for('views.home'))
    else:
        if current_user.is_authenticated:
            return redirect(url_for("views.home"))
        else:
            return render_template('sign_up.html')
        
@auth.route('/user')
def user():
    data = User.query.all()

    return render_template('user.html', users=data)

@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        password = User.query.filter_by(password=password)
        if user and password:
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
        else:
            msg = "Username or password doesn't match"
            return render_template('login.html', error = msg)
    else:
        if current_user.is_authenticated:
            return redirect(url_for("views.home"))
        else:
            return render_template('login.html')
            
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
