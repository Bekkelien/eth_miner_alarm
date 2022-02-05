import requests
import json
import time

from mail import sendmail

WORKERS = 4
ETH = "Feab6260F1c88b515137E152593ac6b3683D925B"
MAIL = True # Do not set this to false!


while True:
    response_API = requests.get('https://api.ethermine.org/miner/:' + ETH + '/currentStats')
    
    if response_API.status_code == 200:
        data = response_API.text
        data = json.loads(data)

        if isinstance(data["data"]["activeWorkers"], int):

            if data["data"]["activeWorkers"] == WORKERS:
                print("All workers are online")
                MAIL = True
            
            if data["data"]["activeWorkers"] < WORKERS and MAIL == True:
                print(f"WARNING, Total number of workers are : {data['data']['activeWorkers']}")
                sendmail()
                print("WARNING email shipped")
                MAIL = False
            
            elif data["data"]["activeWorkers"] < WORKERS:
                print("Wating for workers to go back online")

        else:
            print("Respons value error")
    else:
        print("API Error")

    time.sleep(60)
    