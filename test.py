import time
import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD

lcd = CharLCD(cols = 16, rows = 2, pin_rs = 37, pin_e = 35, pins_data = [33,31,29,23], numbering_mode = GPIO.BOARD)
#lcd = CharLCD()
lcd.cursor_pos = (0,0)
print("HEllow world")
lcd.write_string("aiya")
time.sleep(30)
lcd.close(clear = True)
