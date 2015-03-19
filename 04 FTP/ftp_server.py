# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 22:50:01 2014

@author: e2life
"""

# Echo server program
import socket

HOST = '.'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn,addr = s.accept()

print 'Connected by ', addr
while 1:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()