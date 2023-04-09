from tkinter import *


class Window:

    def __init__(self, master):

        root.title("Sign Up or Login")
        root.minsize(width=300, height=300)
        root.maxsize(width=300,height=300)

        self.login_button = Button(master, text = "Login", width=18,height=4, command=self.LoginPage)
        self.signup_button = Button(master, text = "Sign Up", width=18,height=4, command=self.SignupPage)

        self.login_button.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.signup_button.place(relx=0.5, rely=0.7, anchor=CENTER)

    def LoginPage(self):
        root.title("Login")
        self.Restore()
    def SignupPage(self):
        root.title("Sign Up")
        self.Restore()
    def Restore(self):
            for widgets in root.winfo_children():
                widgets.destroy()


root = Tk()

run = Window(root)

root.mainloop()