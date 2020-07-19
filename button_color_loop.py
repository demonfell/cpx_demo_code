# connection instructions at https://learn.adafruit.com/make-it-switch/hook-up-your-switch

from digitalio import DigitalInOut, Direction, Pull
import time
import board
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)

colors_dict = {
'RED':(255, 0, 0), 
'YELLOW':(255, 150, 0),
'GREEN':(0, 255, 0),
'CYAN':(0, 255, 255),
'BLUE':(0, 0, 255),'PURPLE':(180, 0, 255),
'WHITE':(255, 255, 255),
'OFF':(0, 0, 0)
}

# button
button_1 = DigitalInOut(board.A1)
button_1.direction = Direction.INPUT
button_1.pull = Pull.UP
     
while True:
    if not button_1.value:
        for k,v in colors_dict.items():
            for i in range(0,10):
                led[i] = v
                time.sleep(0.5)
