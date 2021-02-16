# Setup for MKR WiFi 1010 dev board

Setup instructions for an Arduino MKR WiFi 1010 development board.

## Circuit Diagram
Wire the components as shown in the diagram.

![circuit diagram](assets/mkr-mlx90614-sensor-circuit-diagram_schem.png)

#### Components Needed
* mlx90614 sensor breakout board
* connecting wires
* MKR WiFi 1010 development board

<br />

![breadboard diagram](assets/mkr-mlx90614-sensor-circuit-diagram_bb.png)

<br />

### Default Pin Wiring

| Pin No | Function |  | Device Connection |
| --- | --- | --- | --- |
| VCC | +3.3V |  | Vin |
| GND | GND |  | GND |
| 11 | SDA |  | SDA |
| 12 | SCL |  | SCL |
|  |  |  |  |

![pin diagram](assets/Pinout-MKRwifi1010_latest.png)

<br>

## Arduino

Drivers and board details need to be installed to use the Arduino MKR series. Follow the instructions here: https://www.arduino.cc/en/Guide/MKRWiFi1010#toc2

The arduino sketches require the Adafruit MLX90614 library. It is included in the root additional-libraries folder. Afternatively, they can be downloaded through the Arduino libraries manager or from https://github.com/adafruit/Adafruit-MLX90614-Library
