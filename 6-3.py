import socket
import time
import math
import os
import sys
import colorama
from colorama import Fore

serverSocket = socket.socket()

host = ''
port = 8889
ThreadCount = 0

serverSocket.bind((host,port))

print('\nWaiting for connection...')
serverSocket.listen(3)
colorama.init()
print(Fore.CYAN)
def calc(clientSocket, addr):
	clientSocket.send(str.encode('Welcome to the Server\n'))
	while True:

		print('\nConnected to ', addr)

		data = clientSocket.recv(1024)
		num = clientSocket.recv(1024)


		if data == b'1':
			print(data.decode('utf-8') + '. Logarithm Process')
			answer = math.log(float(num))
		elif data == b'2':
			print(data.decode('utf-8') + '. Square Root Process')
			answer = math.sqrt(float(num))
		elif data == b'3':
			print(data.decode('utf-8') + '. Exponential Process')
			answer = math.frexp(float(num))
		else:
			print('Connection Ended....')
			False
			break

		convert = str(answer)
		clientSocket.send(convert.encode('utf-8'))

while True:
	Client, address = serverSocket.accept()
	if(calc(Client,address)):
		pass
	else:
		False
		break

serverSocket.close()

