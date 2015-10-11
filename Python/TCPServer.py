# Simple TCP socket example


from socket import *

serverPort = 12001
listenSocket = socket(AF_INET, SOCK_STREAM)
listenSocket.bind(('', serverPort))
listenSocket.listen(1)
print 'The server is listening for a connection'
connectionSocket, addr = listenSocket.accept()
print 'The server is waiting for a string'
sentence = ''
while (sentence != 'q' and sentence != 'Q'):
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)

connectionSocket.close()
