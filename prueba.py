import requests

correo = "fabialayola@hotmail.com"

parametros = {"autocorrect": False}


try:
    respuesta = requests.get(f"https://emailvalidation.abstractapi.com/v1/?api_key=e06fb4dd03594ddea485b27d1ade4cc1&email={correo}", params = parametros)
    respuesta.raise_for_status()    
    if respuesta.json()["deliverability"] == "DELIVERABLE":
        print("El correo existe.")
    else:
        print("El correo electrónico ingresado no es válido.")
except:
    print("Hubo un error en la solicitud.")