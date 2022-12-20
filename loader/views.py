import logging

from flask import send_from_directory, Blueprint, render_template, request
from utilities import *

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("./uploads", path)


@loader_blueprint.route("/post/", methods=['GET'])
def post_page():
    return render_template("post_form.html")


@loader_blueprint.route("/post/", methods=['POST'])
def upload_page():
    picture = request.files.get("picture")
    description = request.form.get("description")
    filename = picture.filename
    if check_file_type(filename):
        picture.save(f"./uploads/{filename}")
        save_json(description, filename)
        return render_template("post_uploaded.html", filename=filename, description=description)
    else:
        logging.exception("Неправильный тип файла")
        return "Неправильный тип файла"

