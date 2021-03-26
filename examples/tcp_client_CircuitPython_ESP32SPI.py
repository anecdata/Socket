import board
import busio
import microcontroller
import supervisor
import sys
import os
import time
from digitalio import DigitalInOut
from adafruit_esp32spi import adafruit_esp32spi
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from secrets import secrets


# edit host and port to match server
HOST = "192.168.10.10"
PORT = 5000
TIMEOUT = 5
INTERVAL = 5
MAXBUF = 256


# PyPortal or similar; edit pins as needed
spi = board.SPI()
esp32_cs = DigitalInOut(board.ESP_CS)
esp32_ready = DigitalInOut(board.ESP_BUSY)
esp32_reset = DigitalInOut(board.ESP_RESET)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset, debug=False)

print("Connecting to Wifi")
esp.connect(secrets)

print("IP Address", esp.pretty_ip(esp.ip_address))
print("Server ping", esp.ping(HOST), "ms")

socket.set_interface(esp)

while True:
    print("Create TCP Client Socket")
    s = socket.socket()
    s.settimeout(TIMEOUT)

    print("Connecting")
    socketaddr = socket.getaddrinfo(HOST, PORT, 0, socket.SOCK_STREAM)[0][4]
    s.connect(socketaddr)

    s.send(b'Hello, world')
    print("Sent")

    buf = s.recv(MAXBUF)
    print("Receied", buf)

    s.close()

    time.sleep(INTERVAL)
