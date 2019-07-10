# Sending Email from Python 

import smtplib, ssl

def read_creds():
    user = passw = ""
    with open("credentials.txt", "r") as f: # ID and PW saved on this text file 
        file = f.readlines()
        user = file[0].strip()
        passw = file[1].strip()

    return user, passw


port = 465

sender, password = read_creds()

receive = sender

message = """\
Subject: Python Email Tutorial

This is from python!

Cavin
"""

context = ssl.create_default_context()

print("Starting to send")
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receive, message)

print("sent email!")
