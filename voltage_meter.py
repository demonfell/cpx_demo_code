# wiring instrucations at https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-analog-in

import time
import board
import analogio
 
analogin = analogio.AnalogIn(board.A1)
 
 
def getVoltage(pin):  # helper
    return (pin.value * 3.3) / 65536
 
 
while True:
    # Need to format as a tuple to plot values
    print((getVoltage(analogin),))
    time.sleep(0.1)# wiring instrucations at https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-analog-in

import time
import board
import analogio
 
analogin = analogio.AnalogIn(board.A1)
 
 
def getVoltage(pin):  # helper
    return (pin.value * 3.3) / 65536
 
 
while True:
    print("Analog Voltage: %f" % getVoltage(analogin))
    time.sleep(0.1)
