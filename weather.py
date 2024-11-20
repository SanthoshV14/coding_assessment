import requests
import requests
import base64
from datetime import datetime

def kelvin_to_fahrenheit(temp):
    return f"{((9/5) * (temp - 273.15) + 32):.2f}"

def get_weather(city):
    ak = base64.b64decode(b"ODM0ZDQyY2UzZjEzZGM3ZGRiNTQyYzBkZGVhNjNiYzk=").decode("ascii")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={ak}"
    response = requests.get(url)
    response = response.json()

    print("---------------------------------")
    print(f"Weather in {city.capitalize()}")
    print("---------------------------------")
    print(f"- Description: {response['weather'][0]['description'].capitalize()}")
    print(f"- Temperature: {kelvin_to_fahrenheit(response['main']['temp'])} 'F")
    print(f"- Feels-like: {kelvin_to_fahrenheit(response['main']['feels_like'])} 'F")
    print(f"- Low: {kelvin_to_fahrenheit(response['main']['temp_min'])} 'F")
    print(f"- High: {kelvin_to_fahrenheit(response['main']['temp_max'])} 'F")
    print(f"- Pressure: {(response['main']['pressure'] * 0.02953):.2f} inHg")
    print(f"- Humidity: {response['main']['humidity']}%")
    print(f"- Sunrise: {datetime.fromtimestamp(response['sys']['sunrise']).strftime('%I:%M %p')}")
    print(f"- Sunset: {datetime.fromtimestamp(response['sys']['sunset']).strftime('%I:%M %p')}")
    print()
    
def add_fav(city):
    if len(city)==0:
        print("City name is empty")
        return

    if len(favorites)<3 and city not in favorites:
        favorites.append(city)
        print(f"{city} added to favorites.\n")
    else:
        print(f"favorites is full or city already in favorites.\n")

def remove_fav(city):
    if len(favorites)==0:
        print("Favorites is empty.\n")
        return
    
    if len(city)==0:
        print("City name is empty")
        return

    if city in favorites:
        favorites.remove(city)
        print(f"{city} removed from favorites.\n")
    else:
        print(f"{city} not in favorites.\n")
        
def print_fav():
    if len(favorites)>0:
        for i, city in enumerate(favorites):
            print(f"{i+1}. {city}")
        print()
    else:
        print("Favorites is empty.\n")


instructions = """
--------------------------------------------------
                Instructions
--------------------------------------------------
1. -w <city-name> - Get weather details of a city
2. -a <city-name> - Add city to favorites
3. -r <city-name> - Add city from favorites
4. -l - Print the favorite list
5. -e - Exit
--------------------------------------------------
"""
favorites = []

if __name__=="__main__":
    print(instructions)

    while True:
        cmd_input = input("Enter your input: ")
        cmd_input = cmd_input.lower()
        cmd = cmd_input[:3].strip()

        if cmd == "-w":
            city = cmd_input[3:].strip()
            get_weather(city)
        
        elif cmd == "-a":
            city = cmd_input[3:].strip()
            add_fav(city)

        elif cmd == "-r":
            city = cmd_input[3:].strip()
            remove_fav(city)

        elif cmd == "-l":
            print_fav()

        elif cmd == "-e":
            print("Exiting program.\n")
            break
        else:
            print("Unknown command.\n")