from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY="2AZSMss3p5QPbcY2hBsJ",
        SQLALCHEMY_DATABASE_URI=f"sqlite:////{Path(__file__).parents[1]}/local.sqlite",
        SQLALCHEMY_TRACK_MODIFICATION=False
    )

    db.init_app(app)
    Migrate(app, db)


    from apps.crud import views as crud_views
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app