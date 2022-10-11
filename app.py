from flask import Flask
import sys
app = Flask(__name__)


@app.route("/")
def hello():
    return "api test!"

@app.route("/test")
def hi():
    return "Can I believe goorm?"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)