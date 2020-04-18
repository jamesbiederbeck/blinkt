#!/usr/bin/env python
#Take number between 0 and 1 and graph it on the blinkt
#Values floored at 0 and celing at 1
import fileinput
import math
import time

import blinkt


blinkt.set_clear_on_exit()

def show_graph(v, r, g, b):
    v *= blinkt.NUM_PIXELS
    for x in range(blinkt.NUM_PIXELS):
        if v < 0:
            r, g, b = 0, 0, 0
        else:
            r, g, b = [int(min(v,1.0) * c) for c in [r, g, b]]
        blinkt.set_pixel(x, r, g, b)
        v -= 1

    blinkt.show()

blinkt.set_brightness(0.1)

try:
    for line in fileinput.input():
        v = float(str(line))
        print("graphing ",v)
        show_graph(v, 255, 0, 255)

except KeyboardInterrupt:
    pass

