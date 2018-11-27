##main.py for a dht12 sensor

import dht12
import machine

i2c = machine.I2C(scl = machine.Pin(5), sda = machine.Pin(4))

print(i2c.scan())
#confirm that this returns a value. Usually ##

sensor = dht12.DHT12(i2c)

sensor.measure()

temp = sensor.temperature()
#returns a float of the temperature in Celcius

hum = sensor.humidity()
#returns a float of the relative humidity in percent
