import requests
import json
import time

ETH = "Feab6260F1c88b515137E152593ac6b3683D925B"
MAIL = False

while True:
    response_API = requests.get('https://api.ethermine.org/miner/:' + ETH + '/currentStats')
    
    if response_API.status_code == 200:
        data = response_API.text
        data = json.loads(data)

        if isinstance(data["data"]["activeWorkers"], int):

            if data["data"]["activeWorkers"] == 4:
                print("All workers are online")
                MAIL = True
            
            if data["data"]["activeWorkers"] < 4 and MAIL == True:
                print(f"WARNING, Total number of workers are : {data['data']['activeWorkers']}")
                print("Sending WARNING email")
                # Send email
                MAIL = False

        else:
            print("Respons value error")
    else:
        print("API Error")

    time.sleep(60)
    