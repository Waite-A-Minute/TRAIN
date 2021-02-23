import time
import math
from datetime import datetime, date
from time import sleep


stations = []
linenumber=1
fastestrain= 99999
previousstation = ""
currenttext = ""
destination = ""
startfile = ""
currentnode = ""
startnode = input("Starting station: ")
endnode = input("Destination station: ")
notinthepast = False
x=1
nodenumber=1
nodelength = ""
startnode=startnode+'.txt'
endnode=endnode+'.txt'
timetonode=0
visitednodes = []
thistrain=""
print(startnode)
#date and time stuff
now = datetime.now()
current_time = 1000#now.strftime("%H%M")    
today = date.today()
d1 = today.strftime("%d/%m/%Y") 
startfile = open(startnode,'r')
print(startfile.read())
estimatedtime=current_time

currentnode = startnode
print(currentnode)
print("endnode",endnode)
#getting the files ready
node = open(currentnode,'r') 
node = node.read()
node = node.split("\n")
node = [item.split(",") for item in node if node]
while thistrain != endnode:
   
    for station,leavetime , arrivetime in node:
        if x > len(node)-1:
             print("There are no more trains")
             print(node)
             currentnode = station +'.txt' 
             print("currentnode:",currentnode)
             x=1          
        
  
        else:
            #checking if the train time is after the current time
            if int(current_time)< int(leavetime):   
                
                #print statments to monitor progress
                print("x",x)
                print("fastesttrain",fastestrain)
                print("currentnode",currentnode)
                print("current time:",current_time)
                print("station being looked at:", station,"leavetime", leavetime)
                print("currentnode:",currentnode)    
                

                #Checking if the destination is an option
                if station ==endnode:
                    print("Found the endnode",endnode)
                    break
                else:
                    print("This aint it Chief")
                    
                   #working out what the shortest time is    
                if int(thistrain)<int(fastestrain):
                    fastestrain = thistrain
                    previousstation = currentnode
                    
             #moving onto the next line in the file
                x=x+1
                #break
            else:
                print("Leaves too soon")
                x = x+1
                print("x", x)
    else:
        print("done")
        
