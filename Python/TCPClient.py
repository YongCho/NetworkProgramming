# Simple TCP
#


from socket import *
serverName = '127.0.0.1'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = ''
while (sentence != 'q' and sentence != 'Q'):
    sentence = raw_input('Input lowercase sentence: ')
    clientSocket.send(sentence)
    response = clientSocket.recv(1024)
    print 'From Server: ', response
clientSocket.close()
