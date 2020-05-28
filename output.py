#!/usr/bin/python
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
from RPLCD.gpio import CharLCD
from gpiozero import Buzzer

GPIO.setmode(GPIO.BOARD)
buzzer = Buzzer(22)
lcd = CharLCD(cols = 16, rows = 2, pin_rs = 37, pin_e = 35, pins_data = [33, 31, 29, 23], numbering_mode=GPIO.BOARD)
tempCheck = False
hotTime = 0
TEMP = 50
HUMID = 90
while True:
	humidity, temperature = Adafruit_DHT.read_retry(11,4)
	temperature = temperature*9/5 + 32
	if ( temperature > TEMP or humidity > HUMID) and tempCheck == False:
		print("Buzzzer Noise")
		buzzer.on()
		time.sleep(5)
		buzzer.off()
		tempCheck = True
	if tempCheck == True: 
		hotTime += 1
		if (hotTime > 100):
			buzzer.on()
			time.sleep(5)
			buzzer.off()
			hotTime = 0
	if tempCheck == True and temperature < TEMP and humidity < HUMID: 
		tempCheck = False 
	lcd.cursor_pos = (0,0)
	lcd.write_string("Temp: %d F" % temperature)
	lcd.cursor_pos = (1,0)
	lcd.write_string("Humidity %d %%" % humidity)
	print("Temperature: " + str(temperature) + 'C')
	print("Humidity: " + str(humidity) + '%')
	
