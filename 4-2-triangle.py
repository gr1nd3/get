import RPi.GPIO as gpio
import sys
from time import sleep
dac=[26, 19, 13, 6, 5, 11, 9, 10]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
def perev(a, n):
    return [int (elem) for elem in bin(a)[2:].zfill(n)]
T=input()
        
try:
    while (True):
        t=int(T)/256/2
        for i in range(256):
            gpio.output(dac, perev(i, 8))
            sleep(t)

        for i in range(255, -1, -1):
            gpio.output(dac, perev(i, 8))
            sleep(t)
finally:
    gpio.output(dac, 1)
    gpio.cleanup()
  