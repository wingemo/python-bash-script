#import the necessary package!
import requests

#input the city name
city = 'Stockholm'

#fetch the weater details
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

#display the result!
print(res.text)