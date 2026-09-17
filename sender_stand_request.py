import configuration
import requests
import data

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)

def post_new_client_kit(kit_body, auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         # Se escriben los headers aquí en lugar de en "data" para
                         # poder incluir el token al ser un argumento
                         headers= {"Content-Type": "application/json",
                                 "Authorization": "Bearer " + auth_token})
