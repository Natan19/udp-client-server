import socket

MAX_SIZE_BYTES = 65535 #Maximum size of UDP DGRAM

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
hosts = []
while True:
    host = input('Input host address:')
    port = 3000
    hosts.append((host, port))
    message = input('Input lowercase sentence:')
    data = message.encode('ascii')
    print('OS assigned {} to me'.format(s.getsockname()))
    s.sendto(data, (host, port))
    data, address = s.recvfrom(MAX_SIZE_BYTES)
    text = data.decode('ascii')
    if(address in hosts):
        print('The server {} replied with {!r}'.format(address, text))
        hosts.remove(address)
    else:
        print('message {!r} from unexpected host {}!'.format(text, address))
