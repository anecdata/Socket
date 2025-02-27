import board
import busio
import digitalio
import time
from adafruit_wiznet5k.adafruit_wiznet5k import WIZNET5K
import adafruit_wiznet5k.adafruit_wiznet5k_socket as socket

W5x00_RSTn = board.GP15

# WIZnet W5100S Ethernet Hat on Raspberry Pi Pico [W]
cs = digitalio.DigitalInOut(board.GP17)
spi = busio.SPI(board.GP18, MOSI=board.GP19, MISO=board.GP16)
eth = WIZNET5K(spi, cs)

ethernetRst = digitalio.DigitalInOut(W5x00_RSTn)
ethernetRst.direction = digitalio.Direction.OUTPUT
ethernetRst.value = False
time.sleep(1)
ethernetRst.value = True

HOST = eth.pretty_ip(eth.ip_address)
PORT = 5000
TIMEOUT = None
MAXBUF = 256

print(f"WIZnet Server IP Address: {HOST}")

print("Create TCP Server Socket")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(TIMEOUT)

s.bind((HOST, PORT))
s.listen()
print(f"Listening on {HOST}, {PORT}")

buf = bytearray(MAXBUF)
while True:
    print("Accepting connections")
    conn, addr = s.accept()
    conn.settimeout(TIMEOUT)
    print("Accepted from", addr)

    size = conn.recv_into(buf, MAXBUF)
    print("Received", buf[:size], size, "bytes")

    conn.send(buf[:size])
    print("Sent", buf[:size], size, "bytes")

    conn.close()
