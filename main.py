import requests
import time 

from mail import sendmail

# User interface
nanominer_api = "https://api.nanopool.org/v1/eth/reportedhashrate/0xfeab6260f1c88b515137e152593ac6b3683d925b"

hashrate_limit = input("Enter alarm limit in Mh/s: \n")

# Variable to reset alarm when hasrate has been restored to hasrate limit
alarm_activated = True

print("Alarm is activated, with limit set to:", hashrate_limit)

while 1:
    
    # Dirty error catcher 
    try:

        # Get nanominer API of last reported hasrate
        response = requests.get(nanominer_api)

        # Store response in json formate
        hashrate = response.json()

        # Get last reported hasrate
        last_reported_hashrate = hashrate['data']

        # Check if last reported hasrate are less than hasrate limit
        if int(last_reported_hashrate) < int(hashrate_limit) and alarm_activated == True:
            sendmail()
            print("Alarm, mail i sendt out")

            alarm_activated = False

        # If hasrate limit has been restored activate alarm again 
        if int(last_reported_hashrate) >= int(hashrate_limit):
            
            alarm_activated = True


        # Read time 
        localtime = time.localtime(time.time())
        start_h = localtime[3]
        start_m = localtime[4]
        start_s = localtime[5]

        print("Last reported hashrate:", str(last_reported_hashrate), "Time:", str(start_h) + ":" + str(start_m) + ":" + str(start_s))

    # Dirty expection handler
    except Exception as program_failure:
        print("Program is not running correctly", program_failure)


    # Delay, halt program for 60s
    time.sleep(60)