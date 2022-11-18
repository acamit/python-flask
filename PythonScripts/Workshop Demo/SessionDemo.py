"""
Automated Birthday Wisher

For email - Using python's library and gmail account.
For SMS use Twilio API
For Whatsapp messages -
"""
import random

import pandas as pd
import datetime as dt
import os

import smtplib

from config import MY_EMAIL, MY_PASSWORD


from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from config import TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID, TWILIO_TEMP_NUMBER

today = dt.datetime.now()
print(today)
birthdays = pd.read_csv("birthdays.csv")

birthdays_today = birthdays[(birthdays['month'] == today.month) & (birthdays['day'] == today.day)]
print(birthdays_today)


def send_greetings(row):
    print(row)
    # get a message
    message = get_message(row)
    # send email
    email = row['email']
    send_email(message, email)

    # send text message
    send_text_message(message, row['phone'])

    #     send whatsapp messsage
    #       send HTML Email


def get_message(row):
    name = row['name']
    template_path = f'message_templates/message{random.randint(1, 3)}.txt'
    with open(template_path) as template:
        message = template.read()
        message = message.replace('[NAME]', name)
    return message


def send_email(message, email):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=email,
                            msg=f'Subject: Happy Birthday! \n\n {message}'
                            )


def send_text_message(message, phone_num):
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, http_client=proxy_client)
    t_message = client.messages.create(body=message, from_=TWILIO_TEMP_NUMBER, to=phone_num)
    print(t_message.status)


birthdays_today.apply(send_greetings, axis=1)


