import pytesseract
from PIL import Image
from flask import Flask, jsonify, request

from .utils import get_image_from_request
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
def extract():
    img: Image = get_image_from_request(request)
    text = pytesseract.image_to_string(img, lang='chi_sim', config='--psm 1 --oem 1')
    return {"text": text}
