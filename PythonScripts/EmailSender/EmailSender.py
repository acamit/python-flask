import smtplib

my_email = 'acamit84@gmail.com'

connection = smtplib.SMTP("smtp.gmail.com", port=587)
password = 'fclskebcykqhuuce'
# secure and encrypt the message
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs='amit.chawla0895@gmail.com',
    msg="Subject:hello \n\n This is the body of my email"
)
connection.close()
