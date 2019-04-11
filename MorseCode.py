# Add your Python code here. E.g.
from microbit import *


correct = False

question = "CODE:- .-- --- / .--. .-.. ..- ... / ..-. .. ...- . ..--.."
Correct_answer = ".......-.-."
answer = ""
answered = False

while not correct:
    while not answered:
        display.scroll(question)
        if button_a.get_presses():
            answered = True
    
    while len(answer) < len(Correct_answer):   
        if button_a.get_presses():
            answer += "." 
            display.show(".")
        if button_b.get_presses():
            answer += "-" 
            display.show("-")
    if answer != Correct_answer: 
        display.show("X")
    else:
        display.scroll("Well done")
        correct = True 

while correct == True :
    display.scroll("ABAAB")

