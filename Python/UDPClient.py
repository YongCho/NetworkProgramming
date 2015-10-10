# UDP socket example
#
# To run:
#     Execute python UDPServer.py
#     Execute python UDPClient.py in a different terminal window


from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = ''
while (message != 'q' and message != 'Q'):
	message = raw_input('Input lowercase sentence: ')
	clientSocket.sendto(message, (serverName, serverPort))
	response, serverAddress = clientSocket.recvfrom(2048)
	print response

clientSocket.close()
