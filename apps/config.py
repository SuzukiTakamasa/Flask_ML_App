from pathlib import Path

basedir = Path(__file__).parents[1]

class BasicConfig:
    SECRET_KEY = "2AZSMss3p5QPbcY2hBsJ"
    WTF_CSRF_SECRET_KEY = "AuwzyszUSsugKN7KZs6f"
    UPLOAD_FOLDER = str(Path(basedir, "apps", "images"))
    LABELS = [
        "unlabeled",
        "person",
        "bicycle",
        "car",
        "motorcycle",
        "airplane",
        "bus",
        "train",
        "truck",
        "boat",
        "traffic light",
        "fire hydrant",
        "street sign",
        "stop sign",
        "parking meter",
        "bench",
        "bird",
        "cat",
        "dog",
        "horse",
        "sheep",
        "cow",
        "elephant",
        "bear",
        "zebra",
        "giraffe",
        "hat",
        "backpack",
        "umbrella",
        "shoe",
        "eye glasses",
        "handbag",
        "tie",
        "suitcase",
        "frisbee",
        "skis",
        "snowboard",
        "sports ball",
        "kite",
        "baseball bat",
        "baseball glove",
        "skateboard",
        "surfboard",
        "tennis racket",
        "bottle",
        "plate",
        "wine glass",
        "cup",
        "fork",
        "knife",
        "spoon",
        "bowl",
        "banana",
        "apple",
        "sandwich",
        "orange",
        "broccoli",
        "carrot",
        "hot dog",
        "pizza",
        "donut",
        "cake",
        "chair",
        "couch",
        "potted plant",
        "bed",
        "mirror",
        "dining table",
        "window",
        "desk",
        "toilet",
        "door",
        "tv",
        "laptop",
        "mouse",
        "remote",
        "keyboard",
        "cell phone",
        "microwave",
        "oven",
        "toaster",
        "sink",
        "refrigerator",
        "blender",
        "book",
        "clock",
        "vase",
        "scissors",
        "teddy bear",
        "hair drier",
        "toothbrush",
    ]

class LocalConfig(BasicConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:////{basedir}/local.sqlite"
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_ECHO = True

class TestingConfig(BasicConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:////{basedir}/testing.sqlite"
    SQLALCHEMY_TRACK_MODIFICATION = False
    WTF_CSRF_ENABLED = False
    UPLOAD_FOLDER = str(Path(basedir, "tests", "detector", "image"))

config = {
    "testing": TestingConfig,
    "local": LocalConfig,
}