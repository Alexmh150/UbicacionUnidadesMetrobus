import requests
from pandas import json_normalize

def Consulta(nombre):
    url = "http://127.0.0.1:5000"
    payload="{\"query\":\"{\\r\\n   studentsByName(nomgeo:\\\""+nombre+"\\\") {\\r\\n     nomgeo\\r\\n     latitud\\r\\n     longitud\\r\\n   }\\r\\n}\",\"variables\":{}}"
    headers = {
          'Content-Type': 'application/json'
          }
    response = requests.request("POST", url, headers=headers, data=payload)
    return json_normalize(response.json()['data'],'studentsByName')

def ConsultaLista():
    url = "http://127.0.0.1:5000"
    payload="{\"query\":\"{\\r\\n    getStudents{\\r\\n        nomgeo\\r\\n    }\\r\\n}\",\"variables\":{}}"
    headers = {
          'Content-Type': 'application/json'
          }
    response = requests.request("POST", url, headers=headers, data=payload)
    return json_normalize(response.json()['data'],'getStudents')