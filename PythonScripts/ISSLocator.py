import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)
print(response.json())
response.raise_for_status()
data = response.json()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
issPosition = (latitude, longitude)
print(issPosition)


#
# # get quote from api
# response = requests.get("https://api.kanye.rest/")
# print(response.json())
#
# quote = response.json()["quote"]
# print(quote)