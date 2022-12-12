from flask import Flask, render_template, request, jsonify
from destiny import Destiny, UserDestiny, read_destinies, cost_to_int
from my_intellect import MyIntellect
import os, json

OK = 200

app = Flask(__name__, template_folder='')

@app.route('/favicon.ico')
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def home():
    return render_template('static/index.html')

@app.route("/result", methods=['POST'])
def result():
    body = request.get_json()
    user_destiny = UserDestiny(
        body["type"],
        body["biome"],
        body["weather"],
        cost_to_int(body["cost"]),
        body["country"] == "si",
        body["languages"].replace(" ", "").split(","),
        float(body["trip_length"])
    )

    destinies = read_destinies('static/destinies.csv')

    destiny_selected = None
    max_hit = 0
    hitted_map = {}

    for destiny in destinies:
        count_field = destiny.compare_fields(user_destiny)
        if max_hit <= count_field:
            max_hit = count_field
            hitted_map[max_hit] = destiny._name

    destiny_selected = None
    print(hitted_map)
    if max_hit >= 4:
        destiny_selected = hitted_map[max_hit]
    destiny_data = {"name": ""}

    if destiny_selected != None:
        destiny_data = {"name": destiny_selected}

    return jsonify(destiny_data), 200
