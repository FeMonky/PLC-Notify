# plcRead #########################################################
import os
import sys
import textOut
from cpppo.server.enip import client 

def read_1():
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
    with client.connector (host=host) as conn:
        for index, descr, op, reply, status, value in conn.pipeline( 
         operations=client.parse_operations(tags), depth=2):   
            print("%20s: %s" % (descr, value))
    raw=("%s" % (value[0]))
    plcValue1=(raw)
    print("Read Done")
    return(plcValue1)
