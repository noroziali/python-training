import telnetlib
import time

IP = open("IP.txt")
USERNAME = "admin"
PASSWORD = "cisco"
ENABLE_PASS = "cisco"

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
    telnet.write("conf t\n")
    time.sleep(1)
    telnet.write("hostname 33333333\n")
    time.sleep(1)
    telnet.write("end\n")
    time.sleep(1)
    telnet.write("exit\n")
