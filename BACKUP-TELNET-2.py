import telnetlib
import time
import os
import datetime
import shutil

IP = open("IP.txt")
USERNAME = "admin"
PASSWORD = "cisco"
ENABLE_PASS = "cisco"
TFTP = "192.168.102.254"
DATE1 = datetime.datetime.now()
DATE2 = ("%s-%s-%s" %(DATE1.year,DATE1.month,DATE1.day))
DIR1 = "C:\BACKUP-"
DIR2 = str(DATE2)
DIR3 = DIR1 + DIR2

for line in IP.readlines():
    HOST = line.strip()
    telnet = telnetlib.Telnet(HOST)
    telnet.read_until("Username: ")
    time.sleep(3)
    telnet.write(USERNAME + "\n")
    time.sleep(3)
    telnet.read_until("Password: ")
    telnet.write(PASSWORD + "\n")
    time.sleep(1)
    telnet.write("en\n")
    time.sleep(1)
    telnet.write(ENABLE_PASS + "\n")
    time.sleep(1)
    telnet.write("copy running-config tftp:\n")
    time.sleep(1)
    telnet.write(TFTP + "\n")
    time.sleep(1)
    telnet.write("\n")
    time.sleep(1)
    telnet.write("end\n")
    time.sleep(1)
    telnet.write("exit\n")
    
shutil.copytree("C:\TFTP-Root", DIR3)