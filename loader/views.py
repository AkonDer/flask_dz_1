from flask import send_from_directory, Blueprint, render_template

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("./uploads", path)


@loader_blueprint.route("/post/", methods=['GET'])
def post_page():
    return render_template("post_form.html")


@loader_blueprint.route("/post/", methods=['POST'])
def upload_page():
    return render_template("post_uploaded.html")


