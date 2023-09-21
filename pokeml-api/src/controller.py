from flask import Flask, send_from_directory, Response
from werkzeug.exceptions import NotFound

# flask --app src/controller.py run
app = Flask(__name__)


@app.route("/")
def base():
    try:
        return send_from_directory('resources', 'index.html')
    except NotFound:
        return Response("The front app has not been built. Please follow the README.", status=404, mimetype='application/json')


@app.route("/<path:path>")
def home(path):
    try:
        return send_from_directory('resources', path)
    except FileNotFoundError:
        return "The front app has not been built. Please follow the README."


@app.route("/health")
def health():
    return "OK"


if __name__ == '__main__':
    # host is required for containerized environments
    app.run(host='0.0.0.0')
