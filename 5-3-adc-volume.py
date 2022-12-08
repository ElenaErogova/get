import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
dac=[26, 19, 13, 6, 5, 11, 9, 10]
leds=[24, 25, 8, 7, 12, 16, 20, 21]
comp=4
troyka=17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def perev(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        GPIO.output(dac, perev(k))
        sleep(0.005)
        if GPIO.input(comp)==0:
            k-=2**i
    return k

def volume(n):
    n=int(n/256*10)
    mas=[0]*8
    for i in range(n-1):
        mas[i]=1
    return mas

try:
    while True:
        k=adc()
        if k!=0:
            GPIO.output(leds, volume(k))
            print(int(k/256*10))

        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup() 