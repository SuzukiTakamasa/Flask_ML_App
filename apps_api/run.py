import os

from flask import Flask

from apps_api.api import api
from apps_api.api.config import config


config_name = os.environ.get("CONFIG", "local")

app = Flask(__name__)
app.config.from_object(config[config_name])
app.register_blueprint(api)


