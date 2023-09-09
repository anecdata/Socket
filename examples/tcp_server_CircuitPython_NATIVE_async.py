# async TCP server, listening on three ports
# Adafruit CircuitPython 8.2.4 on 2023-08-22; Adafruit QT Py ESP32-S3 no psram with ESP32S3

import os
import asyncio
import traceback
import wifi
import socketpool

PORTS = (5000, 5001, 5002,)
MAXBUF = 256
ACCEPT_TIMEOUT = 0
CLIENTS_PER_SERVER = 1
CONN_TIMEOUT = 1

async def tcpserver(PORT):
    s = pool.socket(pool.AF_INET, pool.SOCK_STREAM)
    s.bind(("", PORT))
    s.listen(CLIENTS_PER_SERVER)
    s.settimeout(ACCEPT_TIMEOUT)
    buf = bytearray(MAXBUF)
    while True:
        try:
            conn, addr = s.accept()
            print(f"Connection to {wifi.radio.ipv4_address}:{PORT} accepted from {addr[0]}:{addr[1]}")
            conn.settimeout(CONN_TIMEOUT)
            size = conn.recv_into(buf, MAXBUF)
            print(f"Received {buf[:size]} {size} bytes")
            conn.close()
        except OSError as ex:  # EAGAIN
            pass
        await asyncio.sleep(0)

pool = socketpool.SocketPool(wifi.radio)

# choose your own connect adventure
wifi.radio.connect(os.getenv("WIFI_SSID"), os.getenv("WIFI_PASSWORD"))

async def main():
    tasks = []
    for taskno in range(len(PORTS)):
        tasks.append(asyncio.create_task(tcpserver(PORTS[taskno])))
    await asyncio.gather(*tasks)

asyncio.run(main())

# CPython TCP client, connecting to three ports
'''
#!/usr/bin/env python3
# Python 3.9.6
import socket
import time
import random

# edit host and port to match server
HOST = "192.168.6.210"
PORTS = (5000, 5001, 5002,)
TIMEOUT = 5
INTERVAL = 1

while True:
    PORT = random.choice(PORTS)
    print(f"Creating TCP Client Socket...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(TIMEOUT)
        print(f"Connecting to {HOST}:{PORT}...")
        try:
            s.connect((HOST, PORT))
            size = s.send(b'Hello, world')
            print(f"Sent {size} bytes to {HOST}:{PORT}")
        except socket.timeout:
            print(f"connect timed out")
    time.sleep(INTERVAL)
'''
