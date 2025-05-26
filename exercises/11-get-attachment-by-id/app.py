import requests

def get_attachment_by_id(attachment_id):
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    respuesta = response.status_code


    if (respuesta==200):
        Datos = response.json()

        for post in Datos["posts"]:
                for attachment in post["attachments"]:
                    if attachment["id"] == attachment_id:
                        return attachment["title"]
        return print("El Attachment no fue Encontrado") 
    else:
        print("Something went wrong")

print(get_attachment_by_id(137))