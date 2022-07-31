import tkinter
import random

window = tkinter.Tk()


def RandomNumber():
    MyRandom = random.randint(1, 6)
    dice_thrown.configure(text="Dice thrown: " + str(MyRandom))


MyTitle = tkinter.Label(window, text="Random Number Generator", font="Helvetica 16 bold")
MyTitle.pack()

MyButton = tkinter.Button(window, text="Roll", command=RandomNumber)
MyButton.pack()

dice_thrown = tkinter.Label(window, font="Helvetica 16 bold")
dice_thrown.pack()

window.mainloop()