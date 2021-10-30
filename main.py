import json
from IcaBankenClient import IcaBankenClient

#Please provide all information below as per README.md
#CLIENT_ID = '<client_id>' 
#CLIENT_SECRET = '<client_secret>'
#SSN = '<ssn>'
#ACCOUNT_ID = '<account_id>'
#STATUS = '<status>'

def write_to_file(data):
    with open('data.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

client = IcaBankenClient(CLIENT_ID, CLIENT_SECRET, SSN)
access = client.get_access_token()

if access == 200:
    write_to_file(client.get_transactions(ACCOUNT_ID, STATUS))
else:
    write_to_file(access)