# Doc https://weatherstack.com/documentation

from utilities.SecretManager import *
import requests

class forex_rate:
    def __init__(self):
        sm = secretmanager()
        self.data = sm.jsonify()
    def return_data(self,fromcur,tocur):
        token = self.data["currency_token"]
        url = f"https://api.apilayer.com/fixer/latest?symbols={tocur}&base={fromcur}"
        headers = {
            "apikey": f"{token}"
        }
        response = requests.request("GET",url,headers=headers)
        # response = response.json()
        data = response.json()
        print(data["success"])
        if data["success"] == True:
            msg = f"Forex rate from {data["base"]} to provided currencies are:\n"
            for currency, value in data["rates"].items():
                val = f"{currency}: {value}"
                msg += val + "\n"
            return msg
        else:
            msg = f"Forex rate from to provided currencies are else statementt"
            return msg 