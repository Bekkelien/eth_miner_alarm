import requests
import json
import time
from datetime import datetime

from mail import sendmail
from configuration import read_config 

config = read_config()

MAIL = True # Do not set this to false!

HASHRATE_LIMIT = int(input("Enter alarm limit in MH/s: \n"))

while True:
    response_API = requests.get('https://api.ethermine.org/miner/:' + config["eth"]["ethermine"] + '/currentStats')
    
    if response_API.status_code == 200:
        data = response_API.text
        data = json.loads(data)

        reported_hashrate = data['data']['reportedHashrate']

        if isinstance(reported_hashrate,int):
            reported_hashrate = reported_hashrate / 1000000
            if reported_hashrate >= HASHRATE_LIMIT:
                print(f"{datetime.now().time()} Reported hashrate: {reported_hashrate} MH/s")
                MAIL = True
            
            if MAIL == True:
                if reported_hashrate < HASHRATE_LIMIT:
                    MAIL = False
                    print(f"{datetime.now().time()} WARNING, Reported hashrate are: {reported_hashrate} MH/s")
                    sendmail()
                    print(f"{datetime.now().time()} WARNING email shipped")
                    
            else:
                print(f"{datetime.now().time()} Wating on hashrate")

        else:
            print(f"{datetime.now().time()} Respons value error")
    else:
        print(f"{datetime.now().time()} API Error")

    time.sleep(60)
    