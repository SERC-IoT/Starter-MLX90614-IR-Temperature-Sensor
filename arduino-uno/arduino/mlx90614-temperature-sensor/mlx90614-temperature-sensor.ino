/*
 * Sketch that reads temperature from a MLX90614 temperature sensor, and prints
 * the reading to the serial console.
 */

// Include the libraries we need
#include <Wire.h>
#include <Adafruit_MLX90614.h>

// create sensor object
Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void setup() 
{
  Serial.begin(9600);

  Serial.println("** MLX90614 Temperature Reading **"); 
  mlx.begin();  // initialise sensor
}

void loop()
{
  // the mlx90614 sensor provides both an ambient temperature reading and an ir
  // temperature reading of objects in front of the sensor.
  Serial.print("Ambient = "); Serial.print(mlx.readAmbientTempC()); Serial.print(" C");
  Serial.print("\tObject = "); Serial.print(mlx.readObjectTempC()); Serial.println(" C");

  Serial.println();
  delay(1000);
}
