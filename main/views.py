from flask import Blueprint, render_template, request
from utilities import *

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template("index.html")


@main_blueprint.route('/search/')
def post_list_page():
    data = download_json()
    word = request.args.get('find')
    _list = search(data, word)
    return render_template("post_list.html", data=_list, word=word)
