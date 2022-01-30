#!/usr/bin/env python3
import socket
import time


# edit host and port to match server
HOST = "192.168.10.10"
PORT = 5000
TIMEOUT = 5
INTERVAL = 5
MAXBUF = 256


while True:
    print("Create TCP Client Socket")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)

    print("Connecting")
    s.connect((HOST, PORT))

    size = s.send(b'Hello, world')
    print("Sent", size, "bytes")

    buf = s.recv(MAXBUF)
    print('Received', buf)
    
    s.close()

    time.sleep(INTERVAL)
