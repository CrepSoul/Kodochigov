import requests
from datetime import datetime

city = "Moscow,RU"
appid = "2d854e3b2d35cbf405c2bca746be8e7a"

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
now = res.json()
print("Город:", city)
print("\n")
print("Скорость ветра сейчас:", now['wind']['speed'])
print("Видимость сейчас:", now['visibility'])
print("\n")

res = requests.get("https://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
week = res.json()
for i in range(1, 40, 8):
    print("Дата: ", datetime.utcfromtimestamp(week['list'][i]['dt']).strftime('%d.%m.%Y'))
    print("Скорость ветра:", week['list'][i]['wind']['speed'])
    print("Видимость:", week['list'][i]['visibility'])
    print("\n")
