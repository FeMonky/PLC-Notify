# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 09:37:02 2016

@author: avieux
"""

from __future__ import print_function
from cpppo.server.enip import client
import time

host = "192.168.0.22"
tags = ["PyComm_Read1[0-9]"]

        
with client.connector( host=host ) as conn:
    req1 = conn.write( "PyComm_Read1[0-2]", data=[1,1,1] )
    req2 = conn.read( "PyComm_Read1[2]" )
    assert conn.readable( timeout=1.0 ), "Failed to receive reply 1"
    rpy1 = next( conn )
    assert conn.readable( timeout=1.0 ), "Failed to receive reply 2"
    rpy2 = next( conn )
