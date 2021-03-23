# Socket
TCP and UDP socket examples and helpers for use with CircuitPython. Easy to modify: Add exception handling, context managers; make TCP examples re-use connections or make new connections. ESP32-S2 and CPython TCP examples based on https://github.com/adafruit/circuitpython/tree/main/tests/circuitpython-manual/socketpool/

More examples:

Adafruit_CircuitPython_ESP32SPI TCP Client example: HTTP  
https://github.com/adafruit/Adafruit_CircuitPython_ESP32SPI/blob/master/examples/esp32spi_tcp_client.py

Adafruit_CircuitPython_ESP32SPI UDP Client example: NTP  
https://github.com/adafruit/Adafruit_CircuitPython_ESP32SPI/blob/master/examples/esp32spi_udp_client.py

Adafruit CircuitPython ESP32-S2 examples:  
https://github.com/adafruit/circuitpython/tree/main/tests/circuitpython-manual/socketpool/

## Compatibility
```
Socket Feature Availability

                               CircuitPython  CircuitPython
                CPython        ESP32SPI       ESP32-S2

TCP Server      Yes            Not Impl.      Yes

TCP Client      Yes            Yes            Yes

UDP Server      Yes            Not Impl.      Yes

UDP Client      Yes            Yes            Yes


Compatibility (Verified)

                                CircuitPython    CircuitPython
                 CPython        ESP32SPI         ESP32-S2
                 TCP Server     TCP Server       TCP Server

CPython
TCP Client       Yes            Not Impl.        Yes

CircuitPython
ESP32SPI
TCP Client       Yes            Not Impl.        Yes

CircuitPython
ESP32-S2
TCP Client       Yes            Not Impl.        Yes

                                CircuitPython    CircuitPython
                 CPython        ESP32SPI         ESP32-S2
                 UDP Server     UDP Server       UDP Server

CPython
UDP Client       Yes*           Not Impl.        Yes*

CircuitPython
ESP32SPI
UDP Client       Yes*           Not Impl.        Yes*

CircuitPython
ESP32-S2
UDP Client       Yes*           Not Impl.        Yes*

* pending circuitpython issues
```
