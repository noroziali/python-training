# Server side
from socket import *

ip = raw_input('Enter Your(server) the ip address:')

port = int(raw_input('Enter Your(server) the port:'))

socket_connection = socket(AF_INET, SOCK_STREAM)
socket_connection.bind((ip, port))
socket_connection.listen(10)
print('The server is running on port ' + str(port))
client, address = socket_connection.accept()
print('Session open --> ' + str(address))
receive_data = client.recv(1024)
print(receive_data)
while True:
    shell_command = raw_input('\ncommand ==>')
    if shell_command is None or shell_command == '' or shell_command == '\n':
        client.sendall('-')
        continue

    client.send(shell_command)
    receive_data = client.recv(1024123213)
    print(receive_data)


client.close()
