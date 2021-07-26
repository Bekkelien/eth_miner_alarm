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

        # Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
        s = smtplib.SMTP_SSL(smtp)
        # uncomment if interested in the actual smtp conversation
        # s.set_debuglevel(1)
        # do the smtp auth; sends ehlo if it hasn't been sent already
        s.login(fro_m, pwd)

        s.sendmail(fro_m, to, msg.as_string())
        s.quit()

# Test mail within this block
if __name__ == "__main__":
        sendmail()