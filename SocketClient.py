import socket

MAX_SIZE_BYTES = 65535 #Maximum size of UDP DGRAM

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('OS assigned {} to me'.format(s.getsockname()))
message = input('Input lowercase sentence:')
data = message.encode('ascii')
s.sendto(data, ('127.0.0.1', 3000))
data, address = s.recvfrom(MAX_SIZE_BYTES)
text = data.decode('ascii')
print('The server {} replied with {!r}'.format(address, text))