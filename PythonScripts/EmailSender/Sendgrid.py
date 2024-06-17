import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("abc@gmail.com")  # Change to your verified sender
to_email = To("abc@gmail.com")  # Change to your recipient
subject = "Upcoming onsite workshop"
content = Content("text/plain", "Hi Everyone,\nAs discussed over the call, we will be conducting an onsite workshop with the clien from July 3, 2024 - July 5,2024. Workshop will be conducted in Gurgaon Plot 13 office. Further detailed agenda will be shared as finalized. All the colleagues will be required to be in office during the visit. Colleagues must be in office by 12 pm Noon on July 3, 2024. Neccessary arrangements for accommodation will be made for collegaes living more than 50Km from the office(as per the existing HR records).\
\n\nThanks and Regards,\nYour name")
mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)
