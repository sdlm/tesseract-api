import io

from PIL import Image

from . import settings, exceptions


def get_image_from_request(request, rise_exc: bool = True):
    file = get_file_from_request(request, rise_exc)
    img = Image.open(io.BytesIO(file.read()))
    print(f"filename: {file.filename}, mimetype: {file.mimetype}, size: {img.size}")
    return img


def get_file_from_request(request, rise_exc: bool = True):
    if "file" not in request.files:
        if rise_exc:
            raise exceptions.InvalidUsage("You must send file")
        return None

    file = request.files["file"]
    if not file or file.filename == "":
        if rise_exc:
            raise exceptions.InvalidUsage("You must send file")
        return None

    if not allowed_file(file.filename):
        if rise_exc:
            raise exceptions.InvalidUsage("Only .jpg allowed")
        return None

    if file.mimetype not in settings.ALLOWED_MIMETYPES:
        if rise_exc:
            raise exceptions.InvalidUsage("Only JPEG images allowed")
        return None

    return file


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in settings.ALLOWED_EXTENSIONS
