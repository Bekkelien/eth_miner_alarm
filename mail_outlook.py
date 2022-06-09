import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from configuration import read_config 

config = read_config()

to = config["mail"]["to"]
fro_m = config["mail"]["from"]
pwd = config["mail"]["pwd"]

def sendmail():
    try:
        smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    except:
        smtpObj = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)

    try:
        msg = MIMEMultipart()

        msg['Subject'] = "| Miner has lower hashrate than expected |"
        message = 'ALARM'

        msg.attach(MIMEText(message))

        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(fro_m, pwd) 
        smtpObj.sendmail(fro_m, to, msg.as_string()) 

        smtpObj.quit()

        return True

    except:
        return False