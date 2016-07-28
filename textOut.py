#textOut ################################################
import os
import sys
import plcRead
import time
import smtplib
import popper
from email.mime.text import MIMEText
import tkinter
from tkinter import messagebox

def textSend(finalMessage):
    print("Start Message Transmission")
    # Read Items from Access Config file into List and strip /n
    with open('config.txt') as f:
        w = [word.strip() for word in f]             
        l5 = str(w[5])
        #print(l5)               #Mail Account Username:
        l7 = str(w[7])
        #print(l7)               #Mail Account Password:                
        l9 = str(w[9])
        #print(l9)               #Mail Account String:

    username = (l5)
    password = (l7)
    sms1 = (l9)
    message = finalMessage
    msg = MIMEText("""From: %s
    Subject: WachterAlarmRobot--
    %s""" % (username, message))
       
    print("Sending Message Now")
    print(finalMessage)
    time.sleep(5)
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(username,password)
        server.sendmail(username, sms1, msg.as_string())
        server.quit()
        print("Successfully Sent Message")
    except Exception:
        print("Error: Unable to Send Message")

    
def textLogic(v1):
    print("Start Message Assembly Logic")

    # Read Items from Config file into List and strip /n
    with open('config.txt') as f:
        w = [word.strip() for word in f]             
        l11 = str(w[11])
        #print(l11)               #Alarm_Message_1:
        l13 = str(w[13])
        #print(l13)               #Alarm_Message_2:                
        l15 = str(w[15])
        #print(l15)               #Alarm_Message_3:
        l17 = str(w[17])
        #print(l17)              #Alarm_Message_4:             
        l19 = str(w[19])
        #print(l19)              #Alarm_Message_5:             
        l21 = str(w[21])
        #print(l21)              #Alarm_Message_6:            
        l23 = str(w[23])
        #print(l23)              #Alarm_Message_7:            
        l25 = str(w[25])
        #print(l25)              #Alarm_Message_8:           
        l27 = str(w[27])
        #print(l27)              #Alarm_Message_9:          
        l29 = str(w[29])
        #print(l29)              #Alarm_Message_10:             
        l31 = str(w[31])
        #print(l31)              #Alarm_Message_11:              
        l33 = str(w[33])
        #print(l33)              #Alarm_Message_12:            
        l35 = str(w[35])
        #print(l35)              #Alarm_Message_13:            
        l37 = str(w[37])
        #print(l37)              #Alarm_Message_14:            
        l39 = str(w[39])
        #print(l39)              #Alarm_Message_15:            
        l41 = str(w[41])
        #print(l41)              #Alarm_Message_16:             
        l43 = str(w[43])
        #print(l43)              #Alarm_Message_17:              
        l45 = str(w[45])
        #print(l45)              #Alarm_Message_18:           
        l47 = str(w[47])
        #print(l47)              #Alarm_Message_19:


    finalMessage = ('')

    if  (v1 == "1"):
        finalMessage = l11
    elif(v1 == "2"):
        finalMessage = l13
    elif(v1 == "3"):
        finalMessage = l15
    elif(v1 == "4"):
        finalMessage = l17
    elif(v1 == "5"):
        finalMessage = l19
    elif(v1 == "6"):
        finalMessage = l21
    elif(v1 == "7"):
        finalMessage = l23
    elif(v1 == "8"):
        finalMessage = l25
    elif(v1 == "9"):
        finalMessage = l27
    elif(v1 == "10"):
        finalMessage = l29
    elif(v1 == "11"):
        finalMessage = l31
    elif(v1 == "12"):
        finalMessage = l33
    elif(v1 == "13"):
        finalMessage = l35
    elif(v1 == "14"):
        finalMessage = l37
    elif(v1 == "15"):
        finalMessage = l39
    elif(v1 == "16"):
        finalMessage = l41
    elif(v1 == "17"):
        finalMessage = l43
    elif(v1 == "18"):
        finalMessage = l45
    elif(v1 == "19"):
        finalMessage = l47

    print("Message Assembly Done")
    print(finalMessage)
    textSend(finalMessage)
    popper.popupmsg(finalMessage)