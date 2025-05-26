import requests
import json

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
Tiempo = json.loads(response.text)
#print(Tiempo)

hora= Tiempo["hours"]
minutos=Tiempo["minutes"]
segundos=Tiempo["seconds"]

print(f'Current time: {hora} hrs {minutos} min and {segundos} sec')

