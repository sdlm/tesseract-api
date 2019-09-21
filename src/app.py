from flask import Flask, jsonify

from .exceptions import InvalidUsage

app = Flask(__name__)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route("/")
def ping():
    return {"status": "ok"}


@app.route("/extract", methods=["POST"])
def get_the_same_img():
    return {"status": "ok"}
