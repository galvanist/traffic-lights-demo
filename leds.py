import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#red
GPIO.setup(7,GPIO.OUT)
#amber
GPIO.setup(11,GPIO.OUT)
#green
GPIO.setup(15,GPIO.OUT)

#wait for now
GPIO.output(7,True)
time.sleep(5)

#ready steady...
GPIO.output(7,True)
GPIO.output(11,True)
time.sleep(3)

#go go go...
GPIO.output(7,False)
GPIO.output(11,False)
GPIO.output(15,True)
time.sleep(5)

#slow...
GPIO.output(7,False)
GPIO.output(11,True)
GPIO.output(15,False)
time.sleep(2)

#stop and wait
GPIO.output(7,True)
GPIO.output(11,False)
GPIO.output(15,False)
