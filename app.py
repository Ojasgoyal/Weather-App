from flask import Flask, render_template, request, jsonify
import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError("API_KEY environment variable not set.")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

def get_weather(city,country):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city},{country}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ConnectionError(f"Error: Received status code {response.status_code}")
    return response.json()


@app.route('/weather', methods=['GET', 'POST'])
def weather():
    city = request.args.get('city')
    country = request.args.get('country')
    if not city or not country:
        return jsonify({"error": "City or country not provided"}), 400

    try:
        data = get_weather(city, country)
        if "error" in data:
            return jsonify({"error": "Could not fetch weather data"}), 404
        
        weather_data = {
            "location": f"{data['location']['name']}, {data['location']['country']}",
            "temperature": data['current']['temp_c'],
            "weather": data['current']['condition']['text'],
            "icon": data['current']['condition']['icon'],
        }
        return jsonify(weather_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(debug=True)