import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "ac7e8f309ee54b11ec52b72fb0396f04"
LAT = 48.69
LONG = 2.37
params = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "alerts,daily,current,minutely"
}
# https://api.openweathermap.org/data/2.5/onecall?lat=48.69&lon=2.37&exclude=alerts,daily,current,minutely&appid=ac7e8f309ee54b11ec52b72fb0396f04

response = requests.get(OWM_Endpoint, params)
response.raise_for_status()
# print(response.status_code)
data = response.json()
print(data)
