#!/usr/bin/env python3
import socket


HOST = ""
PORT = 5000
TIMEOUT = None
MAXBUF = 256


print("Create TCP Server Socket")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(TIMEOUT)

s.bind((HOST, PORT))
s.listen()
print("Listening")

while True:
    print("Accepting connections")
    conn, addr = s.accept()
    conn.settimeout(TIMEOUT)
    print("Accepted from", addr)

    buf = conn.recv(MAXBUF)
    print("Received", buf, "from", addr)

    size = conn.sendall(buf)
    print("Sent", buf[:size], size, "bytes to", addr)

    conn.close()
