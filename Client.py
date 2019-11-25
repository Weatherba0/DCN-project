import socket
UDP_IP_ADDRESS = "127.0.0.1"
UPD_PORT_NUM = 6789
Message = "Hello World"

cSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cSocket.sendto(Message.encode(), (UDP_IP_ADDRESS, UPD_PORT_NUM))
