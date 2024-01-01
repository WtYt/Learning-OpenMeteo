import requests

def get_weather(lat, lng):
    url = "https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) + "&longitude=" + str(lng) + "&hourly=weathercode&forecast_days=1&timezone=Asia%2FTokyo"
    weather_today = requests.get(url).json()

    return(weather_today)
