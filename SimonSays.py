# Add your Python code here. E.g.
from microbit import *
import random

#red_led = 0
#orange_led = 1
#yellow_led = 8
#green_led = 12

#red_switch = 4
#orange_switch = 6
#yellow_switch = 7
#green_switch = 3

code = "BABBB"

correctSeq = "#"
currentSeq = "#"

def genRandomColour():
    i = random.randint(0, 3)
    if i == 0:
        return "r"
    elif i == 1:
        return "o"
    elif i == 2:
        return "y"
    elif i == 3:
        return "g"

def appendRandomSequence(length):
    global correctSeq
    for i in range(0, length):
        if correctSeq == "#":
            correctSeq = genRandomColour()
        else:
            correctSeq += genRandomColour()

def flash(colour):
    if colour == "#":
        return

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

def flashAll():
    pin0.write_digital(1)
    pin12.write_digital(1)
    pin1.write_digital(1)
    pin8.write_digital(1)
    sleep(500)
    pin0.write_digital(0)
    pin12.write_digital(0)
    pin1.write_digital(0)
    pin8.write_digital(0)

def enterCode(colour):
    if colour == "#":
        return
    
    global currentSeq
    #display.on()
    if currentSeq == "#":
        currentSeq = colour
    else:
        currentSeq = currentSeq + colour
    
    #display.off()
    #flash(colour)

display.off()
pin4.read_digital()
pin6.read_digital()
pin7.read_digital()
pin3.read_digital()

def flashSeq():
    for char in correctSeq:
        flash(char)

appendRandomSequence(3)


i = 0
while i < 3:
    appendRandomSequence(1)
    flashSeq()
    while correctSeq != currentSeq:
        lastchar = "#"
        if pin4.read_digital():
            lastchar = "r"
        elif pin6.read_digital():
            lastchar = "o"
        elif pin7.read_digital():
            lastchar = "y"
        elif pin3.read_digital():
            lastchar = "g"
    
        enterCode(lastchar)
        if (correctSeq[len(currentSeq) - 1] != currentSeq[len(currentSeq) - 1]) and (currentSeq != "#"):
            flashAll()
            currentSeq = "#"
            #display.on()
            correctSeq = "#"
            appendRandomSequence(4)
            #display.off()
            i = 0
            sleep(500)
            flashSeq()
        else:
            flash(lastchar)
    
    currentSeq = "#"
    i += 1

#flashAll()

display.on()
while True:
    display.scroll(code)
