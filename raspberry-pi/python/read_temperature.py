# script for reading temperture values from MLX90614 sensor.

import time
from smbus2 import SMBus
from mlx90614 import MLX90614

# define sensor i2c address
thermometer_address = 0x5a

try:
    # create sensor object
    bus = SMBus(1)
    sensor = MLX90614(bus, address=thermometer_address)

    print("* MLX90614 Temperature *")
    print("Object | Ambient")

    while True:
        # read sensor values
        object_temp = sensor.get_object_1() #note: method might have changed to get_obj_temp()
        ambient_temp = sensor.get_ambient() #note: method might have changed to get_amb_temp()

        # print readings to console
        # {} is used in conjunction with format() for substitution.
        # .2f       - format to 2 decimal places.
        print("{0:>5.2f}C | {1:>5.2f}C".format(object_temp, ambient_temp), end='\r')

        time.sleep(1)


except KeyboardInterrupt:
    print('script stopped by user')
finally:
    bus.close()
    print('Goodbye!')
