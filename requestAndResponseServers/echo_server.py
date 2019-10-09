#!/usr/bin/env python3

import socket

HOST = '127.0.0.1' #local host
PORT = 2000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("bound port and listening")
    conn, addr = s.accept()
    print("Accept just returned, we got a connection from", addr)
    with conn:
        while True:
            data = conn.recv(1024) #Read 1024 bytes from client
            if not data:
                break
            print("I just for this from the client", data)
            conn.sendall(data) #Block until all data is sent
