# Setup for ESP32 dev board

<!-- #TODO add sensor and circuit diagrams -->
Setup instructions for an ESP32 based development board, like the Lolin D32 or Lolin32 Lite.

## Circuit Diagram
Wire the components as shown in the diagram.

![circuit diagram](assets/esp32--sensor-circuit-diagram_schem.png)

#### Components Needed
* 
* connecting wires
* esp32 development board


<br />

![breadboard diagram](assets/esp32--sensor-circuit-diagram_bb.png)

<br />

### Default Pin Wiring

| Pin No | Function | Device Connection |
| --- | --- | --- |
|  |  |  |
|  | +3.3V | Vdd |
|  | GND | GND |
|  | GPIO 0 | DQ |

![pin diagram](assets/Lolin32_pinout03.png)

Further details and other board pin out diagrams can be found here: https://randomnerdtutorials.com/esp32-pinout-reference-gpios/

<br>

## Arduino

The sketch will work with many different types and chipset of board. To use an ESP32 board with Arduino, you will need to install the relevant board configuration files. Follow the instructions here: https://github.com/espressif/arduino-esp32/blob/master/docs/arduino-ide/boards_manager.md

<!-- #TODO add library info -->
The arduino sketch requires the -- library. It is included in the libraries folder.

<br />

## MicroPython

<!-- #TODO add library info -->
MicroPython already has drivers for -- devices baked in.

<br />

## References

- https://randomnerdtutorials.com/esp32-pinout-reference-gpios/
