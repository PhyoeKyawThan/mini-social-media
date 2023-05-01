from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'domisgay'
    app.secret_key = 'domis'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
    app.config['UPLOAD_FOLDER'] = 'social/static/images'#image file save path
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    #register blueprint
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth")

    from .models import User, Post
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    # login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app

def create_database(app):
    if not path.exists('social/database.db'):
        db.create_all(app)
        print("Created DB")