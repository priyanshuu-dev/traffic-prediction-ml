import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import pickle


df = pd.read_csv("Metro_Interstate_Traffic_Volume.csv")


df["date_time"] = pd.to_datetime(df["date_time"])


df["hour"] = df["date_time"].dt.hour
df["day"] = df["date_time"].dt.dayofweek


def traffic_level(volume):

    if volume < 1500:
        return 0

    elif volume < 4000:
        return 1

    else:
        return 2


df["traffic_level"] = df["traffic_volume"].apply(
    traffic_level
)


label_encoder_weather = LabelEncoder()


df["weather_main"] = label_encoder_weather.fit_transform(
    df["weather_main"]
)


df["holiday"] = df["holiday"].apply(
    lambda x: 0 if x == "None" else 1
)


X = df[[
    "hour",
    "day",
    "temp",
    "rain_1h",
    "clouds_all",
    "weather_main",
    "holiday"
]]


y = df["traffic_level"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = XGBClassifier(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=8,
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


hour = int(input("Enter Hour (0-23): "))

day = int(input("Enter Day (0=Monday, 6=Sunday): "))


temp_celsius = float(
    input("Enter Temperature in Celsius: ")
)

temp = temp_celsius + 273.15


rain = float(input("Enter Rain Amount: "))

clouds = int(input("Enter Cloud Percentage: "))


print("\nWeather Options:")

for option in label_encoder_weather.classes_:
    print(option)


weather = input(
    "Enter Weather Type: "
).strip().title()


while weather not in label_encoder_weather.classes_:

    print("\nInvalid Weather Type!")

    weather = input(
        "Enter Weather Type Again: "
    ).strip().title()


holiday_input = input(
    "Is it Holiday? (yes/no): "
).strip().lower()


if holiday_input == "yes":
    holiday = 1
else:
    holiday = 0


weather_encoded = label_encoder_weather.transform(
    [weather]
)[0]


sample = pd.DataFrame([{
    "hour": hour,
    "day": day,
    "temp": temp,
    "rain_1h": rain,
    "clouds_all": clouds,
    "weather_main": weather_encoded,
    "holiday": holiday
}])


prediction = model.predict(sample)[0]


if prediction == 0:
    level = "Low"

elif prediction == 1:
    level = "Medium"

else:
    level = "High"


print("\nPredicted Traffic Level:", level)