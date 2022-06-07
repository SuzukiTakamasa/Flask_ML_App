from pathlib import Path

basedir = Path(__file__).parents[1]

class BasicConfig:
    SECRET_KEY = "2AZSMss3p5QPbcY2hBsJ"
    WTF_CSRF_SECRET_KEY = "AuwzyszUSsugKN7KZs6f"
    UPLOAD_FOLDER = str(Path(basedir, "apps", "images"))
    LABELS = []

class LocalConfig(BasicConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:////{basedir}/local.sqlite"
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_ECHO = True

class TestingConfig(BasicConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:////{basedir}/testing.sqlite"
    SQLALCHEMY_TRACK_MODIFICATION = False
    WTF_CSRF_ENABLED = False

config = {
    "testing": TestingConfig,
    "local": LocalConfig,
}