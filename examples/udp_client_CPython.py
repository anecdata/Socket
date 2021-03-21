#!/usr/bin/env python3
import time
import socket


# edit host and port to match server
HOST = "192.168.10.10"
PORT = 5000
TIMEOUT = 5
INTERVAL = 5
MAXBUF = 256


buf = bytearray(MAXBUF)
while True:
    print("Create UDP Client Socket")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(TIMEOUT)

    size = s.sendto(b"Hello, world", (HOST, PORT))
    print("Sent", size, "bytes")

    size, addr = s.recvfrom_into(buf)
    print("Received", buf[:size], size, "bytes from", addr)

    s.close()

    time.sleep(INTERVAL)
