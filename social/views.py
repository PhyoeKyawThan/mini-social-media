from flask import Blueprint, render_template, request, redirect, url_for, session, send_file, current_app
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
        new_post = Post(caption=caption, date=datetime.now(), imgPath=path.join("static/images", file_name), user_id=current_user.id)
        db.session.add(new_post)
        db.session.commit()
        #check file_null or not
        if upload_file:
            if path.exists(path.join(current_app.config['UPLOAD_FOLDER'], file_name)):
                pass
            else:
                upload_file.save(path.join(current_app.config['UPLOAD_FOLDER'], file_name))
        return redirect(url_for('views.profile'))
        

@views.route('/profile')
@login_required
def profile():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template("profile.html", posts=current_user.posts)

@views.errorhandler(401)
def unauthorized_error_handlar(error):
    return redirect(url_for('auth.login'))