# Rain Alert System ☔

A Python script that checks the weather forecast and sends automated WhatsApp alerts if rain is detected. Built with OpenWeatherMap API and Twilio integration.

![GitHub last commit](https://img.shields.io/github/last-commit/masood2004/rain_alert?color=blue) ![Python](https://img.shields.io/badge/Python-3.8%2B-yellowgreen) ![License](https://img.shields.io/badge/License-MIT-brightgreen)

## Features ✨

- 🌩️ **Real-Time Weather Monitoring**: Fetches 12-hour weather forecasts using OpenWeatherMap API
- 📲 **WhatsApp Notifications**: Sends instant rain alerts via Twilio's WhatsApp integration
- 🔒 **Secure Configuration**: Uses `.env` file to store sensitive credentials (never committed to Git!)
- 🛠️ **Error Handling**: Built-in HTTP request validation with `response.raise_for_status()`

## Installation 📦

1. Clone the repository:
   ```bash
   git clone https://github.com/masood2004/rain_alert.git
   cd rain_alert
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create `.env` file with your credentials:
   ```ini
   MY_LAT="YOUR_LATITUDE"
   MY_LONG="YOUR_LONGITUDE"
   OWM_APP_ID="your_openweathermap_api_key"
   ACCOUNT_SID="your_twilio_account_sid"
   TWILIO_AUTH_TOKEN="your_twilio_auth_token"
   ```

## Configuration ⚙️

### Required Environment Variables
| Variable            | Description                          |
|---------------------|--------------------------------------|
| `MY_LAT`            | Your latitude (decimal format)       |
| `MY_LONG`           | Your longitude (decimal format)      |
| `OWM_APP_ID`        | OpenWeatherMap API key               |
| `ACCOUNT_SID`       | Twilio Account SID                   |
| `TWILIO_AUTH_TOKEN` | Twilio Authentication Token          |

⚠️ **Important**: Add `.env` to your `.gitignore` to prevent exposing credentials!

## Usage 🚀

1. Ensure you've completed all installation steps
2. Run the script:
   ```bash
   python main.py
   ```
3. If rain is detected in the forecast, you'll receive a WhatsApp message:
   ```
   "It's going to rain today. Be careful about your electronic devices 📱 and motorbike 🚲."
   ```

### Twilio Setup Note
Make sure your Twilio WhatsApp sandbox is properly configured:
- Connect your phone number via Twilio's sandbox instructions
- Use the official sandbox number: `whatsapp:+14155238886`

## Contributing 🤝

Contributions are welcome! Please follow these steps:
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments 🙏

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- SMS services powered by [Twilio](https://www.twilio.com/)
- Python environment management with [python-dotenv](https://pypi.org/project/python-dotenv/)

---

**Stay Dry!** ☂️ Made with ❤️ by [Masood](https://github.com/masood2004)
