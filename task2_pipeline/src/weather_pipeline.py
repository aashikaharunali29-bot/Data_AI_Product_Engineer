import requests
import pandas as pd
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# API URL
BASE_URL = "https://api.open-meteo.com/v1/forecast"

# Parameters
params = {
    "latitude": 13.0827,   # Chennai
    "longitude": 80.2707,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

try:
    logging.info("Fetching weather data...")

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        current = data.get("current", {})

        weather_data = {
            "city": "Chennai",
            "temperature": current.get("temperature_2m"),
            "humidity": current.get("relative_humidity_2m"),
            "wind_speed": current.get("wind_speed_10m")
        }

        # Derived field
        weather_data["weather_score"] = (
            weather_data["temperature"] +
            weather_data["humidity"] / 10
        )

        df = pd.DataFrame([weather_data])

        # Save CSV
        df.to_csv("weather_data.csv", index=False)

        logging.info("Data saved successfully!")
        print(df)

    else:
        logging.error(
            f"API request failed: {response.status_code}"
        )

except Exception as e:
    logging.error(f"Error occurred: {e}")