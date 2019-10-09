#!/usr/bin/env python3

import socket
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])

print("Trying {0}:{1}...".format(HOST, PORT))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to {0}".format(HOST))
    while True:
        line = sys.stdin.readline()
        s.sendall(str.encode(line))
        response = s.recv(1024)
        print(response.decode())
