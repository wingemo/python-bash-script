#import the necessary package!
import requests
import json

WMO = {
  0: "Clear sky",
  1: "Mainly clear",
  2: "partly cloudy"
}

#input the city name
city = 'Stockholm'

#fetch the weater details
url = 'https://api.open-meteo.com/v1/forecast?latitude=59.36&longitude=18.26&current_weather=true&timezone=Europe%2FBerlin'
res = requests.get(url)
b = json.loads(res.text)
#display the result!

print(WMO[b['current_weather']['weathercode']])
print(b['current_weather']['temperature'])
