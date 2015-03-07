"""
Original code adapted from Pimoroni's example code.
github.com/pimoroni/unicorn-hat
Added try / except aspect
Created random brightness using uniform function
Added clean shutdown to turn off the blinkys!
"""

import unicornhat as u
from random import randint
from random import uniform



try:
    while True:
        u.rotation(90)
        x = randint(0, 7)
        y = randint(0, 7)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        bright = uniform(0.0, 1.0)
        u.brightness(bright)      
        u.set_pixel(x, y, r, g, b)
        u.show()
except KeyboardInterrupt:
    u.clean_shutdown()    
