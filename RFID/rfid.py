# RFID Reader
# 4/27/2019

import RPi.GPIO as GPIO
import time

# GPIO.setmode(GPIO.BCM)

# GPIO22 is SCL  pin
# GPIO27 is DIN pin
# GPIO17 is DOUT  pin

GPIO.setup(17, GPIO.IN)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

clk=GPIO.PWM(22,1200)
clk.start(50)

def init():
    if GPIO.input(17) == True:
        GPIO.output(27,False)
        
        
    
def main():
    while True:
        





    

#GPIO.setup(9, GPIO.IN)

#pi = pigpio.pi()
#pi.set_mode(9, pigpio.INPUT) # set port 9 as input



#setup the port
#pi = pigpio.pi(SCL,17)
#pi = pigpio.pi(DOUT,27)
#pi = pigpio.pi(DIN,22)
#pi.set_mode(17,pigpio.OUTPUT)
#pi.set_mode(27,pigpio.INPUT)
#pi.set_mode(22,pigpio.OUTPUT)
#def init():
 #   if pi.read(SCL)==1:
  #      pi.set_pull_down_up()
        
