import requests
import json

response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
#Datos = json.loads(response.text)
respuesta = response.status_code

if (respuesta==200):
    Datos = response.json()
    PrimerPost = Datos["posts"][0]["author"]["name"]
    #Nombrre = PrimerPost["name"]
    #url_UltimaImagen = ImagenesCurso[-1]
    print(PrimerPost)
else:
    print("Something went wrong")


