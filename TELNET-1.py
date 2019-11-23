import telnetlib
import time

IP = "192.168.102.99" 
USERNAME = "admin"
PASSWORD = "cisco"
ENABLE_PASS = "cisco"

telnet = telnetlib.Telnet(IP)
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
telnet.write("hostname HQ\n")
time.sleep(1)
telnet.write("end\n")
time.sleep(1)
telnet.write("exit\n")
