#! /bin/env python

# food_weight.py
# Jean P Walker
# weighing food function

from hx711 import HX711
import RPi.GPIO as GPIO
import sys
import time

# Calibration of force sensor
calib = 1
sck = 21
dout = 20

def weight_initialize():
    sensor = HX711(dout, sck)
    sensor.set_reading_format("MSB", "MSB")
    sensor.set_reference_unit(calib)
    sensor.reset()
    sensor.tare()
    return (0, sensor)

def weight_food(sensor):
    while (True):
        try:
            print sensor.get_weight()
        except:
            weight_shutdown()
        time.sleep(.1)

def weight_shutdown():
    GPIO.cleanup()
    sys.exit()
