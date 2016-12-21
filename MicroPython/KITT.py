# Knight Rider K.I.T.T.

from machine import Pin, PWM
from neopixel import NeoPixel
from time import sleep

POCET_LED = 8
pin = Pin(2, Pin.OUT)
np = NeoPixel(pin, POCET_LED)

a = b = c = d = 0
while True:
    for i in range(8):
        d = c
        c = b
        b = a
        a = i
        np[d] = 0, 0, 0
        np[c] = 5, 0, 0
        np[b] = 50, 0, 0
        np[a] = 100, 0, 0
        np.write()
        sleep(1/12)
    for i in range(8-2,0,-1):
        d = c
        c = b
        b = a
        a = i
        np[d] = 0, 0, 0
        np[c] = 5, 0, 0
        np[b] = 50, 0, 0
        np[a] = 100, 0, 0
        np.write()
        sleep(1/12)
