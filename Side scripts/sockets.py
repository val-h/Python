import socket

# Create a Internet socket that uses TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Provide a tuple with the ip and port for the server to run on, localhost
s.bind(('127.0.0.1', 55555))
# listen() tells the server to listen for connections
s.listen()

# Permanent loop that accepts connections
print('Server is running...')
while True:
    # Recieve the client and address from a connection
    client, address = s.accept()
    print(f'Connected to {address}')
    client.send('You are connected!'.encode())
    client.close()


