#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpServer=socket(AF_INET,SOCK_STREAM)

tcpServer.bind(ADDR)
tcpServer.listen(5)

while True:
	print('waiting for connection')
	tcpClient,addr=tcpServer.accept()
	print('...connected from',addr)

	while True:
		data = tcpClient.recv(BUFSIZ).decode()
		print(data)
		if not data:
			continue
		else:
			print("[%s] %s" % (ctime(),data))
			serdata = input('>')
			while True:
				if not serdata:
					continue
				else:
					tcpClient.send(('[%s] %s'%(ctime(),serdata)).encode())

					print('waitting....')
					break
	tcpClient.close()
tcpServer.close()
