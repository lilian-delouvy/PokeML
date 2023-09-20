from flask import Flask, send_from_directory

# flask --app src/controller.py run
app = Flask(__name__)


@app.route("/")
def base():
    return send_from_directory('resources', 'index.html')


@app.route("/<path:path>")
def home(path):
    return send_from_directory('resources', path)


@app.route("/health")
def health():
    return "OK"


if __name__ == '__main__':
    # host is required for containerized environments
    app.run(host='0.0.0.0')
