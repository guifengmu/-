#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from socket import *
from select import *
import re


HOST = 'www.bilibili.com'
PORT = 80
BUFSIZ = 1024
ADDR = (HOST,PORT)
tcpclient = socket(AF_INET,SOCK_STREAM)
tcpclient.connect(ADDR)

tcpclient.send(('GET/ \n').encode())

data = tcpclient.recv(BUFSIZ).decode()

with open(r"/root/webpage.txt",'w') as f:
	f.write(data)
