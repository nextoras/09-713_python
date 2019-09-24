import requests

url = "https://new.timerman.org/api/v1/events"

response = requests.get(url)

data = response.json()

print(data)