import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
print(response.text)

hora=17
minutos=06
segundos=23

print(f'Current time: {hora} hrs {minutos} min and {segundos} sec')

