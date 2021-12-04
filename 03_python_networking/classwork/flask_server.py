from flask import Flask, json

cities = [
    {'id': 1, 'name': 'Archangelsk'},
    {'id': 2, 'name': 'Moscow'},
    {'id': 3, 'name': 'Nizhniy Novgorod'}
]

app = Flask(__name__)


@app.route('/cities', methods=['GET'])
def get_cities():
    return json.dumps(cities, indent=4)


@app.route("/")
def main_page():
    return "<p>Welcome to Flask!</p>"


if __name__ == '__main__':
    app.run()
