import sys
import Adafruit_DHT

while True: 
	print('hello world')
	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,4)
	print("Temperature: " + str(temperature) + "C")
	print("Humidity: " + str(humidity))
