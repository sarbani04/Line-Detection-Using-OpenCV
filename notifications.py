
'''import time
import cv2
import numpy as np'''

## SEND EMAIL ALERTS
import smtplib 
'''from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders'''
#from sinchsms import SinchSMS


def email_alert(name, rstp, reason):
    print('sending email alert')
    sender = 'suryakantamazumder9@gmail.com'
    receiver = ["sarbani.m4@gmail.com", "parthag835@gmail.com"]

    #msg = MIMEMultipart()
    #msg['From'] = sender
    #msg['to'] = receiver
    #msg['Subject'] = "[	ATTENTION USER	]"
    body = " Your camera '{}' of RTSP {} has encountered {}".format(name, rtsp, reason)
    #msg.attach(MIMEText(body, 'plain'))

    
        # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
    s.starttls()
        # Authentication
    s.login(sender, 'dwR8\jnABy"e')
    #helbppbnnhpdjqbq
    print("Logging into server account")

        # Converts the Multipart msg into a string
    text = body
    for i in receiver:
            #print(i)
        s.sendmail(sender, i, text)
        print("Sending email...")
        # terminating the session
    s.quit()


email_alert('Sarbani', 'Hi', 'Trespassing Alert')



'''content='sarbani'
mail=smtplib.SMTP('smtp.gmail.com',587)
#mail.ehlo()

mail.starttls()
mail.login('sarbani.m4@gmail.com','password')
message = 'Email sent'
mail.sendmail('sarbani.m4@gmail.com','suryakantamazumder9.m4@gmail.com', message)
mail.quit()
'''


# function for sending SMS 
'''def sendSMS(message): 
    

    # enter all the details 
    # get app_key and app_secret by registering 
    # a app on sinchSMS
    number = ['+917042903334','+919958076688']
    app_key = 'bb5ac3d6-d55b-4d34-9680-8bb712ecb4a4'
    app_secret = 'Fr79j61PxU+BuSexJD93Bg=='
  
    # enter the message to be sent 
    #message = "WARNING SOMEONE'S TRESSAPSSING"
 
    client = SinchSMS(app_key, app_secret) 
    print("Sending '%s' to %s" % (message, number)) 
  
    response = client.send_message(number, message) 
    message_id = response['messageId'] 
    response = client.check_status(message_id) 
  
    # keep trying unless the status retured is Successful 
    while response['status'] != 'Successful': 
        print(response['status']) 
        time.sleep(1) 
        response = client.check_status(message_id) 
  
    print(response['status'])'''

