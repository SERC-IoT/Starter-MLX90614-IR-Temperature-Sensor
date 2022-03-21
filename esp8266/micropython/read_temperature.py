import time
import mlx90614
from machine import SoftI2C, Pin

# define software I2C bus (needed for ESP8266).
# alternatively hardware I2C bus (ESP32 only) can be used by passing 0 or 1 to
# constructor, i.e.: i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=100000)
# any input pins can be defined for the i2c interface
# note, sensor doesn't work at default 400k bus speed
i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=100000)

# create sensor object
sensor = mlx90614.MLX90614(i2c)

print("* MLX90614 Temperature *")
print("Object | Ambient")

while True:
    # read sensor values
    object_temp = sensor.read_object_temp()
    ambient_temp = sensor.read_ambient_temp()

    # print readings to console
    # {} is used in conjunction with format() for substitution.
    # .2f       - format to 2 decimal places.
    print("{0:>5.2f}C | {1:>5.2f}C".format(object_temp, ambient_temp), end='\r')

    time.sleep_ms(1000)
