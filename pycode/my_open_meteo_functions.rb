require 'net/http'
require 'json'

def get_weather(lat, lng)
  url = URI("https://api.open-meteo.com/v1/forecast?latitude=#{lat}&longitude=#{lng}&hourly=temperature_2m,precipitation_probability,rain,weather_code")
  response = Net::HTTP.get(url)
  weather_today = JSON.parse(response)
  weather_today
end

def code2WeatherJP(code)
  case code
  when 0 then "快晴"
  when 1 then "晴れ"
  when 2 then "時々曇り"
  when 3 then "曇り"
  when 45 then "霧"
  when 48 then "霧氷"
  when 51 then "薄い霧雨"
  when 53 then "霧雨"
  when 55 then "濃い霧雨"
  when 56 then "氷点下の薄い霧雨"
  when 57 then "氷点下の濃い霧雨"
  when 61 then "弱い雨"
  when 63 then "雨"
  when 65 then "激しい雨"
  when 66 then "氷点下の弱い雨"
  when 67 then "氷点下の激しい雨"
  when 71 then "弱い雪"
  when 73 then "雪"
  when 75 then "激しい雪"
  when 77 then "霧雪"
  when 80 then "弱いにわか雨"
  when 81 then "にわか雨"
  when 82 then "激しいにわか雨"
  when 85 then "弱いにわか雪"
  when 86 then "激しいにわか雪"
  when 95 then "雷雨"
  when 96 then "雹を伴う雷雨"
  when 99 then "雹を伴う激しい雷雨"
  else "未定義"
  end
end

def code2Weather(code)
  case code
  when 0 then "clear"
  when 1 then "sunny"
  when 2 then "partly cloudy"
  when 3 then "cloudy"
  when 45 then "fog"
  when 48 then "freezing fog"
  when 51 then "light drizzle"
  when 53 then "drizzle"
  when 55 then "dense drizzle"
  when 56 then "light freezing drizzle"
  when 57 then "dense freezing drizzle"
  when 61 then "slight rain"
  when 63 then "rain"
  when 65 then "heavy rain"
  when 66 then "light freezing rain"
  when 67 then "heavy freezing rain"
  when 71 then "slight snow falls"
  when 73 then "snow falls"
  when 75 then "heavy snow falls"
  when 77 then "snow grains"
  when 80 then "slight rain showers"
  when 81 then "rain showers"
  when 82 then "heavy rain showers"
  when 85 then "slight snow showers"
  when 86 then "heavy snow showers"
  when 95 then "thunderstorm"
  when 96 then "thunderstorm with slight hail"
  when 99 then "thunderstorm with heavy hail"
  else "undefined"
  end
end

def main
  lat = 35.6895  # Example latitude for Tokyo
  lng = 139.6917 # Example longitude for Tokyo
  weather_data = get_weather(lat, lng)
  puts weather_data
end

if __FILE__ == $0
  main
end