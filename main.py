import requests
from twilio.rest import Client
import os
# line for pythonanywhere to connect to proxy server
# from twilio.http.http_client import TwilioHttpClient


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ["OWM_API_KEY"]
LAT = 48.691280
LONG = 2.376180
weather_params = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "alerts,daily,current,minutely"
}

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
twilio_phone_number = os.environ["TWILIO_PHONE_NUMBER"]
my_phone_number = os.environ["MY_PHONE_NUMBER"]

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
    # add the 3 lines below for pythonanywhere to connect to proxy server
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_=twilio_phone_number,
        to=my_phone_number
    )
    print(message.status)

