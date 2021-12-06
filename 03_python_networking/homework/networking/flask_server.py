from flask import Flask

from utils import fib

app = Flask(__name__)


@app.route("/fib", methods=["GET"])
def fib_wrapper() -> str:
    __ = fib()

    return "Pong"


@app.route("/")
def main_page() -> str:
    return "Pong"


def run_flask_server():
    app.run(host="127.0.0.1", port=8090)


if __name__ == "__main__":
    run_flask_server()
