import requests

response = requests.post("https://assets.breatheco.de/apis/fake/sample/save-project-json.php")


data = {
    "id": 2323,
    "title": "Very big project"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers=headers)
print(response.text)