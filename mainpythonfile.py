#importing modules
from tkinter import *
import mysql.connector
from tkinter import messagebox


login=Tk()
login.geometry('543x232+100+200')
login.maxsize(543,232)
login.minsize(532,232)
login.iconbitmap("iconpm.ico")
login.title('Login Page')
login.configure(bg='light blue')


def login_command():
    if mainpage_entry.get() == "" :
        mainpage_entry.delete(0, 'end')
        return mainwindow()
        print(mainwindow())

Label(login, text ="___Login___", font = "Monaco 20 bold",relief="ridge",bg="yellow", borderwidth=5).pack(fill = X)
Label(login, text="Master Key", font="Calibri 20 bold" ,bg ='light blue').place(x=8,y=55)
login_pass = StringVar()
mainpage_entry = Entry(login, textvariable=login_pass,show="*",font = "monaco 10 ")
mainpage_entry.pack(side ='top',ipadx=20 , ipady=10  ,pady=10)
Login_button=Frame(login, bg="#40a6c3", relief="sunken", borderwidth=5)
Login_button.pack(side="bottom",anchor="s")
Button(Login_button, text="Login",font="Dubai",command = login_command).grid(ipadx =50)


def mainwindow():
    root = Tk()
    root.geometry("570x532+700+220")
    root.iconbitmap("iconpm.ico")
    root.minsize(570, 532)
    root.maxsize(570, 532)

    root.title("Password Manager")
    '''
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="poah",
          database="password_manager"
                )
    '''

    def add():
        def add_entry():
            print(f"{websiteentry.get(), usernameentry.get(), passwordentry.get()}")
            messagebox.showinfo("Thankyou!", "Your details have been submitted")

            websiteentry.delete(0, 'end')
            usernameentry.delete(0, 'end')
            passwordentry.delete(0, 'end')

        def close():
            addwin.destroy()

        addwin = Tk()
        addwin.geometry("393x300+200+220")
        addwin.maxsize(393, 300)
        addwin.minsize(393, 300)
        addwin.configure(bg='#c5fad5')
        addwin.iconbitmap("iconpm.ico")
        addwin.title("New Entry")

        Label(addwin, text=" Website's Name ", font="Helvetica 12 bold", bg="#c5fad5").grid()
        Label(addwin, text="Username", font="Helvetica 12 bold", bg="#c5fad5").grid(row=1)
        Label(addwin, text="Password", font="Helvetica 12 bold", bg="#c5fad5").grid(row=2)

        Websiteval = StringVar()
        Usernameval = StringVar()
        Passwordval = StringVar()

        websiteentry = Entry(addwin, textvariable=Websiteval)
        usernameentry = Entry(addwin, textvariable=Usernameval)
        passwordentry = Entry(addwin, textvariable=Passwordval)

        websiteentry.grid(row=0, column=1, ipady=5, ipadx=5)
        usernameentry.grid(row=1, column=1, ipady=5, ipadx=5)
        passwordentry.grid(row=2, column=1, ipady=5, ipadx=5)
        button_frame = Frame(addwin, bg="#a8a4f5", relief="raised", borderwidth=6)
        button_frame.place(y=240)
        Button(button_frame, text="Submit", font="Dubai", command=add_entry).grid(row=0, ipadx=65)
        Button(button_frame, text="Close", font="Dubai", command=close).grid(row=0, column=1, ipadx=70)

        addwin.mainloop()

    def logoff():
        root.destroy()

#Defining previous data
    def prevdata():

        prev = Tk()
        prev.geometry("800x800")
        prev.maxsize(800, 800)
        prev.minsize(500, 500)
        prev.configure(bg='#f08080')
        prev.iconbitmap("iconpm.ico")
        prev.title("All Passwords")

        










        prev.mainloop()




    # main loop code
    frame_label = Frame(root, bg="#40a6c3", relief="groove", borderwidth=5)
    frame_label.pack(fill=X)
    Label(frame_label, text="Password Manager", font="Monaco 20 bold").pack()

    frame_button = Frame(root, bg="#40a6c3", relief="groove", borderwidth=5)
    frame_button.pack(side="bottom", anchor="s", fill=X)
    Button(frame_button, text="Add New", font="Monaco 15", command=add).grid(ipadx =20)
    Button(frame_button ,text="Show All Passwords",font="Monaco 15" ,command= prevdata).grid(row=0, column=1)
    Button(frame_button, text="Log Off", font="Monaco 15", command=logoff).grid(row=0, column=2 ,ipadx=40)

    # Image Source
    photo = PhotoImage(file="password.png",master=root)  #Great achivement --13 hrs
    bg =Label(root,image= photo)
    bg.image=photo
    bg.pack(padx=20,pady=20)

login.mainloop()
 