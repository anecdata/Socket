import board
import busio
import digitalio
import time
from adafruit_wiznet5k.adafruit_wiznet5k import WIZNET5K
import adafruit_wiznet5k.adafruit_wiznet5k_socket as socket

# WIZnet W5100S-EVB-Pico
SPI0_SCK = board.GP18
SPI0_TX = board.GP19
SPI0_RX = board.GP16
SPI0_CSn = board.GP17
W5x00_RSTn = board.GP15

cs = digitalio.DigitalInOut(SPI0_CSn)
spi = busio.SPI(SPI0_SCK, MOSI=SPI0_TX, MISO=SPI0_RX)
eth = WIZNET5K(spi, cs, is_dhcp=True, debug=False)

ethernetRst = digitalio.DigitalInOut(W5x00_RSTn)
ethernetRst.direction = digitalio.Direction.OUTPUT
ethernetRst.value = False
time.sleep(1)
ethernetRst.value = True

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
