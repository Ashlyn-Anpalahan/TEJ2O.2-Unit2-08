"""
Created by: Ashlyn
Created on: Feb 2026
This module will allow an RGB LED to scroll through different colors
"""

from microbit import *

# setup
display.clear()
display.show(Image.HAPPY)

# Button A
while True:
    if button_a.is_pressed():
        # Red
        pin13.write_digital(1)
        pin14.write_digital(0)
        pin15.write_digital(0)
        display.scroll("Red")
        sleep(1000)

        # Blue
        pin13.write_digital(0)
        pin14.write_digital(0)
        pin15.write_digital(1)
        display.scroll("Blue")
        sleep(1000)

        # Green
        pin13.write_digital(0)
        pin14.write_digital(1)
        pin15.write_digital(0)
        display.scroll("Green")
        sleep(1000)

        # Magenta
        pin13.write_digital(1)
        pin14.write_digital(0)
        pin15.write_digital(1)
        display.scroll("Magenta")
        sleep(1000)

        # Yellow
        pin13.write_digital(1)
        pin14.write_digital(1)
        pin15.write_digital(0)
        display.scroll("Yellow")
        sleep(1000)

        # Cyan
        pin13.write_digital(0)
        pin14.write_digital(1)
        pin15.write_digital(1)
        display.scroll("Cyan")
        sleep(1000)

        # White
        pin13.write_digital(1)
        pin14.write_digital(1)
        pin15.write_digital(1)
        display.scroll("White")
        sleep(1000)

        # Turn Off
        pin13.write_digital(0)
        pin14.write_digital(0)
        pin15.write_digital(0)
        sleep(1000)
