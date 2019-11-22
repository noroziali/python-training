import platform
import sys
import socket
import datetime
import time
import telnetlib
import os
from datetime import datetime
import consolegraphic
print "hello"
#time.sleep(5)
#print "hello agaoin "
user_input=raw_input("stated your desigred destenation in CDIR format:")
print "okay,you've selected :"
print user_input
scantarget = user_input
net_split= scantarget.split(".")
dot="."
netid=net_split[0]+dot+net_split[1]+dot+net_split[2]+dot
start= int(raw_input("where would you like to start? \n"))
end= int(raw_input("okay, and where would you like to finish? \n"))
os_type= platform.system()
if os_type == "Windows":
    ping = "ping -n 2 "

elif os_type == "Linux":
    ping = "ping -c 2 "

else:
    ping == "ping -c 1 "
time_str = datetime.now()
time_end = int(0)
time_dur = int(0)
print "operation is initiated . . . \n"
target_count= 0
target_list=[]
for ip in xrange(start,end):
    target =netid + str(ip)
    command = ping + target
    command = str(command)
    command_exec = os.popen(command)
    for line in command_exec.readlines():
        if "ttl" in line.lower():
            target_count= target_count + 1 
            print target, "----> Live"
            target_list.append(target)


time_end = datetime.now()
time_dur = time_end - time_str
print "operation is Compeleted ! \n"
print "total operation time :", time_dur
print "toatal live systyems :", target_count
seelist = raw_input("would you like to see the list of hosts? \n") 
if seelist == yes:
    print target_list
else:
    exit
    

