from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "PredictX API Running"

@app.route('/predict')
def predict():
    temp = request.args.get('temp')
    humidity = request.args.get('humidity')

    if float(humidity) > 75:
        result = "Rain 🌧️"
    else:
        result = "No Rain ☀️"

    return jsonify({
        "temperature": temp,
        "humidity": humidity,
        "prediction": result
    })

app.run()
