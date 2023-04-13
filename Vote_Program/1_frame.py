from tkinter import *

f = open("vote_list.txt", "r", encoding="utf8")
f_list = f.readlines()
for i in f_list:
    if i == "\n":
        f_list.remove("\n")

for i in range(len(f_list)):
    if f_list[i] == '전교생 투표 리스트\n':
        value1 = i
    elif f_list[i] == '학년 투표 리스트\n':
        value2 = i
    elif f_list[i] == '반 투표 리스트\n':
        value3 = i

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

    for i in range(value1 + 1, value2):
        button_all = Button(frame_all_vote, text=f_list[i], width=41).pack(side="top", fill="x")
    for i in range(value2 + 1, value3):
        button_grade = Button(frame_grade_vote, text=f_list[i], width=41).pack(side="top", fill="x")
    for i in range(value3 + 1, len(f_list) - 1):
        button_class = Button(frame_class_vote, text=f_list[i], width=41).pack(side="top", fill="x")

Login_window()

f.close()

root.mainloop()