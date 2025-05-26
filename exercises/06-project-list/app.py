import requests
import json

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")
#Datos = json.loads(response.text)
Datos = response.json()
Nombre_Curso = Datos[1]["name"]

respuesta = response.status_code

if (respuesta==200):
    print(Nombre_Curso) 
else:
    print("Something went wrong")