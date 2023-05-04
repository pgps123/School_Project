from tkinter import *

root = Tk()
root.title("test")
root.geometry("900x500")

test_var = StringVar()

test_radiobutton1 = Radiobutton(root, text="radio1", variable=test_var, value="radio1")
test_radiobutton1.select()
test_radiobutton2 = Radiobutton(root, text="radio2", variable=test_var, value = "radio2")
test_radiobutton3 = Radiobutton(root, text="radio3", variable=test_var, value="radio3")

test_radiobutton1.pack()
test_radiobutton2.pack()
test_radiobutton3.pack()


root.mainloop()