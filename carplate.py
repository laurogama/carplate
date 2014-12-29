from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from Settings import *
import Settings
from ocr.OCR import process_image, execute_tesseract


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)


@app.route("/takepicture")
def take_picture():
    # OCR.take_picture()
    process_image()
    execute_tesseract(THRESHOLD + ".png")
    return "Hello World!"

@app.route("/")
def index():
    return "Hello there!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')