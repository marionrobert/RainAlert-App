import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "ac7e8f309ee54b11ec52b72fb0396f04"
LAT = 48.691280
LONG = 2.376180
weather_params = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "alerts,daily,current,minutely"
}



response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
twelve_hours = data["hourly"][:12]
all_ids = [hour['weather'][0]['id'] for hour in twelve_hours]


will_rain = False

for id in all_ids:
    if id < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_=test_phone_number,
        to=my_phone_number
    )
    print(message.status)

