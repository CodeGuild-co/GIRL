# Add your Python code here. E.g.
from microbit import *

#red_led = 0
#orange_led = 1
#yellow_led = 8
#green_led = 12

#red_switch = 4
#orange_switch = 6
#yellow_switch = 7
#green_switch = 3

#code = "BABBB"

def flash(colour):
    if colour == "r":
        pin0.write_digital(1)
        sleep(500)
        pin0.write_digital(0)
        sleep(500)
    elif colour == "g":
        pin12.write_digital(1)
        sleep(500)
        pin12.write_digital(0)
        sleep(500)
    elif colour == "o":
        pin1.write_digital(1)
        sleep(500)
        pin1.write_digital(0)
        sleep(500)
    elif colour == "y":
        pin8.write_digital(1)
        sleep(500)
        pin8.write_digital(0)
        sleep(500)


while True:
    display.off()
    if pin4.read_digital():
        flash("r")
    elif pin6.read_digital():
        flash("o")
    elif pin7.read_digital():
        flash("y")
    elif pin3.read_digital():
        flash("g")
    