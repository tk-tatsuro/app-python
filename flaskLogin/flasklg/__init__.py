import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Flask-Loginライブラリアプリケーションの接続
login_manager = LoginManager()

# ログイン関数
login_manager.login_view = 'app.login'

# ログインにリダイレクトした際のメッセージ
login_manager.login_message = 'ログインしてください。'

# 変数作成
basedir = os.path.abspath(os.path.dirname(__name__))
# ライブラの接続
db = SQLAlchemy
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysite'
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from flasklg.views import bp
    app.register_blueprint(bp)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    return app
