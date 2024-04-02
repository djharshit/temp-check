from flask import Flask
from os import environ

app = Flask(__name__)


@app.route("/")
def hello_world():
    var = environ.get("TEMP_VAR", "default")
    return "Hello, World! " + var


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
