# AI Traffic Prediction System 🚦

An AI-powered traffic congestion prediction dashboard built using Python, Flask, XGBoost, HTML, CSS, and JavaScript.

This system predicts traffic congestion levels based on multiple real-world parameters like weather conditions, rainfall, cloud density, road condition, signal delay, time, and city data.

---

## ✨ Features

- AI-based Traffic Prediction
- Dynamic Congestion Detection
- Animated Traffic Status Ring
- Real-time Weather Impact UI
- AI Traffic Insight Panel
- Responsive Dashboard Design
- Modern Glassmorphism UI
- XGBoost Machine Learning Model

---

## 🧠 Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- XGBoost
- Pandas
- NumPy

---

## 📂 Project Structure

```txt
Traffic-Prediction-System/
│
├── app.py
├── model.py
├── traffic_model.pkl
├── traffic_prediction_dataset.csv
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── image.png
│
└── screenshots/
    ├── low.png
    ├── medium.png
    └── high.png
```

---

## 📸 Screenshots

### 🟢 Low Traffic Prediction

![Low Traffic](screenshots/low.png)

---

### 🟡 Medium Traffic Prediction

![Medium Traffic](screenshots/medium.png)

---

### 🔴 High Traffic Prediction

![High Traffic](screenshots/high.png)

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Traffic-Prediction-System.git
```

Open project folder:

```bash
cd Traffic-Prediction-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask server:

```bash
python app.py
```

---

## 🚀 How It Works

The system takes user input such as:

- City
- Time
- Day
- Temperature
- Rainfall
- Cloud Percentage
- Weather Condition
- Road Condition
- Signal Delay

The trained XGBoost model then predicts traffic congestion as:

- LOW
- MEDIUM
- HIGH

The frontend dynamically updates:
- Traffic Ring
- AI Insight
- Weather Impact
- Congestion Status
- Probability Score

---

## 📊 Machine Learning Model

The project uses an XGBoost Classifier trained on traffic and weather-related features.

### Input Features
- City
- Hour
- Day
- Weekend
- Temperature
- Rainfall
- Clouds
- Weather Type
- Holiday
- Road Condition
- Signal Delay

### Output
- Traffic Congestion Level

---

## 👨‍💻 Author

Priyanshu

GitHub: https://github.com/priyanshuu-dev

---

## ⭐ Future Improvements

- Live Weather API Integration
- Real-time Traffic Map
- Route Optimization
- Deployment Support
- Historical Traffic Analytics
- Mobile Responsive Enhancements

---

## 📜 License

This project is open-source and available for educational purposes.
