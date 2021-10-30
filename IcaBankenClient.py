import requests
import uuid
import json

class IcaBankenClient:
    ACCESS_TOKEN_ENDPOINT = 'https://ims.icagruppen.se/oauth/v2/token'

    API_BASE_URL = 'https://apimgw-icabanken.ica.se/t/icabanken.tenant/ica/bank/services/psd2/accounts/sandbox/1.0.0'

    def __init__(self, client_id, client_secret, ssn):
        self.CLIENT_ID = client_id
        self.CLIENT_SECRET = client_secret
        self.SSN = ssn

    def get_access_token(self):
        
        access_token_request = requests.post(self.ACCESS_TOKEN_ENDPOINT, data = {
            'grant_type': 'client_credentials', 'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET, 'scope': 'psd2_sandbox:' + self.SSN}) ##.status_code   #json()

        response = access_token_request.json()
        response_status = access_token_request.status_code

        if response_status == 200:
            self.access_token = response['access_token']
            return response_status
        else:
            return response

    def get_transactions(self, account_id, status):

        transactions_endpoint = '/Accounts/' + account_id + '/transactions'

        transactions = requests.get(self.API_BASE_URL + transactions_endpoint, params = {'status': status}, 
            headers = {
                'accept': 'application/json',
                'X-Request-ID': str(uuid.uuid4()),
                'Authorization': 'Bearer ' + self.access_token
            })
        
        return transactions.json()