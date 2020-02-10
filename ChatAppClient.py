import socket

MAX_SIZE_BYTES = 65535 #Maximum size of a UDP DGRAM

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 3000
hostname = ''
host = ''

while True:
    if not host:
        host = input('Type host:')
    s.connect((host, port))
    message = input('Type message:')
    data = message.encode('utf-8')
    s.send(data)
    data = s.recv(MAX_SIZE_BYTES)
    text = data.decode('utf-8')
    print('Replied with: {!r}'.format(text))
