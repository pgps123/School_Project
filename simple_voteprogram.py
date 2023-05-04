from tkinter import *

class mini_voteprogram:
    def __init__(self, root):
        self.root = root
        self.root.title("test")
        self.root.geometry("900x500+300+100")
        self.root.resizable(False, False)

        self.show_screen()

    def show_screen(self):
        self.people_var = IntVar()
        self.main_label = Label(self.root, text="반장선거")
        self.people1_radio = Radiobutton(self.root, text="people1", variable=self.people_var, value=1)
        self.people2_radio = Radiobutton(self.root, text="people2", variable=self.people_var, value=2)
        self.people3_radio = Radiobutton(self.root, text="people3", variable=self.people_var, value=3)

        self.main_label.pack()
        self.people1_radio.pack()
        self.people2_radio.pack()
        self.people3_radio.pack()

        self.select_button = Button(self.root, text="선택", command=self.select_button_cmd)

        self.select_button.pack()

    def select_button_cmd(self):
        self.read_file = open("mini_vote_list", "r", encoding="utf8")
        self.write_file = open("mini_vote_list", "w", encoding="utf8")
        self.mini_vote_list = list(map(int, self.read_file.readline().split()))
        self.people1_voting = self.mini_vote_list[0]
        self.people2_voting = self.mini_vote_list[1]
        self.people3_voting = self.mini_vote_list[2]
        self.user_select = self.people_var.get()

        if self.user_select == 1:
            self.people1_voting += 1
        elif self.user_select == 2:
            self.people2_voting += 1
        elif self.user_select == 3:
            self.people3_voting += 1

        self.write_file.write("{0} {1} {2}".format(self.people1_voting, self.people2_voting, self.people3_voting))

        self.read_file.close()
        self.write_file.close()

if __name__ == "__main__":
    root = Tk()
    mini_voteprogram(root)
    root.mainloop()