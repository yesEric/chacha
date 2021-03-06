from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.babel import Babel

from config import  config

bootstrap=Bootstrap()
mail=Mail()
moment=Moment()
db=SQLAlchemy()


login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='/auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    babel=Babel(app)
    app.config['BABEL_DEFAULT_LOCALE'] = 'zh_Hans_CN'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .content import content as content_blueprint
    app.register_blueprint(content_blueprint,url_prefix="/content")

    return app