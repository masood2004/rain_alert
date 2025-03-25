import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


MY_LAT = os.environ.get("MY_LAT")
MY_LONG = os.environ.get("MY_LONG")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
account_sid = os.environ.get("ACCOUNT_SID")
appId = os.environ.get("OWM_APP_ID")
client = Client(account_sid, auth_token)

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": appId,
    "cnt": 4,
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)

response.raise_for_status()

data = response.json()


for n in range(0, 4):
    if (data["list"][n]["weather"][0]["id"]) < 700:
        message = client.messages.create(
            body="It's going to rain today. Be careful about your electronic devices 📱 and motorbike 🚲.",
            from_='whatsapp:+14155238886',
            to='whatsapp:+923103288291'
        )
        print(message.status)
        break
