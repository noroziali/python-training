import telnetlib
import time

IP = open("IP.txt")
USERNAME = "admin"
PASSWORD = "cisco"
ENABLE_PASS = "cisco"
TFTP = "192.168.102.254"

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
