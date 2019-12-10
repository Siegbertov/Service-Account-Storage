from tkinter import *
from tkinter import messagebox


class password_window(object):
    attemps = 0

    def __init__(self, master):
        self.top = Toplevel(master)
        top = self.top
        top.title("Enter Password")
        top.geometry("{}x{}".format(300, 100))
        top.resizable(width=False, height=False)

        self.l = Label(top, text="Your Password", font=fonttxt, justify=CENTER)
        self.l.place(rely=0.05, relx=0.1, relheight=0.25, relwidth=0.8)

        self.e = Entry(top, show="*")
        self.e.place(rely=0.35, relx=0.1, relheight=0.25, relwidth=0.8)

        self.b = Button(top, text="Submit", font=fonttxt, command=self.check)
        self.b.place(rely=0.65, relx=0.1, relheight=0.25, relwidth=0.8)

    def check(self):
        self.value = self.e.get()
        pw = "sieg"

        if self.value == pw:
            self.top.destroy()
            root.deiconify()
        else:
            self.attemps += 1
            if self.attemps == 5:
                root.quit()
            self.e.delete(0, END)
            messagebox.showerror("Wrong Password", "Attemps left: {}".format(5 - self.attemps))


root = Tk()
root.title("Service Account Storage")
root.geometry("{}x{}+{}+{}".format(400, 400, 100, 100))
fonttxt = ("Helvetica", "16")

# Comment those two lines if you don't want to write password
root.withdraw()
pw = password_window(root)

root.mainloop()