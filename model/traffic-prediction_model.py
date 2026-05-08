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


df["weather_main"] = label_encoder_weather.fit_transform(
    df["weather_main"]
)

df["city"] = label_encoder_city.fit_transform(
    df["city"]
)

df["road_condition"] = label_encoder_road.fit_transform(
    df["road_condition"]
)

df["congestion_level"] = label_encoder_target.fit_transform(
    df["congestion_level"]
)


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


X = df[[
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
]]


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


print("\nModel Accuracy:", round(accuracy, 2))


with open("traffic_model.pkl", "wb") as f:
    pickle.dump(model, f)


print("\nModel Saved Successfully!")


print("\n===== TRAFFIC PREDICTION =====")


print("\nAvailable Cities:")

for city in label_encoder_city.classes_:
    print(city)


city = input(
    "\nEnter City: "
).strip().title()


while city not in label_encoder_city.classes_:

    print("\nInvalid City!")

    city = input(
        "Enter City Again: "
    ).strip().title()


hour = int(input("\nEnter Hour (0-23): "))

day = int(input("Enter Day (0=Monday, 6=Sunday): "))


if day >= 5:
    is_weekend = 1
else:
    is_weekend = 0


temp = float(
    input("Enter Temperature in Celsius: ")
)


rain = float(input("Enter Rain Amount: "))

clouds = int(input("Enter Cloud Percentage: "))


print("\nWeather Options:")

for option in label_encoder_weather.classes_:
    print(option)


weather = input(
    "\nEnter Weather Type: "
).strip().title()


while weather not in label_encoder_weather.classes_:

    print("\nInvalid Weather Type!")

    weather = input(
        "Enter Weather Type Again: "
    ).strip().title()


holiday = int(
    input("Holiday? (0 = No, 1 = Yes): ")
)


print("\nRoad Conditions:")

for option in label_encoder_road.classes_:
    print(option)


road = input(
    "\nEnter Road Condition: "
).strip().title()


while road not in label_encoder_road.classes_:

    print("\nInvalid Road Condition!")

    road = input(
        "Enter Road Condition Again: "
    ).strip().title()


traffic_signal_delay = int(
    input("Enter Traffic Signal Delay: ")
)


city_encoded = label_encoder_city.transform(
    [city]
)[0]

weather_encoded = label_encoder_weather.transform(
    [weather]
)[0]

road_encoded = label_encoder_road.transform(
    [road]
)[0]


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
    "traffic_signal_delay": traffic_signal_delay
}])


prediction = model.predict(sample)[0]


level = label_encoder_target.inverse_transform(
    [prediction]
)[0]


print("\nUSER INPUT DATA")

print("City:", city)
print("Hour:", hour)
print("Day:", day)
print("Temperature:", temp)
print("Rain Amount:", rain)
print("Cloud Percentage:", clouds)
print("Weather:", weather)
print("Holiday:", holiday)
print("Road Condition:", road)
print("Traffic Signal Delay:", traffic_signal_delay)


print("\nPredicted Traffic Level:", level)