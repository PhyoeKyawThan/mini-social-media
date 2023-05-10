from flask import Blueprint, render_template, request, redirect, url_for, session, send_file, current_app, flash
from werkzeug.utils import secure_filename
from os import path
from flask_login import current_user, login_required
from . import db
# from .img_upload import save_file
from .models import Post, User
from datetime import datetime
from . import auth

views = Blueprint("views", __name__)

@views.route("/")
@login_required
def home():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template("index.html", posts=posts)

@views.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == 'POST':
        caption = request.form["caption"]
        upload_file = request.files['file']
        file_name = secure_filename(upload_file.filename)
        if caption != '' or upload_file:
            new_post = Post(caption=caption, date=datetime.now(), imgPath=path.join("static/images", file_name), user_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
        #check file_null or not
        if upload_file:
            PATH = f"images/{file_name}"
            if path.exists(path.join(current_app.config['UPLOAD_FOLDER'], PATH)):
                pass
            else:
                upload_file.save(path.join(current_app.config['UPLOAD_FOLDER'], PATH))
        return redirect(url_for('views.profile'))
        

@views.route('/profile')
@login_required
def profile():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template("profile.html", posts=current_user.posts)

@views.route("/edit_profile")
@login_required
def edit_profile():
  return render_template("profile-edit.html")

@views.route('/edit', methods=['POST', 'GET'])
@login_required
def edit():
    if request.method == 'POST':
        profile = request.files['profile']
        username = request.form['username']
        origin_password = request.form['origin_pass']
        new_password = request.form['new_password']
        
        #update pass and new profile location
        
        if profile:
            PATH = f"profiles/{secure_filename(profile.filename)}"
            if path.exists(path.join(current_app.config['UPLOAD_FOLDER'], PATH)):
                pass
            else:
                profile.save(path.join(current_app.config['UPLOAD_FOLDER'], PATH))
                current_user.profile = f"static/profiles/{secure_filename(profile.filename)}"
                
        #username and password update 
        if current_user.username != username:
            current_user.username = username
        if origin_password != '' or new_password != '':
            if origin_password != current_user.password:
                flash("Your old password is worng", category="passerror")
                return redirect(url_for('views.edit_profile'))
            elif current_user.password == new_password:
                flash("New password must not same with original password", category="error")
                return redirect(url_for('views.edit_profile'))
            else:
              current_user.password = new_password
        db.session.commit() #commit update data
        return redirect(url_for('views.profile'))

@views.route('/delete/<id>')
@login_required
def delete(id):
    post = Post.query.filter_by(id=id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('views.profile'))
    
@views.errorhandler(401)
def unauthorized_error_handlar(error):
    return redirect(url_for('auth.sign_up'))