import requests

url = "https://assets.breatheco.de/apis/fake/sample/random-status.php"
response = requests.get(url)
respuesta = response.status_code

if (respuesta==200):
    print(response.text) 
else:
    print("Something went wrong")