import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Button, Entry
import tkinter.messagebox
import pandas as pd
# ==========================Main frame================================


def append_df_to_excel(df, excel_path):
    df_excel = pd.read_excel(excel_path)
    result = pd.concat([df_excel, df])
    result.to_excel(excel_path, index=False)


class Main():
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("\tLibrary Project\t")

        # ==========================variable Declaration================================

        self.page = StringVar()
        self.loginName = StringVar()
        self.loginPass = StringVar()
        self.signupName = StringVar()
        self.signupPass = StringVar()
        self.signupage = StringVar()
        self.signupemail = StringVar()
        self.signupno = StringVar()
        self.sts = StringVar()

        self.createWidgets()
        self.showlogin()

    # ==========================Frame Declaration================================

    def createWidgets(self):
        Label(self.parent, textvariable=self.page, font=("", 20)).pack()
        # ==========================Frame Declarations================================
        addbook = Frame(self.parent)
        delbook = Frame(self.parent)
        returnbook = Frame(self.parent)
        titleframe = Frame(returnbook, width=1650, padx=20, bd=5, relief=RIDGE)
        titleframe.pack()

        # ==========================Frame 1 (Log IN Frame)================================

        Label(addbook, text="Name", state=NORMAL).grid(sticky=W)
        Entry(addbook, textvariable=self.loginName).grid(row=0, column=1, pady=10, padx=10)
        Label(addbook, text="Password").grid(sticky=W)
        Entry(addbook, textvariable=self.loginPass, show="*").grid(row=1, column=1)
        Button(addbook, text="Login", command=self.login).grid(sticky=W, pady=10)
        Button(addbook, text="Sign Up", command=self.signup).grid(row=2, column=1, pady=10)
        Button(addbook, text="Exit", command=self.iexit).grid(row=2, column=2, pady=10)

        # ==========================Frame 2 (Sign In Frame)================================

        Label(delbook, text="Name").grid(sticky=W)
        Entry(delbook, textvariable=self.signupName).grid(row=0, column=1, pady=10, padx=10)
        Label(delbook, text="Password").grid(sticky=W)
        Entry(delbook, textvariable=self.signupPass, show="*", width=20).grid(row=1, column=1, pady=10)
        Label(delbook, text="Phone No.").grid(sticky=W)
        Entry(delbook, textvariable=self.signupno).grid(row=2, column=1, pady=10)
        Label(delbook, text="Email").grid(sticky=W)
        Entry(delbook, textvariable=self.signupemail).grid(row=3, column=1, pady=10)
        Label(delbook, text="Age").grid(sticky=W)
        Entry(delbook, textvariable=self.signupage).grid(row=4, column=1, pady=10)
        Button(delbook, text="Create", command=self.create).grid(sticky=W, pady=10)
        Button(delbook, text="Back", command=self.showlogin).grid(row=5, column=1, pady=10)
        Button(delbook, text="Exit", command=self.iexit).grid(sticky=W, row=5, column=2, pady=10)

        # ==========================Frame 3 (After Login Frame)================================

        dataframeleft = LabelFrame(returnbook, bd=10, width=1100, height=400, padx=10, relief=RIDGE, font=("", 12), text="Book Info:")
        dataframeleft.pack(side=LEFT)
        dataframeright = LabelFrame(returnbook, bd=10, width=500, height=400, padx=10, relief=RIDGE, font=("", 12), text="User Info:")
        dataframeright.pack(side=RIGHT)
        Button(returnbook, text='Borrow Book', command=self.borrow_book).pack(side=BOTTOM, )
        Button(returnbook, text='Return Book', command=self.return_book).pack(side=BOTTOM)
        Button(returnbook, text='Suggest Book', command=self.suggest_book).pack(side=BOTTOM)
        # ==========================Frame 3 (Right Frame)================================
        self.lblname = Label(dataframeright, text="Name :", padx=2, pady=2)
        self.lblname.grid(row=0, column=0, sticky=W)
        self.lblname = Entry(dataframeright)
        self.lblname.grid(row=0, column=1)

        self.lblname = Label(dataframeright, text="Address :", padx=2, pady=2)
        self.lblname.grid(row=1, column=0, sticky=W)
        self.lblname = Entry(dataframeright)
        self.lblname.grid(row=1, column=1)

        self.lblname = Label(dataframeright, text="Phone no : ", padx=2, pady=2)
        self.lblname.grid(row=2, column=0, sticky=W)
        self.lblname = Entry(dataframeright)
        self.lblname.grid(row=2, column=1)

        self.lblname = Label(dataframeright, text="E-mail : ", padx=2, pady=2)
        self.lblname.grid(row=3, column=0, sticky=W)
        self.lblname = Entry(dataframeright)
        self.lblname.grid(row=3, column=1)

        self.lblname = Label(dataframeright, text="Postal code :", padx=2, pady=2)
        self.lblname.grid(row=4, column=0, sticky=W)
        self.lblname = Entry(dataframeright)
        self.lblname.grid(row=4, column=1)

        # ==========================Frame 3 (LeftFrame)================================
        self.tree = ttk.Treeview(dataframeleft, height=15, padding=3)
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        vsb.place()
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree["columns"] = ("Column 1", "Column 2")
        self.tree.grid()
        self.tree.heading('#0', text='Name', anchor=W)
        # self.tree.heading("Column 1", text='Book Name', anchor='center')
        self.view_records()

        # ============================= Frame init ===========================
        self.loginFrame=addbook
        self.signupFrame=delbook
        self.stdloggedFrame=returnbook
        Label(self.parent, text="Library Management System", width=1650, padx=20, bd=5, relief=RAISED, font=("Monotype Corsiva", 40, 'bold')).pack(side=TOP)

