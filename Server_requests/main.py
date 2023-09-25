# importing the requests library
import requests

# api-endpoint
URL = "https://jsonplaceholder.typicode.com/photos"

albumId = 1

# defining a params dict for the parameters to be sent to the API
PARAMS = {'albumId': albumId}

# sending get request and saving the response as response object
server_response = requests.get(url=URL, params=PARAMS)

# extracting data in json format
data = server_response.json()

filtered_data = list(filter(lambda it: it['id'] == 12, data))

print(filtered_data)
