import requests
import json

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project1.php")
Datos = json.loads(response.text)

Nombre_Curso = Datos["name"]
respuesta = response.status_code

if (respuesta==200):
    print(Nombre_Curso) 
else:
    print("Something went wrong")