from flask import Flask
from os import environ

app = Flask(__name__)

CLIENT_ID = environ.get("CLIENT_ID", "")
CLIENT_HASG = environ.get("CLIENT_HASG", "")


@app.route("/")
def hello_world():
    return f"Hello, World! {CLIENT_ID} {CLIENT_HASG}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
