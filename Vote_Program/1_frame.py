from tkinter import *

root = Tk()
root.title("문명투표함")
root.geometry("640x480")

root.resizable(False, False) # x,y 크기 변경 불가

frame_left = Frame(root, width=10, bd=1)

ID_label = Label(root, text="ID", width=5, height=2)
ID_entry = Entry(root, width=20)
PW_label = Label(root, text="PW", width=5, height=2)
PW_entry = Entry(root, width=20)
Login_button = Button(root, text="로그인", width=5, height=2)

ID_label.grid(row=0, column=0, padx=3, pady=3)
ID_entry.grid(row=0, column=1, padx=3, pady=3)
PW_label.grid(row=1, column=0, padx=3, pady=3)
PW_entry.grid(row=1, column=1, padx=3, pady=3)
Login_button.grid(row=2, column=0, columnspan=2, padx=3, pady=3)

root.mainloop()