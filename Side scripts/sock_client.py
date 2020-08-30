import socket
from socket import SOCK_STREAM

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server, localhost
s.connect(('127.0.0.1', 55555))
# Specify how many bytes to recieve
message = s.recv(1024)
s.close()

print(message.decode())

