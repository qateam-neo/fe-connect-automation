
import requests
import json
from config import Config 
from apis.config_apis import BASE_URL, HEADERS

class ClientApprovalAPI:
    
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = HEADERS
        self.civil_id_number = Config.CIVIL_ID_NUMBER
        
    def client_approval_api(self):
        try:
            data = {"civil_id_number": self.civil_id_number + "000"} 
            endpoint = self.base_url + '/external/project-connect/dev/profile/approve'
            response = requests.post(endpoint, data=json.dumps(data), headers=self.headers)
            response.raise_for_status()  # Raise an exception if the status code is not 200 OK
            return response.json()
        except Exception as e:
            print("API call failed with error: {}".format(e))
            return None