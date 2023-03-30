import RPi.GPIO as GPIO
import time 
def dec2bin(a):
    return [int (num) for num in bin(a)[2:].zfill(8)]
def num2dac(a):
    signal = dec2bin(a)
    GPIO.output(dac,signal)
    return signal

def adc():
    for a in range(levels):
        num2dac(a)
        time.sleep(0.001)
        if GPIO.input(comp) == 0:
            return a

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
bits = len(dac)
levels = 2 ** bits
maxv = 3.3
GPIO.setmode (GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
try:     
    while True:
        val = adc()
        print(val, dec2bin(val) ,"V= {:.4}" .format(val / levels * maxv))  
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
    c = 0