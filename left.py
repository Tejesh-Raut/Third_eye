import RPi.GPIO as GPIO
import time
enable_pin = 18
M1A = 17
M2A=22
M1B=23
M2B=24

GPIO.setmode(GPIO.BCM)
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(M1A, GPIO.OUT)
GPIO.setup(M2A, GPIO.OUT)
GPIO.setup(M1B, GPIO.OUT)
GPIO.setup(M2B, GPIO.OUT)
GPIO.output(enable_pin, True)
GPIO.output(M1A, False)
GPIO.output(M2A, True)
GPIO.output(M1B, True)
GPIO.output(M2B, False)
