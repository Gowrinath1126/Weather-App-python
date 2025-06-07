import requests
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print(Fore.GREEN + f"\n🌍 Weather in {data['name']}, {data['sys']['country']}")
            print(Fore.CYAN + f"🌡️ Temperature: {data['main']['temp']}°C")
            print(Fore.YELLOW + f"☁️ Weather: {data['weather'][0]['description'].title()}")
            print(Fore.BLUE + f"💧 Humidity: {data['main']['humidity']}%")
            print(Fore.MAGENTA + f"💨 Wind Speed: {data['wind']['speed']} m/s")
        else:
            print(Fore.RED + "❌ Error:", data.get("message", "Unknown error"))
    except Exception as e:
        print(Fore.RED + f"⚠️ Something went wrong: {e}")

def main():
    print(Style.BRIGHT + Fore.BLUE + "="*40)
    print(Fore.GREEN + "   🌤️ Python Weather App 🌤️   ")
    print(Style.BRIGHT + Fore.BLUE + "="*40)

    api_key = "9746133775469fbf3085f9386ab55877"  # Replace with your own API key

    while True:
        city = input(Fore.WHITE + "\n🏙️ Enter city name (or 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            print(Fore.GREEN + "👋 Goodbye! Stay safe.")
            break
        elif city == "":
            print(Fore.RED + "⚠️ Please enter a valid city name.")
        else:
            get_weather(city, api_key)

if __name__ == "__main__":
    main()
