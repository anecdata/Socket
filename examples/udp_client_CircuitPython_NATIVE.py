import wifi
import socketpool
import ipaddress
import time
from secrets import secrets


# edit host and port to match server
HOST = "192.168.10.10"
PORT = 5000
TIMEOUT = 5
INTERVAL = 5
MAXBUF = 256


print("Connecting to Wifi")
wifi.radio.connect(secrets["ssid"], secrets["password"])

pool = socketpool.SocketPool(wifi.radio)

print("Self IP", wifi.radio.ipv4_address)
server_ipv4 = ipaddress.ip_address(pool.getaddrinfo(HOST, PORT)[0][4][0])
print("Server ping", server_ipv4, wifi.radio.ping(server_ipv4), "ms")

buf = bytearray(MAXBUF)
while True:
    print("Create UDP Client socket")
    s = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)
    s.settimeout(TIMEOUT)

    size = s.sendto(b"Hello, world", (HOST, PORT))
    print("Sent", size, "bytes")

    size, addr = s.recvfrom_into(buf)
    print("Received", buf[:size], size, "bytes from", addr)

    s.close()

    time.sleep(INTERVAL)
