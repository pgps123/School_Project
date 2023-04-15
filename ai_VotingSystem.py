import tkinter as tk

class VotingSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Voting System")

        self.items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

        self.create_widgets()

    def create_widgets(self):
        # 리스트 박스
        self.listbox = tk.Listbox(self.master, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, padx=10, pady=10)
        for item in self.items:
            self.listbox.insert(tk.END, item)

        # 투표 버튼
        self.vote_button = tk.Button(self.master, text="Vote", command=self.vote)
        self.vote_button.pack(side=tk.LEFT, padx=10, pady=10)

        # 결과 라벨
        self.result_label = tk.Label(self.master, text="No vote")
        self.result_label.pack(side=tk.LEFT, padx=10, pady=10)

    def vote(self):
        selection = self.listbox.curselection()
        if len(selection) == 0:
            return
        item = self.items[selection[0]]
        self.result_label.config(text="You voted for {}".format(item))

if __name__ == "__main__":
    root = tk.Tk()
    app = VotingSystem(root)
    root.mainloop()
