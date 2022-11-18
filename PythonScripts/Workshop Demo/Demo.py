"""
Automated Birthday wisher.
1. Create an Excel file for birthdays
2. Read from excel every day at 12:00 am. If there is any birthday today send email and sms.

For email - Using python's library and gmail account.
For SMS use Twilio API

Link to generate app passwords
https://support.google.com/accounts/answer/185833?hl=en


Link to set up twilio account
https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account

For python anywhere
https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/
"""
import os

# python libraries
import pandas as pd
import datetime as dt
import random

# email library and configs
import smtplib
from config import MY_EMAIL, MY_PASSWORD

# SMS imports
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from config import TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID, TWILIO_TEMP_NUMBER


# Step 1  Read csv file
today = dt.datetime.now()

birthdays = pd.read_csv("birthdays.csv")

# get rows with birthday as today.
birthdays_today = birthdays[(birthdays['month'] == today.month) & (birthdays['day'] == today.day)]


def send_greetings(row):
    message = get_message(row)

    # Send Email
    send_email(message, row)

    # Send Text message
    send_text_message(message, row)

    # ToDO send whatsapp messages


def get_message(row):
    name = row['name']
    # get a wish template
    template_path = f'message_templates/message{random.randint(1, 3)}.txt'
    with open(template_path) as template:
        message = template.read()
        message = message.replace('[NAME]', name)
    return message


def send_email(message, row):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=row['email'],
                            msg=f'Subject: Happy Birthday! \n\n {message}'
                            )


def send_text_message(message, row):
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, http_client=proxy_client)
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    t_message = client.messages.create(body=message, from_=TWILIO_TEMP_NUMBER, to=row['phone'])
    print(t_message.status)


print(birthdays_today.apply(send_greetings, axis=1))

