import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)

while True:
    
    GPIO.output(7, GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(7, GPIO.LOW)
    time.sleep(1)
