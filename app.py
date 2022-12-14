from engine.inference_engine import InferenceEngine
from engine.rule import cost_to_int
from flask import Flask, request, jsonify

OK = 200

class UserDestiny:
    def __init__(self, type, biome, weather, cost, country, languages, trip_length):
        self.type = type
        self.biome = biome
        self.weather = weather
        self.cost = cost
        self.country = country
        self.languages = languages
        self.trip_length = trip_length

app = Flask(__name__, template_folder='')

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

    engine = InferenceEngine()
    engine.learn("./static/rules.csv")

    return jsonify(engine.get_most_alike_destiny(user_destiny)), OK
