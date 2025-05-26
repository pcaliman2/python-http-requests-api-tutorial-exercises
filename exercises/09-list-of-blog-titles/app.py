import requests

def get_titles():
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    respuesta = response.status_code
    ListaTitulos= []

    if (respuesta==200):

        Datos = response.json()
        largo = len(Datos["posts"])
        for x in range(largo):
            PrimerPost = Datos["posts"][x]["title"]
            ListaTitulos.append(PrimerPost)
    else:
        print("Something went wrong")
    return ListaTitulos


print(get_titles())




