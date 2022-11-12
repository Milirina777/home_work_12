import logging

from flask import Flask, send_from_directory

from loader.views import loader_blueprint
from main.views import main_blueprint


app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)
logging.basicConfig(filename="basic.log", level=logging.INFO)

# запускает работу основных файлов
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(host="127.0.0.1", port=8080, debug=True)
