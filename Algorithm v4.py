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
    for station, arrivetime, leavetime in node:
        if x > len(node)-1:
             print("There are no more trains")
             print(node)
             currentnode = node[x-4] +'.txt' 
             print("currentnode:",currentnode)
             x=1          
        current_line = 1
        # print("node 1:",node[x])
        print("current time:",current_time)
        print("station:", node[x-1],node[x])
        print("currentnode:",currentnode)
        
        else:
            #checking if the train time is after the current time
            if int(current_time)< int(node[x]):   
                print("x",x)
                print("fastesttrain",fastestrain)
                print("currentnode",currentnode)
                #working out how long that train will take
                thistrain=node[x+1]
                
                #Checking if the destination is an option
                print ("node[x]:",node[x])
                print ("node[x+1]:",node[x+1])
                print ("node[x-1]:",node[x-1])
                if node[x-1] ==endnode:
                    print("Found the endnode",endnode)
                    break
                
                if int(thistrain)<int(fastestrain):
                    fastestrain = thistrain
                    previousstation = currentnode
                #working out what the shortest time is
                x=x+3
                #break
            else:
                print("nope")
                x = x+3
                print("x", x)
    else:
        print("done")
        
