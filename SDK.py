
import requests
'''python
from weather_sdk import WeatherAPI

api = WeatherAPI()

# Add a weather record
print(api.add_weather("Paris", 22.5, "Cloudy", "2025-08-14"))

# Get all weather records
print(api.get_all_weather())'''



class WeatherAPI:
    def __init__(self, base_url="http://127.0.0.1:5000"):
        self.base_url = base_url.rstrip('/')

    def get_all_weather(self):
        return requests.get(f"{self.base_url}/weathers").json()

    def get_weather(self, weather_id):
        return requests.get(f"{self.base_url}/weathers/{weather_id}").json()

    def add_weather(self, city, temperature, condition, date):
        data = {
            "city": city,
            "temperature": temperature,
            "condition": condition,
            "date": date
        }
        return requests.post(f"{self.base_url}/weathers", json=data).json()

    def update_weather(self, weather_id, city, temperature, condition, date):
        data = {
            "city": city,
            "temperature": temperature,
            "condition": condition,
            "date": date
        }
        return requests.put(f"{self.base_url}/weathers/{weather_id}", json=data).json()

    def patch_weather(self, weather_id, city=None, temperature=None, condition=None, date=None):
        data = {}
        if city is not None:
            data["city"] = city
        if temperature is not None:
            data["temperature"] = temperature
        if condition is not None:
            data["condition"] = condition
        if date is not None:
            data["date"] = date
        return requests.patch(f"{self.base_url}/weathers/{weather_id}", json=data).json()

    def delete_weather(self, weather_id):
        return requests.delete(f"{self.base_url}/weathers/{weather_id}").json()

    def search_weather(self, query):
        return requests.get(f"{self.base_url}/weather/search", params={"q": query}).json()


if __name__ == "__main__":
    api = WeatherAPI()

    # Example usage
    print(api.add_weather("London", 18.2, "Rainy", "2025-08-13"))
    print(api.search_weather("Rainy"))
````