import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"msg": "Server is up!"})


if __name__ == "__main__":
    app.run(port=(os.getenv("PORT")))
