import RPi.GPIO as GPIO
import time
import thread
import Queue
import sys


def inputThread(queue):
    timer = time.time()
    while 1:
        # TODO interrupt when sequencer pressed (http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio)
        input = GPIO.input()
        queue.put(input)
        if timer - time.time() < 0.5:
            #TODO notice double tap and long tap


def firstTap():
    #TODO record

def furtherTap():
    #TODO record + play

def doubleTap(first):
    # TODO first=true -> stop recording + keep playing
    # TODO first=false -> firstTap() + keep playing

def longTap():
    # TODO stop

def main():
    queue = Queue()
    try:
        thread.start_new_thread(inputThread, queue)
    except:
        print "Error: unable to start thread"

    input = 0
    while 1:
        if queue.get() != input:
            # TODO select right function
            if input ==
            getattr(sys.modules[__name__], input)()
        else:
            time.sleep(0.01)



if __name__== "__main__":
    main()