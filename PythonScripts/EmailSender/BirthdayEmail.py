import datetime as dt
import random
import smtplib

import pandas as pd
# from datetime import datetime.
today = dt.datetime.now()
today_tuple = (today.month, today.day)

MY_EMAIL = "acamit84@gmail.com"
MY_PASSWORD = "radha@Soami1"

data = pd.read_csv('birthdays.csv')

# birthday_dict = {
#     (birthday_month, birthday_day): data_row
# }

birthday_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()
}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]

    # randomly select the template.
    file_path = f'letter_templates/letter_{random.randint(1, 3)}.txt'

    # read the test
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
    # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday! \n\n {contents}"
        )
