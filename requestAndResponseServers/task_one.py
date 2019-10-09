#!/usr/bin/env python3

import socket 
import sys

HOST = sys.argv[1]
if( len(sys.argv) < 3):
    PAGE = '/'
else:
    PAGE = sys.argv[2]

print("We well fetch '{0}{1}'".format(HOST, PAGE))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, 80))

    http_request = "GET {0} HTTP/1.0\r\n\r\n".format(PAGE) #\r\n\r\n is what the server looks for to know request is done, the client is done talking
    
    print("HTTP request:")
    print(http_request)
    #Send request to server
    s.sendall(str.encode(http_request))
    #Read all data from the server
    response_buffer = b''
    while True:
        data = s.recv(1024)
        response_buffer += data
        if len(data) == 0:
            break #Server closed connection
    
    print("HTTP response:")
    print(response_buffer.decode('utf-8',"ignore"))
