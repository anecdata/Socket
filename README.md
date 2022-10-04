# Socket
TCP and UDP socket examples and helpers for use with CircuitPython. Easy to modify: Add exception handling, context managers; make TCP examples re-use connections or make new connections. ESP32-S2 and CPython TCP examples based on https://github.com/adafruit/circuitpython/tree/main/tests/circuitpython-manual/socketpool/

More examples:

Adafruit_CircuitPython_ESP32SPI TCP Client example: HTTP  
https://github.com/adafruit/Adafruit_CircuitPython_ESP32SPI/blob/master/examples/esp32spi_tcp_client.py

Adafruit_CircuitPython_ESP32SPI UDP Client example: NTP  
https://github.com/adafruit/Adafruit_CircuitPython_ESP32SPI/blob/master/examples/esp32spi_udp_client.py

Adafruit CircuitPython ESP32-S2 examples:  
https://github.com/adafruit/circuitpython/tree/main/tests/circuitpython-manual/socketpool/

There is a class and example for a WIZnet5k TCP [HTTP / WSGI] Server:
https://github.com/adafruit/Adafruit_CircuitPython_Wiznet5k/blob/main/examples/wiznet5k_wsgiserver_test.py

## Compatibility
```
Socket Feature Availability

                               CircuitPython  CircuitPython  CircuitPython  CircuitPython
                CPython        ESP32SPI       ESP32-S2       Pico W         WIZnet5K

TCP Server      Yes            *              Yes            Yes            Yes

TCP Client      Yes            Yes            Yes            Yes            Yes

UDP Server      Yes            **             Yes            Yes

UDP Client      Yes            Yes            Yes            Yes            Yes


CircuitPython Compatibility

                                CircuitPython    CircuitPython    CircuitPython
                 CPython        ESP32SPI         ESP32-S2         Pico W
                 TCP Server     TCP Server       TCP Server       TCP Server

CPython
TCP Client       6.2.0          Not Impl.        6.2.0            8.0.0-beta.1

CircuitPython
ESP32SPI
TCP Client       6.2.0          Not Impl.        6.2.0            

CircuitPython
ESP32-S2
TCP Client       6.2.0          Not Impl.        6.2.0            

CircuitPython
Pico W
TCP Client                      Not Impl.                         

                                CircuitPython    CircuitPython    CircuitPython
                 CPython        ESP32SPI         ESP32-S2         Pico W
                 UDP Server     UDP Server       UDP Server       UDP Server

CPython
UDP Client       6.2.0          Not Impl.        6.2.0            

CircuitPython
ESP32SPI
UDP Client       6.2.0          Not Impl.        6.2.0            

CircuitPython
ESP32-S2
UDP Client       6.2.0          Not Impl.        6.2.0            

CircuitPython
Pico W
UDP Client                      Not Impl.                         
```
`*` There is a class and example for an ESP32SPI TCP (HTTP) Server:  
https://github.com/adafruit/Adafruit_CircuitPython_ESP32SPI/tree/master/examples/server  
However, it is implemented at the interface level (`esp`), not the socket level. ESP32SPI is structured around the NINA firmware, which is structured around Arduino WiFi, which doesn't directly implement socket `bind`, `listen`, or `accept`.

`**` There is a rudimentary example for an ESP32SPI UDP Server:
https://gist.github.com/anecdata/b3d43870942684570d90e3fc9833292b
However, it is implemented at the interface level (`esp`), not the socket level. ESP32SPI is structured around the NINA firmware, which is structured around Arduino WiFi, which doesn't directly implement socket `bind`, `listen`, or `accept`.
