# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 11:04:59 2016

@author: avieux
"""

from __future__ import print_function
from cpppo.server.enip import client
import time

def write_xv():
    host = "192.168.0.22"
    #tags = [ "X_Test[0-9]", "X_Test[5]=(DINT)555", "X_Test[0-9]" ]
    tags = ["X_Test[2]=(DINT)65"]
    #data = [123]

    with client.connector( host=host ) as conn:
        for index,descr,op,reply,status,value in conn.pipeline(
            operations=client.parse_operations( tags ), depth=2 ):
            print( "%s: %20s: %s" % ( time.ctime(), descr, value ))
        
