import requests

API_KEY = "26e1ec51a1b9d34eb4b42f0e520f6fea"
def get_data(place, forcast_days=None, kind=None):
    url =f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8*forcast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    get_data()