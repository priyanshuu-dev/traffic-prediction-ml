import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import pickle

df = pd.read_csv("traffic_prediction_dataset.csv")

label_encoder_weather = LabelEncoder()
label_encoder_city = LabelEncoder()
label_encoder_road = LabelEncoder()
label_encoder_target = LabelEncoder()

df["weather_main"] = label_encoder_weather.fit_transform(df["weather_main"])
df["city"] = label_encoder_city.fit_transform(df["city"])
df["road_condition"] = label_encoder_road.fit_transform(df["road_condition"])
df["congestion_level"] = label_encoder_target.fit_transform(df["congestion_level"])

days = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

df["day"] = df["day"].map(days)

X = df[
    [
        "city",
        "hour",
        "day",
        "is_weekend",
        "temp",
        "rain_1h",
        "clouds_all",
        "weather_main",
        "holiday",
        "road_condition",
        "traffic_signal_delay"
    ]
]

y = df["congestion_level"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

data = {
    "model": model,
    "city_encoder": label_encoder_city,
    "weather_encoder": label_encoder_weather,
    "road_encoder": label_encoder_road,
    "target_encoder": label_encoder_target
}

with open("traffic_model.pkl", "wb") as f:
    pickle.dump(data, f)

print("Model Saved Successfully!")