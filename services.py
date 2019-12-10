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


def add_account():
    ser = serviceE.get()
    log = loginE.get()
    passw = passwordE.get()

    if ser == "" or log == "" or passw == "":
        messagebox.showerror("Error", "You forget something")
    elif (" " in log) or (" " in passw):
        messagebox.showerror("Error", "Login or Password couldn't contains space")
    else:

        f = open('accounts.txt', "a")
        f.write(ser + ", " + log + ", " + passw + "\n")
        f.close()

        txt = "service: {}\nlogin: {}\npassword: {}\nSuccessfully Added".format(ser, log, passw)
        messagebox.showinfo("New Account", txt)

        serviceE.delete(0, END)
        loginE.delete(0, END)
        passwordE.delete(0, END)


def show_accounts():
    account_window = Toplevel(root)
    account_window.title("Accounts")
    account_window.geometry("+{}+{}".format(550, 100))
    account_window.resizable(width=False, height=False)

    f = open("accounts.txt", "r")
    f.seek(0)
    for line in f.readlines():
        ser, log, passw = line.split(", ")
        ser, log, passw = ser.strip(), log.strip(), passw.strip()
        txt = "{}\n{} {}\n".format(ser, log, passw)
        Label(account_window, text=txt).pack(ipadx=10, ipady=10)


root = Tk()
root.title("Service Account Storage")
root.geometry("{}x{}+{}+{}".format(400, 400, 100, 100))
fonttxt = ("Helvetica", "16")

# Comment those two lines if you don't want to write password
root.withdraw()
pw = password_window(root)

lbl = Label(root, text="Add Account", font=fonttxt)
lbl.place(rely=0.05, relx=0.05, relheight=0.1, relwidth=0.9)

service = Label(root, text="Service:", font=fonttxt, anchor=E)
service.place(rely=0.2, relx=0.05, relheight=0.1, relwidth=0.3)
serviceE = Entry(root, bd=2)
serviceE.place(rely=0.2, relx=0.35, relheight=0.1, relwidth=0.6)

login = Label(root, text="Login:", font=fonttxt, anchor=E)
login.place(rely=0.35, relx=0.05, relheight=0.1, relwidth=0.3)
loginE = Entry(root, bd=2)
loginE.place(rely=0.35, relx=0.35, relheight=0.1, relwidth=0.6)

password = Label(root, text="Password:", font=fonttxt, anchor=E)
password.place(rely=0.5, relx=0.05, relheight=0.1, relwidth=0.3)
passwordE = Entry(root, bd=2)
passwordE.place(rely=0.5, relx=0.35, relheight=0.1, relwidth=0.6)

sbmt = Button(root, text="Add", font=fonttxt, command = add_account)
sbmt.place(rely=0.7, relx=0.1, relheight=0.1, relwidth=0.8)

show = Button(root, text="Show", font=fonttxt, command = show_accounts)
show.place(rely=0.85, relx=0.1, relheight=0.1, relwidth=0.8)

root.mainloop()