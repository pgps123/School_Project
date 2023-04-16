from tkinter import *
from random import *
import tkinter.messagebox as messagebox

class dobak_system:
    def __init__(self, root):
        self.root = root
        self.root.title("포인트 도박")
        self.root.geometry("900x500")

        self.point_game()

    def point_game(self):
        self.hit = False
        self.point = 10000
        self.user_select = 0

        self.show_point_label = Label(self.root, text="현재 포인트 : {0}".format(self.point))

        self.show_point_label.pack()

        self.mul2_button = Button(self.root, text="X2, 50%", command=lambda: self.random_percent(50, 2))
        self.mul3_button = Button(self.root, text="X3, 40%", command=lambda: self.random_percent(40, 3))
        self.mul5_button = Button(self.root, text="X5, 30%", command=lambda: self.random_percent(30, 5))
        self.mul100_button = Button(self.root, text="X100, 1%", command=lambda: self.random_percent(1, 100))

        self.mul2_button.pack()
        self.mul3_button.pack()
        self.mul5_button.pack()
        self.mul100_button.pack()
        
    def random_percent(self, percent, value):
        self.percent = percent
        self.value = value
        self.temp = randint(1, 100)
        if self.temp <= self.percent:
            self.hit = True

        if self.hit:
            self.point *= self.value
            messagebox.showinfo("Information", "성공")
            self.show_point_label.config(text="현재 포인트 : {0}".format(self.point))
        else:
            self.point //= self.value
            messagebox.showinfo("Information", "실패")
            self.show_point_label.config(text="현재 포인트 : {0}".format(self.point))
        
        self.hit = False

if __name__ == "__main__":
    root = Tk()
    app = dobak_system(root)
    root.mainloop()