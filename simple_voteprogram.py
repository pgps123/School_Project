from tkinter import *
import tkinter.messagebox as messagebox

class mini_voteprogram:
    def __init__(self, root):
        self.root = root
        self.root.title("test")
        self.root.geometry("900x500+300+100")
        self.read_file = open("mini_vote_list", "r", encoding="utf8")
        
        self.mini_vote_list = list(map(int, self.read_file.readline().split()))
        self.people1_voting = self.mini_vote_list[0]
        self.people2_voting = self.mini_vote_list[1]
        self.people3_voting = self.mini_vote_list[2]
        self.read_file.close()
        self.show_screen()

    def show_screen(self):
        self.people_var = IntVar()
        self.main_label = Label(self.root, text="반장선거")
        self.people_list = ["후보1", "후보2", "후보3"]
        self.people1_radio = Radiobutton(self.root, text="후보1", variable=self.people_var, value=1)
        self.people2_radio = Radiobutton(self.root, text="후보2", variable=self.people_var, value=2)
        self.people3_radio = Radiobutton(self.root, text="후보3", variable=self.people_var, value=3)

        self.main_label.pack()
        self.people1_radio.pack()
        self.people2_radio.pack()
        self.people3_radio.pack()

        self.select_button = Button(self.root, text="선택", command=lambda: self.select_button_cmd1())
        self.result_button = Button(self.root, text="결과 확인", command=lambda: self.result_button_cmd())

        self.select_button.pack()
        self.result_button.pack()

    def select_button_cmd1(self):
        self.read_file = open("mini_vote_list", "r", encoding="utf8")
        
        self.mini_vote_list = list(map(int, self.read_file.readline().split()))
        
        self.user_select = self.people_var.get()

        self.read_file.close()

        self.hit = True
        if self.user_select == 1:
            self.mini_vote_list[0] += 1
        elif self.user_select == 2:
            self.mini_vote_list[1] += 1
        elif self.user_select == 3:
            self.mini_vote_list[2] += 1
        else:
            messagebox.showerror("Error", "선택한 값이 없습니다.")
            self.hit = False

        self.people1_voting = self.mini_vote_list[0]
        self.people2_voting = self.mini_vote_list[1]
        self.people3_voting = self.mini_vote_list[2]
        

        if self.hit:
            self.select_button_cmd2()

    def select_button_cmd2(self):
        self.write_file = open("mini_vote_list", "w", encoding="utf8")

        self.write_file.write("{0} {1} {2}".format(self.people1_voting, self.people2_voting, self.people3_voting))
        messagebox.showinfo("Information", "투표가 완료되었습니다.")

        self.write_file.close()

    def result_button_cmd(self):
        self.max_result = max(self.people1_voting, self.people2_voting, self.people3_voting)
        self.result_list = []

        for i in range(3):
            print("i")
            if self.mini_vote_list[i] == self.max_result:
                self.result_list.append(i)
        
        for i in self.result_list:
            messagebox.showinfo("Infomation", "투표수가 가장 많은 사람은 {0}님 입니다.".format(self.people_list[i]))

        self.result_list = []

if __name__ == "__main__":
    root = Tk()
    mini_voteprogram(root)
    root.mainloop()

    