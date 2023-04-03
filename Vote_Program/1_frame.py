from tkinter import *

root = Tk()
root.title("문명투표함")
root.geometry("640x480")
#root.geometry("640x480+300+100") # 가로 세로 x좌표 y좌표

root.resizable(False, False) # x,y 크기 변경 불가

Login_frame = Frame(root)
Login_frame.pack(fill="x", padx=5, pady=5)
ID_etr = Entry(root, width=30).pack()
PW_etr = Entry(root, width=30, show="*").pack()
Login_btn = Button(root, padx=50, pady=10, text="login").pack()

root.mainloop()