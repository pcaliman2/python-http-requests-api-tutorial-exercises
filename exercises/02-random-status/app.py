import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")
respuesta = response.status_code
#print(respuesta)

if (respuesta== 404):
    print("The URL you asked for is not found")
elif (respuesta== 503):
    print("Unavailable right now")
elif (respuesta== 200):
    print("Everything went perfect")
elif (respuesta== 400):
    print("Something is wrong with the request params")
else:
    print("Unknown status code")
