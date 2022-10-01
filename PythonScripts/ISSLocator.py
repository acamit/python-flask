import smtplib

import requests
from datetime import datetime

MY_LATITUDE = 31.633980
MY_LONGITUDE = 74.872261

ISS_LOCATION_URL = 'http://api.open-notify.org/iss-now.json'
SUNRISE_SUNSET_URL = 'https://api.sunrise-sunset.org/json'

MY_EMAIL = "acamit84@gmail.com"
MY_PASSWORD = "fclskebcykqhuuce"

parameters = dict(lat=MY_LATITUDE, lng=MY_LONGITUDE, formatted=0)


def is_iss_overhead():
    response = requests.get(url=ISS_LOCATION_URL)
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # issPosition = (ISS_latitude, ISS_longitude)
    # print(issPosition)
    if MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE + 5 \
            and MY_LONGITUDE - 5 <= iss_longitude <= MY_LATITUDE + 5:
        return True


def is_night():
    data = requests.get(SUNRISE_SUNSET_URL, params=parameters).json()
    sunrise = int(data["results"]['sunrise'].split("T")[1].split(':')[0])
    sunset = int(data["results"]['sunset'].split("T")[1].split(':')[0])
    print(sunrise, sunset)
    time_now = datetime.now()
    current_hour = time_now.hour
    if current_hour >= sunset or current_hour <= sunrise:
        return True


def send_iis_alert(visible=True):
    message = f"Subject: IIS is now visible \n\n IIS is visible now in your location. Current_date {datetime.now()}"
    if not visible:
        message = f"Subject: IIS is not visible \n\n IIS is not yet visible"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=message
        )


if is_night() and is_iss_overhead():
    send_iis_alert()
else:
    send_iis_alert(False)
