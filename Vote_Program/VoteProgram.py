from tkinter import *
import tkinter.messagebox as messagebox

class VotingSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x480+300+100")
        self.root.resizable(False, False)

        self.login_window()

    def login_window(self):
        self.root.title("로그인")

        self.frame_login = Frame(self.root)
        self.frame_id = Frame(self.frame_login)
        self.frame_pw = Frame(self.frame_login)

        self.ID_label = Label(self.frame_id, text="ID", width=5, height=2)
        self.ID_entry = Entry(self.frame_id, width=20)
        self.PW_label = Label(self.frame_pw, text="PW", width=5, height=2)
        self.PW_entry = Entry(self.frame_pw, width=20, show="*")
        self.login_button = Button(self.frame_login, text="로그인", width=25, height=1, command=self.voting_list_window)

        self.frame_login.pack(fill="none", expand=True)
        self.frame_id.pack(side="top")
        self.frame_pw.pack(side="top")

        self.ID_label.pack(side="left")
        self.ID_entry.pack(side="right")
        self.PW_label.pack(side="left")
        self.PW_entry.pack(side="right")
        self.login_button.pack()

    def voting_list_window(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()

        self.root.title("투표 리스트")

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
            self.listbox_all.insert(END, i[0:-1])
        for i in self.grade_list:
            self.listbox_grade.insert(END, i[0:-1])
        for i in self.class_list:
            self.listbox_class.insert(END, i[0:-1])

        self.f.close()

    def result_button_cmd(self, temp):
        self.open_voting_file = open(self.user_select[:-1], "r", encoding="utf8")
        
        self.voting_number = self.open_voting_file.readline()
        self.voting_number_list = list(map(int, self.voting_number.split()))

        self.open_voting_file.close()

        self.temp = temp
        self.max_value = -1
        for i in range(len(self.voting_number_list)):
            if self.voting_number_list[i] > self.max_value:
                self.max_value = self.voting_number_list[i]

        for i in range(len(self.voting_number_list)):
            if self.voting_number_list[i] == self.max_value:
                messagebox.showinfo("Information", "가장 많은 표를 획득한 사람(것)은 {0}입니다.".format(self.temp[self.user_select_index + 1 + i]))

    def voting_window_by_all_list(self):
        self.root.title(self.user_select[:-1])

        self.candidate_number = IntVar()

        for widgets in self.root.winfo_children():
            widgets.destroy()
        
        if self.all_list_detail[self.user_select_index][-2] == "1":
            self.voting_question = Label(self.root, text=self.all_list_detail[self.user_select_index + 1][:-1]).pack()
            self.question_index = Text(self.root).pack()
            self.finish_button = Button(self.root, text="설문 완료", command=lambda: self.finish_question_cmd(self.all_list_detail)).pack()
        else:
            for i in range(int(self.all_list_detail[self.user_select_index][-2])):
                self.voting_index = Radiobutton(self.root, text=self.all_list_detail[self.user_select_index + i + 1], variable=self.candidate_number, value=i).pack()
            self.finish_button = Button(self.root, text="투표 완료", command=self.finish_voting_cmd).pack()

            self.result_button = Button(self.root, text="결과 확인", command=lambda: self.result_button_cmd(self.all_list_detail)).pack()

        self.return_button = Button(self.root, text="돌아가기", command=self.voting_list_window).pack()

    def voting_window_by_grade_list(self):
        self.root.title(self.user_select[:-1])

        self.candidate_number = IntVar()

        for widgets in self.root.winfo_children():
            widgets.destroy()
        
        if self.grade_list_detail[self.user_select_index][-2] == "1":
            self.voting_question = Label(self.root, text=self.grade_list_detail[self.user_select_index + 1][:-1]).pack()
            self.question_index = Text(self.root).pack()
            self.finish_button = Button(self.root, text="설문 완료", command=lambda: self.finish_question_cmd(self.grade_list_detail)).pack()
        else:
            for i in range(int(self.grade_list_detail[self.user_select_index][-2])):
                self.voting_index = Radiobutton(self.root, text=self.grade_list_detail[self.user_select_index + i + 1], variable=self.candidate_number, value=i).pack()
            self.finish_button = Button(self.root, text="투표 완료", command=self.finish_voting_cmd).pack()

        self.return_button = Button(self.root, text="돌아가기", command=self.voting_list_window).pack()

    def voting_window_by_class_list(self):
        self.root.title(self.user_select[:-1])

        self.candidate_number = IntVar()

        for widgets in self.root.winfo_children():
            widgets.destroy()
        
        if self.class_list_detail[self.user_select_index][-2] == "1":
            self.voting_question = Label(self.root, text=self.class_list_detail[self.user_select_index + 1][:-1]).pack()
            self.question_index = Text(self.root).pack()
            self.finish_button = Button(self.root, text="설문 완료", command=lambda: self.finish_question_cmd(self.class_list_detail)).pack()
        else:
            for i in range(int(self.class_list_detail[self.user_select_index][-2])):
                self.voting_index = Radiobutton(self.root, text=self.class_list_detail[self.user_select_index + i + 1], variable=self.candidate_number, value=i).pack()
            self.finish_button = Button(self.root, text="투표 완료", command=self.finish_voting_cmd).pack()

        self.return_button = Button(self.root, text="돌아가기", command=self.voting_list_window).pack()

    def finish_question_cmd(self, temp):
        self.temp = temp
        self.open_question = open(self.user_select[:-1], "r", encoding="utf8")

        self.open_question_list = self.open_question.readlines()

        self.open_question.close()

        self.open_question = open(self.user_select[:-1], "w", encoding="utf8")

        print(type(self.question_index))
        # self.open_question_list.append(self.question_index.get("1.0", END))
        for i in self.open_question_list:
            self.open_question.writelines(i)

        self.open_question.close()

    def finish_voting_cmd(self):
        self.open_voting_file = open(self.user_select[:-1], "r", encoding="utf8")
        
        self.voting_number = self.open_voting_file.readline()
        self.voting_number_list = list(map(int, self.voting_number.split()))
        self.voting_select = self.candidate_number.get()

        self.open_voting_file.close()

        self.voting_number_list[self.voting_select] += 1

        self.finish_voting_write_cmd()

    def finish_voting_write_cmd(self):
        self.write_voting_file = open(self.user_select[:-1], "w", encoding="utf8")

        for i in range(len(self.voting_number_list)):
            self.write_voting_file.writelines("{0} ".format(self.voting_number_list[i]))
        messagebox.showinfo("Information", "투표가 완료되었습니다.")

        self.write_voting_file.close()

    def select_button_cmd(self):
        if self.listbox_all.curselection():
            self.user_select = self.all_list[self.listbox_all.curselection()[0]]
            self.open_all_list_detail = open("vote_all_list.txt", "r", encoding="utf8")
            self.all_list_detail = self.open_all_list_detail.readlines()

            for i in self.all_list_detail:
                if i == "\n":
                    self.all_list_detail.remove("\n")

            for i in range(len(self.all_list_detail)):
                if self.all_list_detail[i][:-2] == self.user_select[:-1] or self.all_list_detail[i][:-2] == self.user_select or self.all_list_detail[i] == self.user_select[:-1] or self.all_list_detail[i] == self.user_select:
                    self.user_select_index = i
                    break
            
            self.voting_window_by_all_list()

            self.open_all_list_detail.close()

        elif self.listbox_grade.curselection():
            self.user_select = self.grade_list[self.listbox_grade.curselection()[0]]
            self.open_grade_list_detail = open("vote_grade_list.txt", "r", encoding="utf8")
            self.grade_list_detail = self.open_grade_list_detail.readlines()

            for i in self.grade_list_detail:
                if i == "\n":
                    self.grade_list_detail.remove("\n")

            for i in range(len(self.grade_list_detail)):
                if self.grade_list_detail[i][:-2] == self.user_select[:-1] or self.grade_list_detail[i][:-2] == self.user_select or self.grade_list_detail[i] == self.user_select[:-1] or self.grade_list_detail[i] == self.user_select:
                    self.user_select_index = i
                    break

            self.voting_window_by_grade_list()
            
            self.open_grade_list_detail.close()

        elif self.listbox_class.curselection():
            self.user_select = self.class_list[self.listbox_class.curselection()[0]]
            self.open_class_list_detail = open("vote_class_list.txt", "r", encoding="utf8")
            self.class_list_detail = self.open_class_list_detail.readlines()

            for i in self.class_list_detail:
                if i == "\n":
                    self.class_list_detail.remove("\n")

            for i in range(len(self.class_list_detail)):
                if self.class_list_detail[i][:-2] == self.user_select[:-1] or self.class_list_detail[i][:-2] == self.user_select or self.class_list_detail[i] == self.user_select[:-1] or self.class_list_detail[i] == self.user_select:
                    self.user_select_index = i
                    break

            self.voting_window_by_class_list()

            self.open_class_list_detail.close()

        else:
            messagebox.showwarning("Warning", "선택한 값이 없습니다.")

if __name__ == "__main__":
    root = Tk()
    app = VotingSystem(root)
    root.mainloop()

    