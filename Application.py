import pyodbc
import tkinter as ttk


connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Abu\Documents\Programming\DatabaseStorage\LoginDatabank.accdb;')
print("Database Connected")
cur = connection.cursor()
cur.execute("SELECT * FROM Users")


def start_login():
    root = ttk.Tk()
    root.title("Login System")
    frm = ttk.Frame(root)
    frm.grid()
    ttk.Label(frm, text="Login!").grid(column=0, row=0)


    ttk.Label(frm, text="Username: ").grid(column=0, row=1)
    NameLabel = ttk.Entry(frm)
    NameLabel.grid(column=1, row=1)

    ttk.Label(frm, text="Password: ").grid(column=0, row=2)
    MailLabel = ttk.Entry(frm)
    MailLabel.grid(column=1, row=2)

    ttk.Label(frm, text="Password: ").grid(column=0, row=2)
    PassLabel = ttk.Entry(frm)
    PassLabel.grid(column=1, row=2)

    ReportLabel = ttk.Label(frm)
    ReportLabel.grid(column=0, row=7)

    def logged_in():
        NameLabel.destroy()
        PassLabel.destroy()
        MailLabel.destroy()
        ReportLabel.destroy()
        frm.destroy()

        Tk1 = ttk.Toplevel()
        frm1 = ttk.Frame(Tk1)
        frm1.grid()
        Tk1.title("System Access")

        ttk.Label(frm1, text="You have Successfully Logged In").grid(column=0, row=0)

        ttk.Label(frm1, text=":D").grid(column=0, row=1)
        Tk1.mainloop()

    def get_data():
        Name = NameLabel.get()
        Password = PassLabel.get()

        NameTable = None
        PassTable = None

        for row in cur.fetchall():
            if Name == row.Username and Password == row.Password:
                ReportLabel.configure(text="Successful")
                logged_in()
                break
            elif Name == "" or Password == "":
                ReportLabel.configure(text="Please enter a username and password")
            else:
                ReportLabel.configure(text="Incorrect username and password")
            

        

    ttk.Button(frm, text="Login", command=lambda: get_data(), height=1, width=10).grid(column=0, row=5)

    def add_data():
        Tk1 = ttk.Toplevel()
        frm1 = ttk.Frame(Tk1)
        frm1.grid()
        Tk1.title("Sign Up System")

        ttk.Label(frm1, text="Username: ").grid(column=0, row=0)
        NewNameLabel = ttk.Entry(frm1)
        NewNameLabel.grid(column=1, row=0)

        ttk.Label(frm1, text="E-Mail: ").grid(column=0, row=1)
        NewMailLabel = ttk.Entry(frm1)
        NewMailLabel.grid(column=1, row=1)

        ttk.Label(frm1, text="Password: ").grid(column=0, row=2)
        NewPassLabel = ttk.Entry(frm1)
        NewPassLabel.grid(column=1, row=2)

        ttk.Label(frm1, text="Confirm Password: ").grid(column=0, row=3)
        NewPassLabel1 = ttk.Entry(frm1)
        NewPassLabel1.grid(column=1, row=3)

        def confirm_addition():
            NewName = NewNameLabel.get()
            NewPass = NewPassLabel.get()
            NewMail = NewMailLabel.get()
            if NewPass == NewPassLabel1.get():

                index = 0
                for row in cur.fetchall():
                    index += 1
                    
                print("Successful")
                cur.execute("INSERT INTO Users VALUES (?, ?, ?, ?)", (index+1, NewName, NewMail, NewPass))
                connection.commit()
                Tk1.destroy()

        ttk.Button(frm1, text="Submit", command=lambda: confirm_addition()).grid(column=0, row=4)
        Tk1.mainloop()



    ttk.Button(frm, text="Make an Account", command=lambda: add_data(), height=1, width=15).grid(column=0, row=6)

    root.mainloop()

start_login()