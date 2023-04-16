from tkinter import *
import tkinter.messagebox as massagebox

class VotingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("문명투표함")
        self.root.geometry("900x480")
        self.root.resizable(False, False)

        self.login_window()

    def login_window(self):
        self.frame_login = Frame(self.root)
        self.frame_id = Frame(self.frame_login)
        self.frame_pw = Frame(self.frame_login)

        self.ID_label = Label(self.frame_id, text="ID", width=5, height=2)
        self.ID_entry = Entry(self.frame_id, width=20)
        self.PW_label = Label(self.frame_pw, text="PW", width=5, height=2)
        self.PW_entry = Entry(self.frame_pw, width=20, show="*")
        self.login_button = Button(self.frame_login, text="로그인", width=25, height=1, command=self.login_button_cmd)

        self.frame_login.pack(fill="none", expand=True)
        self.frame_id.pack(side="top")
        self.frame_pw.pack(side="top")

        self.ID_label.pack(side="left")
        self.ID_entry.pack(side="right")
        self.PW_label.pack(side="left")
        self.PW_entry.pack(side="right")
        self.login_button.pack()

    def voting_window(self):
        self.f = open("vote_list.txt", "r", encoding="utf8")
        self.f_list = self.f.readlines()
        for i in self.f_list:
            if i == "\n":
                self.f_list.remove("\n")

        for i in range(len(self.f_list)):
            if self.f_list[i] == '전교생 투표 리스트\n' or self.f_list[i] == '전교생 투표 리스트':
                self.value1 = i
            elif self.f_list[i] == '학년 투표 리스트\n' or self.f_list[i] == '학년 투표 리스트':
                self.value2 = i
            elif self.f_list[i] == '반 투표 리스트\n' or self.f_list[i] == '반 투표 리스트':
                self.value3 = i

        self.all_list = self.f_list[self.value1 + 1:self.value2]
        self.grade_list = self.f_list[self.value2 + 1:self.value3]
        self.class_list = self.f_list[self.value3 + 1:]

        self.select_button = Button(root, text="선택", command=self.select_button_cmd)

        self.select_button.pack(side=BOTTOM)

        self.frame_all_vote = LabelFrame(self.root, text="전학년 투표리스트", relief="solid", bd=1, width=300)
        self.frame_grade_vote = LabelFrame(self.root, text="학년 투표리스트", relief="solid", bd=1, width=300)
        self.frame_class_vote = LabelFrame(self.root, text="반 투표리스트", relief="solid", bd=1, width=300)

        self.frame_all_vote.pack(side=LEFT, fill=Y)
        self.frame_grade_vote.pack(side=LEFT, fill=Y)
        self.frame_class_vote.pack(side=LEFT, fill=Y)

        self.listbox_all = Listbox(self.frame_all_vote, selectmode="single", height=0, width=42)
        self.listbox_grade = Listbox(self.frame_grade_vote, selectmode="single", height=0, width=42)
        self.listbox_class = Listbox(self.frame_class_vote, selectmode="single", height=0, width=42)

        self.listbox_all.pack(fill=BOTH, expand=True)
        self.listbox_grade.pack(fill=BOTH, expand=True)
        self.listbox_class.pack(fill=BOTH, expand=True)

        for i in self.all_list:
            self.listbox_all.insert(END, i)
        for i in self.grade_list:
            self.listbox_grade.insert(END, i)
        for i in self.class_list:
            self.listbox_class.insert(END, i)

    def select_all(self):
        self.open_file = open("vote_all_list.txt", "r", encoding="utf8")
            
    def login_button_cmd(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()

        self.voting_window()

    def select_button_cmd(self):
        if self.listbox_all.curselection():
            self.user_select = self.all_list[self.listbox_all.curselection()[0]]
            self.select_all()

        elif self.listbox_grade.curselection():
            self.user_select = self.grade_list[self.listbox_grade.curselection()[0]]

        elif self.listbox_class.curselection():
            self.user_select = self.class_list[self.listbox_class.curselection()[0]]

        else:
            massagebox.showwarning("Warning", "선택한 값이 없습니다.")

if __name__ == "__main__":
    root = Tk()
    app = VotingSystem(root)
    root.mainloop()
