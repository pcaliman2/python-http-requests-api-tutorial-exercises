import requests
import json

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")
#Datos = json.loads(response.text)
Datos = response.json()
NumeroElentos = len(Datos)

last_project = Datos[-1]
#last_image_url = last_project["images"][-1]

ImagenesCurso = last_project["images"]

respuesta = response.status_code
last_image_url = last_project["images"][-1]
if (respuesta==200):
    #print(ImagenesCurso) 
    #print(last_project) 
    print(last_image_url)
else:
    print("Something went wrong")





