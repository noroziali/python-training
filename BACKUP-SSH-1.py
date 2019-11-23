import paramiko
import time

IP = open("IP.txt")
USERNAME = "admin"
PASSWORD = "cisco"
ENABLE_PASS = "cisco"
TFTP = "192.168.102.254"

for line in IP.readlines():
    HOST = line.strip()
    SSH = paramiko.SSHClient()
    SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())   
    SSH.connect(HOST, username=USERNAME, password=PASSWORD)
    Console = SSH.invoke_shell()
    Console.recv(65535) 
    Console.send("en\n")
    time.sleep(1)  
    Console.send(ENABLE_PASS + "\n")
    time.sleep(1)
    Console.send("copy running-config tftp:\n")
    time.sleep(1)
    Console.send(TFTP + "\n")   
    time.sleep(1)
    Console.send("\n")
    time.sleep(1)
    Console.recv(65535)
    Console.send("end\n")
    time.sleep(1)
    SSH.close()
