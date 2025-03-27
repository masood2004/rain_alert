import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch necessary environment variables
MY_LAT = os.getenv("MY_LAT")
MY_LONG = os.getenv("MY_LONG")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
account_sid = os.getenv("ACCOUNT_SID")
appId = os.getenv("OWM_APP_ID")

# Check if necessary variables are set
if not all([MY_LAT, MY_LONG, auth_token, account_sid, appId]):
    raise ValueError("One or more environment variables are missing")

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Weather API parameters
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": appId,
    "cnt": 4,  # 4-day forecast
}

# Get the weather forecast
try:
    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    response.raise_for_status()  # Raises HTTPError for bad responses
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")
    exit(1)

# Function to send a message via Twilio WhatsApp
def send_message(body):
    try:
        message = client.messages.create(
            body=body,
            from_='whatsapp:+14155238886',
            to='whatsapp:+923103288291'
        )
        print(f"Message sent: {message.status}")
    except Exception as e:
        print(f"Error sending message: {e}")

# Check if it's going to rain (weather condition id < 700)
RAIN_THRESHOLD = 700
rain_expected = False

# Loop over the next 4 forecast periods
for forecast in data["list"]:
    if forecast["weather"][0]["id"] < RAIN_THRESHOLD:
        rain_expected = True
        break

# Send appropriate message
if rain_expected:
    send_message("It's going to rain today. Be careful about your electronic devices 📱 and motorbike 🚲.")
else:
    send_message("No need to be careful about the weather.")
