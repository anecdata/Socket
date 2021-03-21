import wifi
import socketpool
import ipaddress
import time
from secrets import secrets


HOST = ""  # see below
PORT = 5000
TIMEOUT = None
BACKLOG = 2
MAXBUF = 256


print("Connecting to Wifi")
wifi.radio.connect(secrets["ssid"], secrets["password"])
pool = socketpool.SocketPool(wifi.radio)

print("Self IP", wifi.radio.ipv4_address)
HOST = str(wifi.radio.ipv4_address)
server_ipv4 = ipaddress.ip_address(pool.getaddrinfo(HOST, PORT)[0][4][0])
print("Server ping", server_ipv4, wifi.radio.ping(server_ipv4), "ms")

print("Create TCP Server socket", (HOST, PORT))
s = pool.socket(pool.AF_INET, pool.SOCK_STREAM)
s.settimeout(TIMEOUT)

s.bind((HOST, PORT))
s.listen(BACKLOG)
print("Listening")

buf = bytearray(MAXBUF)
while True:
    print("Accepting connections")
    conn, addr = s.accept()
    conn.settimeout(TIMEOUT)
    print("Accepted from", addr)

    size = recv_into(buf, [MAXBUF])
    print("Received", buf[:size], size)

    conn.send(buf[:size])
    print("Sent", buf[:size], size, "bytes")

    conn.close()
