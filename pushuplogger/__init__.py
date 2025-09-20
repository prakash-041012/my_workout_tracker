from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "supersecretkey" 
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pushups.sqlite"
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    

    from .model import User

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    from .main import main as mainblueprint
    app.register_blueprint(mainblueprint)

    from .auth import auth as authblueprint
    app.register_blueprint(authblueprint)


    with app.app_context():
        db.create_all()

    
    return app