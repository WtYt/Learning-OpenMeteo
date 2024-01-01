import requests

def get_weather(lat, lng):
    url = "https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) + "&longitude=" + str(lng) + "&hourly=temperature_2m,precipitation_probability,rain,weather_code"
    weather_today = requests.get(url).json()

    return(weather_today)
