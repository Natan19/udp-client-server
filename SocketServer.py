import socket

MAX_SIZE_BYTES = 65535 #Maximum size of a UDP DGRAM

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 3000
hostname = '' #INADDR_ANY
s.bind((hostname, port)) #Binds the socket to the port and lets the hostname be chosen.
print('Listening at {}'.format(s.getsockname())) #Prints the IP Adress and port binded to the socket

while True:
    data, address = s.recvfrom(MAX_SIZE_BYTES)
    message = data.decode('ascii')
    upperCaseMessage = message.upper()
    print('The client at {} says {!r}'.format(address, message))
    data = upperCaseMessage.encode('ascii')
    s.sendto(data, address)


