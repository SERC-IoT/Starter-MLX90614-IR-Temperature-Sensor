# ESP8266 and -- -- Sensor

<!-- #TODO add sensor and circuit diagrams -->
Code for getting started with -- -- sensor and an ESP8266 development board.

<br />

## Files and Folders

| File/Folder | Description |
|--- | --- |
| [arduino/](arduino/) | folder for arduino sketches. // For Arduino, use the sketches in the Arduino Uno folder [../arduino-uno/arduino](../arduino-uno/arduino) |
| [micropython/](micropython/) | folder for micropython scripts. Pymakr is configured to sync this folder with the micropython device. |
|  |  |

<br />

## Setup

Setup instructions for a WeMos D1 mini are below. For ESP32 based setup instructions see [esp32-setup.md](esp32-setup.md).

## Circuit Diagram

Wire the components as shown in the diagram.

![circuit diagram](assets/esp8266-starter-circuit-diagram_schem.svg)

#### Components Needed

* 
* connecting wires
* esp8266 device

<br />

![breadboard diagram](assets/esp8266-starter-circuit-diagram_bb.svg)

<br />

### Default Pin Wiring

| Pin No | Function |  | Device Connection |
| --- | --- | --- | --- |
|  |  |  |  |
| 1 | +3.3V |  | Vdd |
| 6 | GND |  | GND |
|  |  |  |  |

![pin diagram](assets/wemos-d1-mini-pinout.png)

Further details and other board pin out diagrams can be found here: https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/

<br />

## Arduino

The sketch will work with many different types and chipset of board. To use an ESP8266 board with Arduino IDE, you will need to install the relevant board configuration files. Follow the instructions here: https://arduino-esp8266.readthedocs.io/en/latest/installing.html

<!-- #TODO add library info -->
The arduino sketches require the -- -- libraries. They are included in the root additional-libraries folder. Afternatively, they can be downloaded through the Arduino libraries manager or from -- --

<br />

## MicroPython

<!-- #TODO add library info -->
MicroPython already has drivers for -- devices baked in.

<br />

## References

- https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/