# ==========================Function def===============================

    def login(self):
        name = self.loginName.get()
        password = self.loginPass.get()
        try:
            f = open("save_data", "r")
            cname, cpass = f.read().split(",")
            if name == cname and password == cpass:
                self.showstdlogged()

            else:
                tkinter.messagebox.showerror("ERROR", "Username or Password Error")
        except:
            self.sts.set("Wrong Name Or Password")

    def signup(self):
        self.loginFrame.pack_forget()
        self.signupFrame.pack()

    def showlogin(self):
        self.signupFrame.pack_forget()
        self.stdloggedFrame.pack_forget()
        self.loginFrame.pack()

    def showstdlogged(self):
        self.loginFrame.pack_forget()
        self.stdloggedFrame.pack()
        tkinter.messagebox.showinfo("Logged In", "Login Successful..!")

    def create(self):
        name = self.signupName.get()
        password = self.signupPass.get()
        age = self.signupage.get()
        number = self.signupno.get()
        email = self.signupemail.get()
        data = [[name, password, age, number, email]]
        df = pd.DataFrame(data, columns=('Name', 'Password', 'Age', 'Number', 'Email'))
        append_df_to_excel(df, 'testsheet.xls')
        self.showlogin()

    def iexit(self):
        iexit = tkinter.messagebox.askyesno("Library Management System", "Confirm..?")
        if iexit > 0:
            root.destroy()
            return

    def view_records(self):
        df = pd.read_excel('BookData.xls')
        for row in df.Name:
          self.tree.insert('', 0, text=row)

    def borrow_book(self):
        tkinter.messagebox.askyesno('Borrow Book')

    def return_book(self):
        tkinter.messagebox.askyesno('return book')

    def suggest_book(self):
        tkinter.messagebox.askyesno('Suggest book')
# ==========================Main frame in loop================================


if __name__ == "__main__":
    root = Tk()
    root.title('Library Management System')
    root.geometry("1350x750+0+0")
    Main(root)
    root.mainloop()

# code by Little_Jerry All Rights Reserved
