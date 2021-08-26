from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()
def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config_options[config_name])
    
    # Initializing flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    # configure UploadSet
    bootstrap = Bootstrap(app)
    
    with app.app_context():
        # Registering main blueprint
        from . main import main as main_blueprint
        app . register_blueprint (main_blueprint)


        #Register auth blueprint
        from .auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    
        # # Configure request   
        from .requests import configure_request
        configure_request(app)
      
        from .requests import configure_request
        configure_request(app)

        db.create_all()
    
    return app