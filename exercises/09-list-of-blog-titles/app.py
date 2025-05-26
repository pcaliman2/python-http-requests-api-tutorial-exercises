import requests

def get_titles():
    ListaTitulos= []
    Datos = response.json()
    largo = len(Datos["posts"])
    for x in range(largo):
        PrimerPost = Datos["posts"][x]["title"]
        ListaTitulos.append(PrimerPost)
    #print(ListaTitulos)
    return ListaTitulos



response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
respuesta = response.status_code

if (respuesta==200):
    print(get_titles())
else:
    print("Something went wrong")
