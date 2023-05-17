from tkinter import *
class test:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+300+100")
        self.root.resizable(False, False)
        self.root.title("test")
        self.window()

    def window(self):
        self.test_txt = Text(self.root).pack()

        self.test_button = Button(self.root, text="testButton", command=self.test_button_cmd).pack()

    def test_button_cmd(self):
        print(self.test_txt.get("1.0", END))
        self.test_button_cmd2()

    def test_button_cmd2(self):
        print(self.test_txt.get("1.0", END))



if __name__ == "__main__":
    root = Tk()
    test(root)
    root.mainloop()