# Raspberry Pi and MLX90614 Infra-Red Temperature Sensor

![RPi Python Checks](../../../workflows/RPi%20Python%20Checks/badge.svg) ![Python code quality](../../../blob/badges/.github/badges/rpipycodequality.svg)

Code for getting started with MLX90614 infra-red temperature sensor using a Raspberry Pi.

<br />

## Files and Folders

| File/Folder | Description |
|--- | --- |
| [python/](python/) | folder for python scripts. |
| [python/read_temperature.py](python/read_temperature.py) | Example python script that reads the temperature values and prints them to the console. |
| [python/requirements.txt](python/requirements.txt) | Requirements file for python dependancy libraries. |
| [config.sh](config.sh) | Bash script to automatically configure and setup the Raspberry Pi for using the MLX90614 infra-red temperature sensor. |
|  |  |

<br />

## Circuit Diagram

Wire the components as shown in the diagram.

![circuit diagram](assets/rpi-mlx90614-sensor-circuit-diagram_schem.svg)

#### Components Needed

* mlx90614 sensor breakout board
* connecting wires
* raspberry pi

<br />

![breadboard diagram](assets/rpi-mlx90614-sensor-circuit-diagram_bb.svg)

<br />

### Default Pin Wiring

| Pin No | Function |  | Device Connection |
| --- | --- | --- | --- |
| 1 | +3.3V |  | Vin |
| 3 | GPIO2 / I2C1 SDA |  | SDA |
| 5 | GPIO3 / I2C1 SCL |  | SCL |
| 6 | GND |  | GND |
|  |  |  |  |

![pin diagram](assets/rp2_pinout.png)

<br />

## Configure Raspberry Pi

The Raspberry Pi needs to have the I2C interface enabled and dependancy libraries need to be installed. Either follow the instructions below or run the config.sh script to automatically setup the Raspberry Pi.

```bash
chmod +x config.sh
./config.sh
```

### Enable I2C interface

I2C needs to be enabled on the Raspberry Pi in order to read data from the sensor.

Open the raspi-config tool, found in preferences, or type the following in a terminal.

```bash
sudo raspi-config
```

Under interfaces, enable I2C interface. Click ok and reboot.

Check that the device is communicating properly. In a terminal, type `sudo i2cdetect -y 1`.

```bash
pi@raspberrypi:~ $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- 5a -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

The default address for the sensor is 0x5a.

### Python Dependancies

The python script requires the PyPi smbus2 library and the PyMLX90614 library from https://pypi.org/project/PyMLX90614/. These libraries can be installed from PyPI by executing:

```bash
sudo pip3 install smbus2 pymlx90614
```

A requirements.txt file is also provided and can be used instead.
```bash
cd ./python
sudo pip3 install -r requirements.txt
```

<br />

## References

- https://pypi.org/project/smbus2/
- https://pypi.org/project/PyMLX90614/
