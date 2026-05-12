import os

import requests


URL = "http://api.weatherapi.com/v1/current.json?"
AQI = "no"
API_KEY = os.getenv("API_KEY")
FILTERING = "Paris"


def get_weather() -> None:
    response = requests.get(URL + f"key={API_KEY}&q={FILTERING}&aqi={AQI}")
    location = response.json()["location"]
    current = response.json()["current"]

    print(f"{location["name"]}/{location["country"]} {location["localtime"]} "
          f"Weather: {current["temp_c"]} Celsius, "
          f"{current["condition"]["text"]}")


if __name__ == "__main__":
    get_weather()
