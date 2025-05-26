import requests
import json

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")
#Datos = json.loads(response.text)
respuesta = response.status_code

if (respuesta==200):
    Datos = response.json()
    NumeroElentos = len(Datos)
    UltimoProyecto = Datos[-1]
    ImagenesCurso = UltimoProyecto["images"]

    elementos = len(UltimoProyecto)
    last_image_url = last_project["images"][-1]
    print(last_image_url)
else:
    print("Something went wrong")





