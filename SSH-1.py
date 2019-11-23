import paramiko
import time

IP = "192.168.93.10"
USERNAME = "admin"
PASSWORD = "cisco"
ENABLE_PASS = "cisco"

SSH = paramiko.SSHClient()
SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())
SSH.connect(IP, username=USERNAME, password=PASSWORD)
Console = SSH.invoke_shell()
Console.recv(65535)
Console.send("en\n")
time.sleep(1)
Console.send(ENABLE_PASS + "\n")
time.sleep(1)
Console.send("conf t\n")
time.sleep(1)
Console.send("hostname TEST3\n")
time.sleep(1)
Console.recv(65535)
Console.send("end\n")
time.sleep(1)
SSH.close()
