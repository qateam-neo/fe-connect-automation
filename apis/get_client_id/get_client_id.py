
import requests
import json
from config import Config 
from apis.config_apis import BASE_URL, HEADERS
from apis.get_client_id.get_client_id_config import GetClientIDConfig

class GetClientIdAPI:
    
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = GetClientIDConfig.HEADERS
        self.civil_id_number = Config.CIVIL_ID_NUMBER
        
    def get_client_id(self):
        try:
            data = {"civil_id_number": self.civil_id_number + "000"} 
            endpoint = self.base_url + '/development/project-connect/profile'
            response = requests.get(endpoint, data=json.dumps(data), headers=self.headers)
            response.raise_for_status()  # Raise an exception if the status code is not 200 OK
            return response.json()
        except Exception as e:
            print("API call failed with error: {}".format(e))
            return None