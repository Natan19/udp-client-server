import socket

MAX_SIZE_BYTES = 65535 #Maximum size of a UDP DGRAM

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 3000
hostname = ''
s.bind((hostname, port))

while True:
    data, address = s.recvfrom(MAX_SIZE_BYTES)
    message = data.decode('utf-8')
    print(message)
    anwser = input("Type answer:")
    anwser = anwser.encode('utf-8')
    s.sendto(anwser, address)''