# Add your Python code here. E.g.
from microbit import *

won = False
code1 = "ABAAB"
code2 = "ABBAB"
code3 = "BABBB"

def matchCode(Correct_code):
    Ans_Code = ""
    while len(Ans_Code) != len(Correct_code):
        if button_a.get_presses():
            Ans_Code += "A" 
        if button_b.get_presses():
            Ans_Code += "B"
    if Ans_Code == Correct_code:
        correct = True
    else:
        correct = False
    return correct  

while not won: 
    
    display.show("1")
    correct1 = matchCode(code1)
    if correct1 == True:
        display.show("2")
        correct2 = matchCode(code2)
        
        if correct2 == True:
            display.show("3")
            correct3 = matchCode(code3)
            if correct3 == True:
                display.scroll("You Won! Well Done!")
                won = True
            else:
                display.scroll("Wrong code - start again!")
        else:
            display.scroll("Wrong code - start again!")
    else:
        display.scroll("Wrong code - start again!")
        

    
        
        