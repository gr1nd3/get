import RPi.GPIO as GPIO
import time 
def dec2bin(a):
    return [int (num) for num in bin(a)[2:].zfill(8)]
def num2dac(a):
    signal = dec2bin(a)
    GPIO.output(dac,signal)
    return signal


def adc():
    bin = 0
    left = -1
    right = 256
    while True:

        mid  = int((right + left)/2)
        GPIO.output(dac, dec2bin(mid))
        time.sleep(0.001)

        comp_val = GPIO.input(comp)
        
        if comp_val == 0:
            right = mid
        else:
            left = mid

        if (right - left <= 1):
            return int(mid)



dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
bits = len(dac)
l = 2 ** bits
maxv = 3.3
GPIO.setmode (GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
try:     
    while True:
        val = adc()
        print(val, dec2bin(val) ,"V= {:.4}" .format(val / l * maxv))  
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
    c = 0
