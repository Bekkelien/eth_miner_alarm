import smtplib
from email.mime.multipart import MIMEMultipart

from configuration import read_config 

config = read_config()

to = config["mail"]["to"]
fro_m = config["mail"]["from"]
pwd = config["mail"]["pwd"]
smtp = config["mail"]["smtp"]

message = "| Miner has lower hashrate than expected |"

def sendmail():

        msg = MIMEMultipart('alternative')
        msg['Subject'] = message
        msg['From'] = fro_m
        msg['To'] = to

        s = smtplib.SMTP_SSL(smtp)
        s.login(fro_m, pwd)

        s.sendmail(fro_m, to, msg.as_string())
        s.quit()

# Test mail within this block
if __name__ == "__main__":
        sendmail()