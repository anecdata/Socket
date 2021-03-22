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

buf = bytearray(MAXBUF)
while True:
    size, addr = s.recvfrom_into(buf)
    print("Received", buf[:size], size, "bytes from", addr)

    size = s.sendto(buf[:size], addr)
    print("Sent", buf[:size], size, "bytes to", addr)
