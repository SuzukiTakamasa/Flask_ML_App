import os
import shutil

import pytest
from apps.app import create_app, db

from apps.crud.models import User
from apps.detector.models import UserImage, UserImageTag

#Fixture function for various unit tests
@pytest.fixture
def fixture_app():
    app = create_app("testing")

    app.app_context().push()

    with app.app_context():
        db.create_all() #Create database table for test
    
    os.mkdir(app.config["UPLOAD_FOLDER"])

    yield app #Execute Test

    User.query.delete()
    UserImage.query.delete()
    UserImageTag.query.delete()

    shutil.rmtree(app.config["UPLOAD_FOLDER"])

    db.session.commit()

@pytest.fixture
def client(fixture_app):
    return fixture_app.test_client()