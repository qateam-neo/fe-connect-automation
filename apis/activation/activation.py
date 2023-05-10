import requests
import json
from config import Config 
from apis.config_apis import BASE_URL, HEADERS
from apis.activation.activation_config import ActivationConfig

class ClientActivateAPI:
    
    def __init__(self, client_id):
        self.base_url = BASE_URL
        self.client_id = client_id
        self.headers = ActivationConfig.HEADERS
        self.funding_amount = 12000
        
    def client_activate_api(self):
        try:
            data={"initial_investment": self.funding_amount, "create_fund": True}
            endpoint = self.base_url + '/development/activate/' + self.client_id
            response = requests.post(endpoint, data=json.dumps(data), headers=self.headers)
            response.raise_for_status()  # Raise an exception if the status code is not 200 OK
            return response.json()
        except Exception as e:
            print("API call failed with error: {}".format(e))
            return None