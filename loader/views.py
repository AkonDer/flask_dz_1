from flask import send_from_directory, Blueprint

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("./uploads", path)
