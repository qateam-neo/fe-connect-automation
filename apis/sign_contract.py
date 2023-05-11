
import requests
import json
from config import CIVIL_ID_NUMBER
from apis.config_apis import BASE_URL, HEADERS

class SignContractAPI:
    
    def __init__(self, client_id):
        self.base_url = BASE_URL
        # self.headers = HEADERS
        # self.headers = {
        #     "Content-Type": "application/json",
        #     "Authorization": f"Bearer {auth_token}"
        # }
        self.client_id = client_id
        self.civil_id_number = CIVIL_ID_NUMBER
        
    def sign_contract_api(self):
        try:
            self.endpoint = self.base_url + '/development/' + self.client_id + "/set-contract-signed",
            headers={
                "Authorization": '#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#',
                "Content-Type": "application/json",
            }
            response = requests.put(self.endpoint, headers=headers)
            response.raise_for_status()  # Raise an exception if the status code is not 200 OK
            return response.json()
        except Exception as e:
            print("API call failed with error: {}".format(e))
            return None
        
    # def generate_token_api(self, data):
    #     try:
    #         # data = {"civil_id_number": self.civil_id_number} 
    #         data ={"civil_id": CIVIL_ID_NUMBER,"is_encoded": True}
    #         self.endpoint = self.base_url + '/development/project-connect/token'
    #         headers={
    #             "Authorization": '#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#',
    #             "Content-Type": "application/json",
    #             "Accept-Language":"en-US,en;q=0.9",
    #             "Connection":"keep-alive",
    #             "Origin":"http://neo-frontend",
    #             "Referer":"http://neo-frontend",
    #             "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    #             "X-Locale":"en_US",
    #             "X-Platform":"web",
    #             "X-Token-Source":"connect",
    #             "X-Version":"1.0",
    #             "Accept":"application/json, text/plain, */*"

    #         }
    #         response = requests.post(self.endpoint, headers=headers)
    #         response.raise_for_status()  # Raise an exception if the status code is not 200 OK
    #         return response.json()
    #     except Exception as e:
    #         print("API call failed with error: {}".format(e))
    #         return None
        

      