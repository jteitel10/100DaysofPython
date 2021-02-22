import requests
from datetime import datetime

#TOKEN=your token here
#USERNAME = your account here
#GRAPH_ID = graph name here

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"

}

#response = requests.post(url=pixela_endpoint,json=user_params)
#print(response.text)

graph_params = {
    "id": "graph1",
    "name": "Reading graph",
    "unit": "pages",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN" : TOKEN,
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#response=requests.post(url=graph_endpoint, json=graph_params, headers=headers)
#print(response.text)

today = datetime.now().strftime("%Y%m%d")

pixel_params = {
    "date": today,
    "quantity": "10",
}

#response=requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}", json=pixel_params, headers=headers)


update_params = {
    "quantity" : "20",
}
#response=requests.put(url=f"{graph_endpoint}/{GRAPH_ID}/20210220", headers=headers, json=update_params)
#print(response.text)

response=requests.delete(url=f"{graph_endpoint}/{GRAPH_ID}/20210220", headers=headers)
print(response.text)
