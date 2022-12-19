from flask import Blueprint, render_template
from utilities import *

main_blueprint = Blueprint('profile_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    data = download_json()
    return render_template("index.html", data=data)
