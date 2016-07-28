# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 09:37:02 2016

@author: avieux
"""

from __future__ import print_function
from cpppo.server.enip import client
import time

#host = "192.168.0.22"
#tags = "X_Test[5-7]"
print("Start Reading PLC")
# Read Items from Access Config file into List and strip /n
with open('config.txt') as f:
        w = [word.strip() for word in f]
        l1 = str(w[1])
        #print(l1)               #PLC Ip Address:
        l3 = str(w[3])
        #print(l3)               #PLC Tags:

host = (l1)
tags = [l3]
        
with client.connector( host=host ) as conn_w:
    req1 = conn_w.write('X_Text[0-9]', data=[1,1,1,1,1,1,1,1,1,1])
    req2 = conn_w.read('X_Text[0-9]')
    assert conn_w.readable( timeout=1.0 ), "Failed to receive reply 1"
    rpy1 = next( conn_w )
    assert conn_w.readable( timeout=1.0 ), "Failed to receive reply 2"
    rpy2 = next( conn_w )
    

with client.connector (host=host) as conn_r:
        for index, descr, op, reply, status, value in conn_r.pipeline( 
         operations=client.parse_operations(tags), depth=2):   
            print("%20s: %s" % (descr, value))
raw=("%s" % (value[2]))
plcValue1=(raw)
print(raw)
print("Read Done")