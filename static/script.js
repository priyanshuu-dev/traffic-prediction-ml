const navTime =
    document.getElementById("nav-time");

const navDate =
    document.getElementById("nav-date");

function updateDateTime(){

    const now = new Date();

    // TIME

    const time =
        now.toLocaleTimeString(
            "en-IN",
            {
                hour: "2-digit",
                minute: "2-digit"
            }
        );

    // DATE

    const date =
        now.toLocaleDateString(
            "en-IN",
            {
                day: "2-digit",
                month: "short",
                year: "numeric"
            }
        );

    navTime.innerText =
        "🕒 " + time;

    navDate.innerText =
        "📅 " + date;
}

updateDateTime();

setInterval(
    updateDateTime,
    1000
);
const form = document.getElementById("prediction-form");

form.addEventListener("submit", async function(e){

    e.preventDefault();

    try{

        const formData = new FormData(form);

        const data =
            Object.fromEntries(formData.entries());

        console.log(data);

        const response = await fetch(
            "http://127.0.0.1:5000/predict",
            {
                method: "POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body: JSON.stringify(data)
            }
        );

        const result = await response.json();

        console.log(result);

        if(result.error){

            alert(result.error);

            return;
        }

        const trafficText =
            document.getElementById("traffic-text");

        const trafficStatus =
            document.getElementById("traffic-status");

        const ring =
            document.getElementById("traffic-ring");

        const badge =
            document.getElementById("traffic-badge");

        const probability =
            document.getElementById("probability-text");

        const peakValue =
            document.getElementById("peak-value");

        const roadStatus =
            document.getElementById("road-status-text");

        const weatherRisk =
            document.getElementById("weather-risk-text");

        const insight =
            document.getElementById("insight-text");

        const weatherTitle =
            document.getElementById("weather-title");

        const weatherEffect =
            document.getElementById("weather-effect");

        const weatherIcon =
            document.getElementById("weather-icon");

        const statusBox =
            document.getElementById("status-box");

        const prediction =
            result.prediction.toLowerCase();

        const weather =
            data.weather_main.toLowerCase();

        ring.classList.remove(
            "low-ring",
            "medium-ring",
            "high-ring"
        );

        trafficText.classList.remove(
            "low-text",
            "medium-text",
            "high-text"
        );

        badge.classList.remove(
            "low",
            "medium",
            "high"
        );

        if(prediction === "low"){

            ring.classList.add("low-ring");

            trafficText.classList.add("low-text");

            badge.classList.add("low");

            trafficStatus.innerText =
                "Smooth Traffic Flow 🟢";

            statusBox.innerText =
                "Smooth Flow";

            insight.innerText =
                "Traffic flow is smooth with minimal congestion risk.";
        }

        else if(prediction === "medium"){

            ring.classList.add("medium-ring");

            trafficText.classList.add("medium-text");

            badge.classList.add("medium");

            trafficStatus.innerText =
                "Moderate Congestion 🟡";

            statusBox.innerText =
                "Moderate Traffic";

            insight.innerText =
                "Moderate vehicle density detected in key routes.";
        }

        else{

            ring.classList.add("high-ring");

            trafficText.classList.add("high-text");

            badge.classList.add("high");

            trafficStatus.innerText =
                "Heavy Traffic Alert 🔴";

            statusBox.innerText =
                "Heavy Traffic";

            insight.innerText =
                "Heavy congestion detected. Alternate routes recommended.";
        }

        trafficText.innerText =
            prediction.toUpperCase();

        badge.innerText =
            prediction.toUpperCase();

        probability.innerText =
            result.confidence + "%";

        const hour =
            Number(data.hour);

        if(hour >= 7 && hour <= 10){

            peakValue.innerText =
                "Morning Rush";
        }

        else if(hour >= 17 && hour <= 20){

            peakValue.innerText =
                "Peak Congestion";
        }

        else{

            peakValue.innerText =
                "Low Traffic Hours";
        }

        roadStatus.innerText =
            data.road_condition;

        if(weather === "rain"){

            weatherRisk.innerText =
                "Heavy Rain Risk 🌧️";

            weatherTitle.innerText =
                "Rain";

            weatherEffect.innerText =
                "Heavy Jam Risk 🌧️";

            weatherIcon.className =
                "ri-heavy-showers-fill";
        }

        else if(weather === "clouds"){

            weatherRisk.innerText =
                "Moderate Impact ☁️";

            weatherTitle.innerText =
                "Clouds";

            weatherEffect.innerText =
                "Moderate Traffic ☁️";

            weatherIcon.className =
                "ri-cloudy-fill";
        }

        else{

            weatherRisk.innerText =
                "Clear Weather ☀️";

            weatherTitle.innerText =
                "Clear";

            weatherEffect.innerText =
                "Low Impact ☀️";

            weatherIcon.className =
                "ri-sun-fill";
        }

    }

    catch(error){

        console.log(error);

        alert("Something Went Wrong");
    }

});