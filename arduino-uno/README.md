# Arduino Uno and -- -- Sensor

![Arduino Sketch Compiles](https://github.com/SERC-IoT/Starter-Start/workflows/Arduino%20Sketch%20Compiles/badge.svg)

<!-- #TODO add sensor and circuit diagrams -->
Setup instructions and starter code for using the -- -- sensor and an Arduino development board.

<br />

## Files and Folders

| File/Folder | Description |
|--- | --- |
| [arduino/](arduino/) | Arduino projects folder |
| [arduino/mlx90614-temperature-sensor/mlx90614-temperature-sensor.ino](arduino/mlx90614-temperature-sensor/mlx90614-temperature-sensor.ino) | Simple arduino sketch. |
| [mkr-wifi-1010-setup.md](mkr-wifi-1010-setup.md) | Setup instructions for using an Arduino MKR WiFi 1010 dev board. |
|  |  |

<br />

## Setup

Setup instructions for an Arduino Uno board is below. For MKR WiFi 1010 based setup instructions see [mkr-wifi-1010-setup.md](mkr-wifi-1010-setup.md).

## Circuit Diagram
Wire the components as shown in the diagram.

![circuit diagram](assets/...)

#### Components Needed
* 
* connecting wires
* arduino uno development board


<br />

![breadboard diagram](assets/...)

<br />

### Default Pin Wiring

| Pin No | Function | Device Connection |
| --- | --- | --- |
| 5V | +5V | Vdd |
| GND | GND | GND |
|  |  |  |

![pin diagram](assets/Pinout-UNOrev3_latest.png)

<br />

## Arduino

The sketch will work with many different types and chipset of board. To use an Arduino Uno, make sure to select the correct board in Boards Manager.

The arduino sketches require the Adafruit MLX90614 library. It is included in the root additional-libraries folder. Afternatively, they can be downloaded through the Arduino libraries manager or from https://github.com/adafruit/Adafruit-MLX90614-Library

## References

* https://www.arduino.cc/en/reference/board
* https://github.com/adafruit/Adafruit-MLX90614-Library
