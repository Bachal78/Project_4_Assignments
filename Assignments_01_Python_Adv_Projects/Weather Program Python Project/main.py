import requests
from pprint import pprint


API_Key= "cb771e45ac79a4e8e2205c0ce66ff633"
city = input("Enter the city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&units=metric"
response = requests.get(url).json()
pprint(response)