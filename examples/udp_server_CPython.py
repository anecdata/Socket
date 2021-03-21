#!/usr/bin/env python3
import time
import socket


HOST = ""
PORT = 5000
TIMEOUT = None
MAXBUF = 256


print("Create UDP Server Socket")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(TIMEOUT)

s.bind((HOST, PORT))

while True:
    buf, addr = s.recvfrom(MAXBUF)
    print("Received", buf, "from", addr)

    size = s.sendto(buf, addr)
    print("Sent", buf, size, "bytes to", addr)
