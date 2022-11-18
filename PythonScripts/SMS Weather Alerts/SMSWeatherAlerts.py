import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/
# https://www.ventusky.com/?p=19.49;86.19;6&l=rain-3h
# https://www.latlong.net/

CURRENT_WEATHER_URL = 'https://api.openweathermap.org/data/2.5/onecall'
API_KEY = 'bd436f2c93565cad355dfc1d277a797d'

"""
Twilio Creds
"""

account_sid = "AC52eb1f88b3efa2e3bea1bef45afe85f7"
auth_token = "ebca8f37eb881f203e41ad8c8e51a971"

lat = 22.572645
lon = 88.363892
part = ''

data = {
    "lat": lat,
    "lon": lon,
    "exclude": "currently,minutely,daily",
    "appid": API_KEY
}


response = requests.get(url=CURRENT_WEATHER_URL,
                        params=data)
response.raise_for_status()
data = response.json()
print(data)
hourly = data['hourly']
print(hourly)

will_rain = False
for hour in hourly[:12]:
    weather = hour["weather"]
    weather_id = weather[0]['id']
    if int(weather_id) < 700:
        will_rain = True


if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token)
    message = client.messages\
        .create(body='Its likely to rain', from_="+13023065086", to="8439269807")

    print(message.status)
