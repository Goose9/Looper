import RPi.GPIO as gpio
import time

#pin 13 red
#pin 16 blue
#pin 20 green
#pin 21 yellow

gpio.setmode(gpio.BCM)
gpio.setup(13, gpio.IN)
gpio.setup(16, gpio.IN)
gpio.setup(20, gpio.IN)
gpio.setup(21, gpio.IN)

counter = 0
while True:
    if gpio.input(13):
        counter += 1
        print(counter, " red light on...")
                            
    if gpio.input(16):
        counter += 1
        print(counter, " blue light on...")
            
    if gpio.input(20):
        counter += 1
        print(counter, " green light on...")
        
    if gpio.input(21):
        counter += 1
        print(counter, " yellow light on...")
        
    time.sleep(1)