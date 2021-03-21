import wifi
import socketpool
import ipaddress
import time
from secrets import secrets


HOST = ""  # see below
PORT = 5000
TIMEOUT = None
MAXBUF = 256


print("Connecting to Wifi")
wifi.radio.connect(secrets["ssid"], secrets["password"])
pool = socketpool.SocketPool(wifi.radio)

print("Self IP", wifi.radio.ipv4_address)
HOST = str(wifi.radio.ipv4_address)
server_ipv4 = ipaddress.ip_address(pool.getaddrinfo(HOST, PORT)[0][4][0])
print("Server ping", server_ipv4, wifi.radio.ping(server_ipv4), "ms")

print("Create UDP Server socket")
s = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)
s.settimeout(TIMEOUT)

s.bind((HOST, PORT))

buf = bytearray(MAXBUF)
while True:
    size, addr = s.recvfrom_into(buf)
    print("Received", buf[:size], size, "bytes from", addr)

    size = s.sendto(buf[:size], addr)
    print("Sent", buf[:size], size, "bytes to", addr)
