# plcNotify Main ################################################
import plcRead
import textOut
import time
#import popper

lastRun2 = ("0")
print("First Pass")

# Main Loop #####################################################
while 1:
    print("Initiate PLC Read Process")
    # Read from PLC #############################################
    plcRead.read_1()
    # Return Values from PLC ####################################
    plcValue1 = plcRead.read_1()
    # Move "Read" Value to varible 1 ############################
    v1 = plcValue1
    # Compare Logic and call textOut routine if true ############  
    if (plcValue1 != lastRun2) and (plcValue1 != "0"):
        textOut.textLogic(v1)
        lastRun2 = plcValue1
    print("Process Complete")
    print("//")
    time.sleep(5) 
        
    
        


        
    
