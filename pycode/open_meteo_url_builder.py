import math
import coordinates_searcher as csrch

class MeteoURLBuilder: # easily created, not completed fully.

    def __init__(self):
        self.url = "https://api.open-meteo.com/v1/forecast"
        self.latitude  = float("nan")   # as a null number
        self.longitude = float("nan")   # as a null number
        self.hourly_parameters  = []    # should create Parameter class?
        self.daily_parameters   = []
        self.current_parameters = []
        self.timezone           = None

    def __init__(self, x:float, y:float):
        self.url = "https://api.open-meteo.com/v1/forecast"
        self.latitude  = y
        self.longitude = x
        self.hourly_parameters  = []
        self.daily_parameters   = []
        self.current_parameters = []
        self.timezone           = None

    def setLongitude(self, x:float):
        self.longitude = x

    def setLatitude(self, y:float):
        self.latitude  = y

    def setTimeZone(self, timezone:str):
        self.timezone = timezone

    def addParameter(self, parameter:str): # unused. useful for generalization?
        pass

    def addHourlyParameter(self, parameter:str):
        self.hourly_parameters.append(parameter)

    def addDailyParameter(self, parameter:str):
        self.daily_parameters.append(parameter)

    def addCurrentParameter(self, parameter:str):
        self.current_parameters.append(parameter)

    def buildUrl(self) -> str:
        if math.isnan(self.latitude) or math.isnan(self.longitude):
            return None
        url =  self.url + "?longitude={:.4f}&latitude={:.4f}".format(self.longitude, self.latitude)
        if self.hourly_parameters:
            url += "&hourly="
            i = 1
            for parameter in self.hourly_parameters:
                url += parameter
                if i < len(self.hourly_parameters):
                    url += ","
                i += 1
        if self.daily_parameters:
            url += "&daily="
            i = 1
            for parameter in self.daily_parameters:
                url += parameter
                if i < len(self.daily_parameters):
                    url += ","
                i += 1
        if self.current_parameters:
            url += "&current="
            i = 1
            for parameter in self.current_parameters:
                url += parameter
                if i < len(self.current_parameters):
                    url += ","
                i += 1
        if self.timezone:
            url += "&timezone=" + self.timezone
        return url

def code2WeatherJP(code:int) -> str:
    if   code == 0:
        return "快晴"
    elif code == 1:
        return "晴れ"
    elif code == 2:
        return "時々曇り"
    elif code == 3:
        return "曇り"
    elif code == 45:
        return "霧"
    elif code == 48:
        return "霧氷"
    elif code == 51:
        return "薄い霧雨"
    elif code == 53:
        return "霧雨"
    elif code == 55:
        return "濃い霧雨"
    elif code == 56:
        return "氷点下の薄い霧雨"
    elif code == 57:
        return "氷点下の濃い霧雨"
    elif code == 61:
        return "弱い雨"
    elif code == 63:
        return "雨"
    elif code == 65:
        return "激しい雨"
    elif code == 66:
        return "氷点下の弱い雨"
    elif code == 67:
        return "氷点下の激しい雨"
    elif code == 71:
        return "弱い雪"
    elif code == 73:
        return "雪"
    elif code == 75:
        return "激しい雪"
    elif code == 77:
        return "霧雪"
    elif code == 80:
        return "弱いにわか雨"
    elif code == 81:
        return "にわか雨"
    elif code == 82:
        return "激しいにわか雨"
    elif code == 85:
        return "弱いにわか雪"
    elif code == 86:
        return "激しいにわか雪"
    elif code == 95:
        return "雷雨"
    elif code == 96:
        return "雹を伴う雷雨"
    elif code == 99:
        return "雹を伴う激しい雷雨"
    else:
        return "未定義"

def code2Weather(code:int) -> str:
    if   code == 0:
        return "clear"
    elif code == 1:
        return "sunny"
    elif code == 2:
        return "partly cloudy"
    elif code == 3:
        return "cloudy"
    elif code == 45:
        return "fog"
    elif code == 48:
        return "freezing fog"
    elif code == 51:
        return "light drizzle"
    elif code == 53:
        return "drizzle"
    elif code == 55:
        return "dense drizzle"
    elif code == 56:
        return "light freezing drizzle"
    elif code == 57:
        return "dense freezing drizzle"
    elif code == 61:
        return "slight rain"
    elif code == 63:
        return "rain"
    elif code == 65:
        return "heavy rain"
    elif code == 66:
        return "light freezing rain"
    elif code == 67:
        return "heavy freezing rain"
    elif code == 71:
        return "slight snow falls"
    elif code == 73:
        return "snow falls"
    elif code == 75:
        return "heavy snow falls"
    elif code == 77:
        return "snow grains"
    elif code == 80:
        return "slight rain showers"
    elif code == 81:
        return "rain showers"
    elif code == 82:
        return "heavy rain showers"
    elif code == 85:
        return "slight snow showers"
    elif code == 86:
        return "heavy snow showers"
    elif code == 95:
        return "thunderstorm"
    elif code == 96:
        return "thunderstorm with slight hail"
    elif code == 99:
        return "thunderstorm with heavy hail"
    else:
        return "undefined"

def main():
    word = "江東区"
    coordinates = csrch.get_coordinates(word)
    print(word + "->" + coordinates[2])
    murlbld = MeteoURLBuilder(coordinates[0], coordinates[1])
    murlbld.addHourlyParameter("temperature_2m")
    #print("t")
    murlbld.addHourlyParameter("weather_code")
    #print("w")
    murlbld.setTimeZone("Asia%2FTokyo")
    url = murlbld.buildUrl()
    print(url)

if __name__ == "__main__":
    main()
