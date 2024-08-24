from flask import Flask
from os import environ

app = Flask(__name__)

CLIENT_ID = environ.get("CLIENT_ID", "")
CLIENT_HASG = environ.get("CLIENT_HASG", "")
PORT = int(environ.get("PORT", 5000))


@app.route("/")
def hello_world():
    return f"Hello, World! {CLIENT_ID} {CLIENT_HASG}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
