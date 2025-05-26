import requests

url = "https://assets.breatheco.de/apis/fake/sample/save-project-json.php"

Datos = {
    "id": 2323,
    "title": "Very big project"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=Datos, headers=headers)
print(response.text)