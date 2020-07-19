touch_pad = board.A1  # For Circuit Playground Express

led = neopixel.NeoPixel(board.NEOPIXEL, 3, brightness=0.2)

touch = touchio.TouchIn(touch_pad)

colors_dict = {
'RED':(255, 0, 0), 
'YELLOW':(255, 150, 0),
'GREEN':(0, 255, 0),
'CYAN':(0, 255, 255),
'BLUE':(0, 0, 255),
'PURPLE':(180, 0, 255),
'WHITE':(255, 255, 255),
'OFF':(0, 0, 0)
}

while True:
    if touch.value:
        led[0] = colors_dict['RED']
        time.sleep(0.5)
        led[1] = colors_dict['GREEN']
        time.sleep(0.5)
        led[2] = colors_dict['BLUE']
        time.sleep(0.5)
    time.sleep(0.5)import time

import board
import touchio
import neopixel

# touch_pad = board.A0  # Will not work for Circuit Playground Express!
touch_pad = board.A1  # For Circuit Playground Express

led = neopixel.NeoPixel(board.NEOPIXEL, 3, brightness=0.2)

touch = touchio.TouchIn(touch_pad)

while True:
    if touch.value:
        led[0] = (255, 0, 0)
        time.sleep(0.5)
        led[1] = (0, 255, 0)
        time.sleep(0.5)
        led[2] = (0, 0, 255)
        time.sleep(0.5)
    time.sleep(0.5)


