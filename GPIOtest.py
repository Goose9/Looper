import RPi.GPIO as gpio
import time
from mutex import mutex
import time

class gpio:
    def __init__(self):
        # pin 13 red
        # pin 16 blue
        # pin 20 green
        # pin 21 yellow

        gpio.setmode(gpio.BCM)
        gpio.setup(13, gpio.IN)
        gpio.setup(16, gpio.IN)
        gpio.setup(20, gpio.IN)
        gpio.setup(21, gpio.IN)

        self.pedal_mutex = mutex
        self.pedal_id = 0
        self.pedal_old = 0

    def checkInput(self):
        counter = 0
        while True:
            if gpio.input(13):
                counter += 1
                print(counter, " red light on...")
                self.pedal_id = 1

            if gpio.input(16):
                counter += 1
                print(counter, " blue light on...")
                self.pedal_id = 2

            if gpio.input(20):
                counter += 1
                print(counter, " green light on...")
                self.pedal_id = 3

            if gpio.input(21):
                counter += 1
                print(counter, " yellow light on...")
                self.pedal_id = 4

            time.sleep(0.5)

    def pedal_idChange(self):
        while self.pedal_old == self.pedal_id and not self.pedal_id == 0:
            time.sleep(0.5)

        self.pedal_old = self.pedal_id
        return self.pedal_old

    @property
    def pedal_mutex(self):
        return self.pedal_mutex

    @pedal_mutex.setter
    def pedal_mutex(self, mut):
        self.pedal_mutex = mut

    @property
    def pedal_id(self):
        self.pedal_mutex.lock()
        pedal_id = self.pedal_id
        self.pedal_mutex.unlock()
        return pedal_id

    @pedal_id.setter
    def pedal_id(self, Id):
        self.pedal_mutex.lock()
        self.pedal_id = Id
        self.pedal_mutex.unlock()

    @property
    def pedal_old(self):
        return self.pedal_old

    @pedal_old.setter
    def pedal_old(self, old_id):
        self.pedal_old = old_id