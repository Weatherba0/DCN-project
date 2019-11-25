import socket

UDP_IP_ADDRESS = "127.0.0.1"
UPD_PORT_NUM = 6789
#Message = "Hello World"
clients = []

sSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sSocket.bind((UDP_IP_ADDRESS, UPD_PORT_NUM))

while True:
    data, adr = sSocket.recvfrom(1024)
    print("Message: ", data.decode())
