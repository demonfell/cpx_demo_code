import time
import board
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 3, brightness=0.2)

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

for k,v in colors_dict.items():
    for i in range(0,9):
        led[i] = v
        time.sleep(0.5)
