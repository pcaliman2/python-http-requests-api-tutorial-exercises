import requests
import json

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")
#Datos = json.loads(response.text)
respuesta = response.status_code

if (respuesta==200):
    Datos = response.json()
    UltimoProyecto = Datos[(len(Datos))-1]
    ImagenesCurso = UltimoProyecto["images"]
    url_UltimaImagen = last_project["images"][-1]
    print(url_UltimaImagen)
else:
    print("Something went wrong")





