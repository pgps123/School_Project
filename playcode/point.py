from random import *
from tkinter import *

root = Tk()
root.title("포인트 도박")
root.geometry("640x480")

def randomPercent(a):
    global hit
    temp = randint(1, 100)
    if temp <= a:
        hit = True

root.mainloop()