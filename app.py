from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)


with open("traffic_model.pkl", "rb") as f:
    saved_data = pickle.load(f)

model = saved_data["model"]

city_encoder = saved_data["city_encoder"]
weather_encoder = saved_data["weather_encoder"]
road_encoder = saved_data["road_encoder"]
target_encoder = saved_data["target_encoder"]


@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.json

        city = data.get("city", "").title()
        hour = int(data.get("hour", 0))
        day = int(data.get("day", 0))
        temp = float(data.get("temp", 0))
        rain = float(data.get("rain_1h", 0))
        clouds = int(data.get("clouds_all", 0))
        weather = data.get("weather_main", "").title()
        holiday = int(data.get("holiday", 0))
        road = data.get("road_condition", "").title()
        signal = int(data.get("traffic_signal_delay", 0))

        if day >= 5:
            is_weekend = 1
        else:
            is_weekend = 0

        
        city_encoded = city_encoder.transform([city])[0]

        weather_encoded = weather_encoder.transform([weather])[0]

        road_encoded = road_encoder.transform([road])[0]

        sample = pd.DataFrame([{
            "city": city_encoded,
            "hour": hour,
            "day": day,
            "is_weekend": is_weekend,
            "temp": temp,
            "rain_1h": rain,
            "clouds_all": clouds,
            "weather_main": weather_encoded,
            "holiday": holiday,
            "road_condition": road_encoded,
            "traffic_signal_delay": signal
        }])

        prediction = model.predict(sample)[0]
        probabilities = model.predict_proba(sample)[0]

        confidence = round(max(probabilities) * 100)
        

        result = target_encoder.inverse_transform([prediction])[0]
        

        return jsonify({
    "prediction": result,
    "confidence": confidence
})
    except Exception as e:

        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)