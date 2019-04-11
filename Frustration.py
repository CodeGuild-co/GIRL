# Add your Python code here. E.g.
from microbit import *

gameFinished = False

while True:
    if button_a.was_pressed():
        gameFinished = False
        continue
    
    if not gameFinished:
        if pin8.read_digital():
            display.show(Image.SAD)
            pin12.write_analog(512)
            continue
        else:
            display.show(Image.HAPPY)
            pin12.write_analog(0)
        
        if pin0.read_digital():
            gameFinished = True
    else:
        display.scroll("ABBAB")
        sleep(500)
