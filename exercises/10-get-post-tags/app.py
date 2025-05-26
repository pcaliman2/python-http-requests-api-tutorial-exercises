import requests
import json

def get_post_tags(post_id):
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    respuesta = response.status_code


    if (respuesta==200):
        Datos = response.json()

        for post in Datos["posts"]:
            if post["id"] == post_id:
                return post["tags"]
        return print("El Post no fue Encontrado") 
    else:
        print("Something went wrong")
    

print(get_post_tags(146))