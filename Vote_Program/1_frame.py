from tkinter import *
import pygame

root = Tk()
root.title("문명투표함")
root.geometry("900x480")

root.resizable(False, False) # x,y 크기 변경 불가

def Login_button_cmd():
    for widgets in root.winfo_children():
        widgets.destroy()
    Vote_window()

def Login_window():
    frame_login = Frame(root)
    frame_id = Frame(frame_login)
    frame_pw = Frame(frame_login)

    ID_label = Label(frame_id, text="ID", width=5, height=2)
    ID_entry = Entry(frame_id, width=20)
    PW_label = Label(frame_pw, text="PW", width=5, height=2)
    PW_entry = Entry(frame_pw, width=20, show="*")
    Login_button = Button(frame_login, text="로그인", width=25, height=1, command=Login_button_cmd)

    frame_login.pack(fill="none", expand=True)
    frame_id.pack(side="top")
    frame_pw.pack(side="top")

    ID_label.pack(side="left")
    ID_entry.pack(side="right")
    PW_label.pack(side="left")
    PW_entry.pack(side="right")
    Login_button.pack()

def Vote_window():
    frame_all_vote = LabelFrame(root, text="전학년 투표리스트", relief="solid", bd=1, width=300)
    frame_grade_vote = LabelFrame(root, text="학년 투표리스트", relief="solid", bd=1, width=300)
    frame_class_vote = LabelFrame(root, text="반 투표리스트", relief="solid", bd=1, width=300)

    frame_all_vote.pack(side="left", fill="y")
    frame_grade_vote.pack(side="left", fill="y")
    frame_class_vote.pack(side="left", fill="y")

Login_window()

root.mainloop()