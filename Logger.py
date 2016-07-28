# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 17:14:57 2016

@author: avieux
Logging Acknowledges and dismisses
"""
import os
import sys
import textOut
import datetime
from cpppo.server.enip import client 

def Logit(yesno, msg):
    timer=datetime.datetime.now().strftime("%c")
    print("Logging Selection")
    with open("LOGGER.txt", "a") as f:
        f.write(timer + "\n")
        f.write(yesno + ": " + msg + "\n")