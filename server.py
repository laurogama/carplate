from timeit import timeit, Timer

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from Settings import *
from ocr.OCR import execute_ocr


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)


@app.route("/takepicture")
def take_picture():
    Timer.timeit(number=10)
    execute_ocr()
    return


@app.route("/")
def index():
    return "Hello there!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')