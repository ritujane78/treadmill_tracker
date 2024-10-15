import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME= "ritujane78"
TOKEN = "asdf543hedgfti56gddsiwu"
ID = "graph1"

post_json = {
    'token':'asdf543hedgfti56gddsiwu',
    'username': 'ritujane78',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

response= requests.post(url = pixela_endpoint, json= post_json)
print(response.json())

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name" : "Treadmill Graph",
    "unit" : "km",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# today= datetime.now()
today = datetime(year=2024, month=10,  day=11)
formatted_date = today.strftime("%Y%m%d")
print(today.strftime("%Y%m%d"))

pixel_endpoint = f"{graph_endpoint}/{ID}"

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input('How much did you walk?')
}

response = requests.post(url = pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_endpoint = f"{pixel_endpoint}/{formatted_date}"

update_config = {
    "quantity" : "3.1"
}
# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)