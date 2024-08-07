import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError

BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather(city,country):
    url = f"{BASE_URL}?key={API_KEY}&q={city},{country}"
    response = requests.get(url)
    return response.json()

def main():

    print("*" * 20)
    print("Weather APP")
    print("*" * 20)
    print("To exit the app type exit and press enter\n\n")

    while True:
        try:
            
            city = input("Enter city name: ").lower()
            if city == "exit":
                raise EOFError
            country = input("Enter country name: ").lower()
            if country == "exit":
                raise EOFError
            data = get_weather(city,country)
            
            if "error" in data:
                raise ValueError
            else:
                temp = data['current']['temp_c']
                weather = data['current']['condition']['text']
                print(f"temperature: {temp}°C")
                print(f"weather: {weather}\n")
        except EOFError:
            sys.exit('\nClosing the app')
        except:
            print("Could not fetch weather data")
        


if __name__ == "__main__":
    main()