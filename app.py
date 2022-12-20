import logging

from flask import Flask

from main.views import main_blueprint
from loader.views import loader_blueprint

logging.basicConfig(filename="basic.log", level=logging.INFO)

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

app.run(debug=True)
