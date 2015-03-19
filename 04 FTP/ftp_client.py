# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 22:46:42 2014

@author: e2life
"""

# Echo client program

import socket, time

HOST = '192.168.100.128'
#PORT = 50007
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

i = 1
while True:
    cmd = raw_input("Command: ").strip()
    if cmd == '':
        continue
    s.sendall(cmd)
    #s.sendall("Hello, this is %d package sent to the ftp server!" % i)
    i += 1
    data = s.recv(1024)
    #time.sleep(2)
    #print 'Received',repr(data)
    print data
s.close()
