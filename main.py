# Rock Paper Scissors Game
from tkinter import *
import random

conclusion = 'Select any option to start\n\n'  # To declare result
yourLives = 3
comLives = 3

def gameCloser():
    buttonRock.grid_forget()
    buttonPaper.grid_forget()
    buttonScissors.grid_forget()
    buttonReplay.grid(row = 1, columnspan = 3)

def rockGame(event):
    playGame(0)

def paperGame(event):
    playGame(1)

def scissorsGame(event):
    playGame(2)

def playGame(selection):
    comChoice = random.choice([0,1,2])
    global yourLives
    global comLives
    global conclusion
    if selection==0 and comChoice==0:
        conclusion = 'Computer Chose Rock\nDraw'

    elif selection==0 and comChoice==1:
        conclusion = 'Computer Chose Paper\nComputer Wins'
        yourLives-=1

    elif selection==0 and comChoice==2:
        conclusion = 'Computer Chose Scissors\nYou Win'
        comLives-=1

    elif selection==1 and comChoice==0:
        conclusion = 'Computer Chose Rock\nYou Win'
        comLives-=1

    elif selection==1 and comChoice==1:
        conclusion = 'Computer Chose Paper\nDraw'

    elif selection==1 and comChoice==2:
        conclusion = 'Computer Chose Scissors\nComuter Wins'
        yourLives-=1

    elif selection==2 and comChoice==0:
        conclusion = 'Computer Chose Rock\nComputer Wins'
        yourLives-=1

    elif selection==2 and comChoice==1:
        conclusion = 'Computer Chose Paper\nYou Win'
        comLives-=1

    else:
        conclusion = 'Computer Chose Scissors\nDraw'

    if yourLives==0:
        conclusion = 'Better Luck Next Time\nYou Lost'
        gameCloser()
    elif comLives==0:
        conclusion = 'Congratulations!!\nYou Won'
        gameCloser()
    
    label2.config(text = 'Your Lives = ' + str(yourLives))
    label3.config(text = "Computer's Lives = " + str(comLives))
    label4.config(text = conclusion)

def replayGame(event):
    global conclusion
    global yourLives
    global comLives
    conclusion = 'Select any option to start\n\n'
    yourLives = 3
    comLives = 3
    buttonReplay.grid_forget()
    label2.config(text = 'Your Lives = ' + str(yourLives))
    label3.config(text = "Computer's Lives = " + str(comLives))
    label4.config(text = conclusion)
    buttonRock.grid(row = 1, column = 0)
    buttonPaper.grid(row = 1, column = 1)
    buttonScissors.grid(row = 1, column = 2)

window = Tk()
window.title('Rock Paper Scissors')

mainFrame = Frame(window, width = 100)
mainFrame.pack()

label1 = Label(mainFrame, text = "Let's play the game")
label1.grid(row = 0, columnspan = 3)

photoRock = PhotoImage(file = 'rock.png')
photoPaper = PhotoImage(file = 'paper.png')
photoScissors = PhotoImage(file = 'scissors.png')

# Lives Information
label2 = Label(mainFrame,text = 'Your Lives = ' + str(yourLives))
label23 = Label(mainFrame,text = '|')
label3 = Label(mainFrame,text = "Computer's Lives = " + str(comLives))
label2.grid(row = 2, column = 0)
label23.grid(row = 2, column = 1)
label3.grid(row = 2, column = 2)

# Result Information
label4 = Label(mainFrame, text = conclusion)
label4.grid(row = 3, columnspan = 3)

# RPS buttons
buttonRock = Button(mainFrame, text = 'Rock', image = photoRock)
buttonRock.bind('<Button-1>', rockGame)
buttonRock.grid(row = 1, column = 0)

buttonPaper = Button(mainFrame, text = 'Paper', image = photoPaper)
buttonPaper.bind('<Button-1>', paperGame)
buttonPaper.grid(row = 1, column = 1)

buttonScissors = Button(mainFrame, text = 'Scissors', image = photoScissors)
buttonScissors.bind('<Button-1>', scissorsGame)
buttonScissors.grid(row = 1, column = 2)

# Replay button
buttonReplay = Button(mainFrame, text = 'Replay')
buttonReplay.bind('<Button-1>',replayGame)

window.mainloop()