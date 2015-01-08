__author__ = 'laurogama'

EXAMPLE = "104_4552.jpg"

IMAGES_PATH = "images/"
FACES_OUTPUT = "output/faces/"
OUTPUT_DIR = "output/"
ORIGINAL = IMAGES_PATH + "original.jpg"
GRAYSCALE = IMAGES_PATH + "grayscale"
BINARIZED = IMAGES_PATH + "binarized"
INVERTED = IMAGES_PATH + "inverted"
THRESHOLD = IMAGES_PATH + "threshold"
ERODED = IMAGES_PATH + "eroded"
MEDIAN_FILTER = IMAGES_PATH + "median_filter"
OUTPUT_TEXT_FILE = OUTPUT_DIR + "output"
FACES = IMAGES_PATH + "faces"

ALLOWED_FILE_FORMAT = ['jpg', 'jpeg', 'png']

# Db config
DATABASE_URL = "postgresql://localhost/carplate_dev"


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'tlklksjldjklskjsslkslslsed'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DATABASE_URL


class TestingConfig(Config):
    TESTING = True
