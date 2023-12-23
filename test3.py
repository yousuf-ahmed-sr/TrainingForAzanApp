import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can change the units to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad requests

        # Ensure the response content is decoded using UTF-8
        data = response.content.decode('utf-8')

        # Convert the JSON string to a Python dictionary
        data = eval(data)

        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Description: {data['weather'][0]['description']}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with the actual API key you obtained from OpenWeatherMap
    api_key = 'YOUR_API_KEY'
    
    city = input("Enter the city name: ")
    get_weather(api_key, city)
