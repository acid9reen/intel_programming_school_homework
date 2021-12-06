from flask import Flask, json, request

cities = [
    {"id": 1, "name": "Archangelsk"},
    {"id": 2, "name": "Moscow"},
    {"id": 3, "name": "Nizhniy Novgorod"},
]

app = Flask(__name__)


@app.route("/cities", methods=["GET"])
def get_cities():
    return json.dumps(cities, indent=4)


@app.route("/fib", methods=["GET", "POST"])
def fib():
    n = request.args.get("n", type=int)

    if n is None:
        return

    prev_prev, prev = 0, 1

    if n == 0:
        return str(prev_prev)
    if n == 1:
        return str(prev)

    for __ in range(1, n):
        tmp = prev + prev_prev
        prev_prev = prev
        prev = tmp

    return str(prev)


@app.route("/")
def main_page():
    return "<p>Welcome to Flask!</p>"


if __name__ == "__main__":
    app.run()
