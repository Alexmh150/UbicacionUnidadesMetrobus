import requests
import pandas as pd 

class ConsultasResultado:
      """Clase para facilitar los querys hacia Graphql"""
      
      def __init__(self,url = "http://127.0.0.1:5000"):
            self.url = url

      def ConsultaUnidades(self):
            self.url
            payload="{\"query\":\"{\\r\\n  getUnidades{\\r\\n    vehicleId\\r\\n      }\\r\\n}\",\"variables\":{}}"
            headers = {'Content-Type': 'application/json'}
            response = requests.request("GET", self.url, headers=headers, data=payload)
            return pd.json_normalize(response.json()['data'],'getUnidades')

      def ConsultaAlcaldias(self):
            self.url
            payload="{\"query\":\"{\\r\\n  getAlcaldias{\\r\\n    Alcaldia\\r\\n      }\\r\\n}\",\"variables\":{}}"
            headers = {'Content-Type': 'application/json'}
            response = requests.request("GET", self.url, headers=headers, data=payload)
            return pd.DataFrame({'Alcaldias':pd.json_normalize(response.json()['data'],'getAlcaldias').Alcaldia.unique()})

      def ConsultaCoordenadasUnidad(self,vehicle_id):
            self.url
            self.vehicle_id = vehicle_id
            payload="{\"query\":\"{\\r\\n  coodernadasByUnidad(vehicleName:"+str(vehicle_id)+"){\\r\\n    positionLatitude\\r\\n    positionLongitude\\r\\n      }\\r\\n}\",\"variables\":{}}"
            headers = {'Content-Type': 'application/json'}
            response = requests.request("GET", self.url, headers=headers, data=payload)
            return pd.json_normalize(response.json()['data'],'coodernadasByUnidad')

      def ConsultaunidadesByAlcaldia(self,alcaldiaName):
            self.url
            self.alcaldiaName = alcaldiaName
            payload="{\"query\":\"{unidadesByAlcaldia(alcaldiaName:\\\""+alcaldiaName+"\\\"){vehicleId}}\",\"variables\":{}}"
            headers = {'Content-Type': 'application/json'}
            response = requests.request("GET", self.url, headers=headers, data=payload)            
            return pd.json_normalize(response.json()['data'],'unidadesByAlcaldia')