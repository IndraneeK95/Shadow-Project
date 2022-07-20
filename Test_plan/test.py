from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import tkinter.messagebox as msg
import mysql.connector
import ast
import tkinter as tkf
from  tkinter import messagebox
import os
import subprocess
import robot
import webbrowser
from tkinter import ttk
from tkinter import filedialog
from datetime import date
import shutil

Dict = {1: 'bidi_transf.robot', 2: 'call_data_On_case.robot', 3: 'check_IPV4_case.robot', 4:'check_IPV6_case.robot', 5:'download_speed_case.robot', 6:'mag_data_On_case.robot', 7:'send_a_msg_case.robot'}
list1 = ['1']
today = date.today()
test_run_no = 0
initial_path='/home/indranee/Mobile application/Test_suite/'
test_sel_by_num=False



def first_page():
    def register():
        window = Tk()
        window.title("SignUp")
        window.geometry("900x750+100+50")
        window.configure(bg='#fff')
        window.resizable(False, False)
        img = PhotoImage(file="register.png", master=window)
        Label(window, image=img, border=0, bg='white').place(x=70, y=200)

        img1 = ImageTk.PhotoImage(file="LT.jpg", master=window)
        Label(window, image=img1, border=0, bg='white').pack()

        frame = Frame(window, width=350, height=390, bg='#fff')
        frame.place(x=480, y=180)

        heading = Label(frame, text="Register", fg="#57a1f8", bg="white", font=("Microdoft Yahei UI Light", 23, 'bold'))
        heading.place(x=100, y=5)

        def on_enter(e):
            user.delete(0, 'end')

        def on_leave(e):
            if user.get() == '':
                   user.insert(0, 'Username')

        user = Entry(frame, fg='black', border=0, bg='white', font=("Microdoft Yahei UI Light", 11))
        user.place(x=80, y=80)
        user.insert(0, 'Username')
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=75, y=107)

        ##################################################################
        def on_enter(e):
            password.delete(0, 'end')
            password.config(show='*')

        def on_leave(e):
            if password.get() == '':
                   password.insert(0, 'Password')

        password = Entry(frame, fg='black', border=0, bg='white', font=("Microdoft Yahei UI Light", 11))
        password.place(x=80, y=150)
        password.insert(0, 'Password')
        password.bind("<FocusIn>", on_enter)
        password.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=75, y=177)

        ##############################################################################
        def on_enter(e):
            email.delete(0, 'end')

        def on_leave(e):
            if email.get() == '':
                email.insert(0, 'Email')

        email = Entry(frame, fg='black', border=0, bg='white', font=("Microdoft Yahei UI Light", 11))
        email.place(x=80, y=220)
        email.insert(0, 'Email')
        email.bind("<FocusIn>", on_enter)
        email.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=75, y=247)

        Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', cursor="hand2", fg='white', border=0,
               command=register_user).place(x=75, y=280)
    def login():
        window = Tk()
        window.title("SignIn")
        window.geometry("900x750+100+50")
        window.configure(bg='#fff')
        window.resizable(False, False)
        window.img = PhotoImage(file="login.png", master=window)
        Label(window, image=window.img, border=0, bg='white').place(x=50, y=200)

        img1 = ImageTk.PhotoImage(file="LT.jpg", master=window)
        Label(window, image=img1, border=0, bg='white').pack()

        frame = Frame(window, width=350, height=390, bg='#fff')
        frame.place(x=480, y=180)

        heading = Label(frame, text="Login", fg="#57a1f8", bg="white", font=("Microdoft Yahei UI Light", 23, 'bold'))
        heading.place(x=100, y=5)

        def on_enter(e):
            user_login.delete(0, 'end')

        def on_leave(e):
            if user_login.get() == '':
                user_login.insert(0, 'Username')

        user_login = Entry(frame, fg='black', border=0, bg='white', font=("Microdoft Yahei UI Light", 11))
        user_login.place(x=80, y=80)
        user_login.insert(0, 'Username')
        user_login.bind("<FocusIn>", on_enter)
        user_login.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=75, y=107)

    ##################################################################
        def on_enter(e):
            login_password.delete(0, 'end')
            login_password.config(show='*')

        def on_leave(e):
            if login_password.get() == '':
                login_password.insert(0, 'Password')

        login_password = Entry(frame, fg='black', border=0, bg='white', font=("Microdoft Yahei UI Light", 11))
        login_password.place(x=80, y=150)
        login_password.insert(0, 'Password')
        login_password.bind("<FocusIn>", on_enter)
        login_password.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=75, y=177)

        Button(frame, width=39, pady=7, text='Sign In', bg='#57a1f8', cursor="hand2", fg='white', command=login_user,
           border=0).place(x=75, y=207)

        Button(frame, text="Forget Password?", cursor="hand2", bg="white", fg="#d77337", bd=0, font=("times new roman", 10),
           command=forget_password).place(x=160, y=250)

    def forget_password():
        window = Tk()
        window.title("Forget Password")
        window.geometry("900x750+100+50")
        window.configure(bg='#fff')
        window.resizable(False, False)
        window.img = PhotoImage(file="sign1.png", master=window)
        Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)

        frame = Frame(window, width=350, height=390, bg='#fff')
        frame.place(x=480, y=70)

        heading = Label(frame, text="Change Password", fg="#57a1f8", bg="white",
                        font=("Microdoft Yahei UI Light", 20, 'bold', 'italic'))
        heading.place(x=90, y=5)

        def on_enter(e):
            email.delete(0, 'end')

        def on_leave(e):
            if email.get() == '':
                email.insert(0, 'Email')

        email = Entry(frame, fg='black', border=0, bg='white', font=("Microdoft Yahei UI Light", 11))
        email.place(x=80, y=80)
        email.insert(0, 'Email')
        email.bind("<FocusIn>", on_enter)
        email.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=75, y=107)

        ##################################################################
        def on_enter(e):
            New_password.delete(0, 'end')

        def on_leave(e):
            if New_password.get() == '':
                New_password.insert(0, 'New Password')

        New_password = Entry(frame, fg='black', border=0, bg='white', font=("Microdoft Yahei UI Light", 11))
        New_password.place(x=80, y=150)
        New_password.insert(0, 'New Password')
        New_password.bind("<FocusIn>", on_enter)
        New_password.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=75, y=177)

        Button(frame, width=39, pady=7, text='Reset Password', bg='#57a1f8', cursor="hand2", fg='white',
               border=0).place(x=75, y=207)

    def register_user():
        mydb = mysql.connector.connect(host='localhost', port='3306', user='root', password='indranee123',
                                       database='register_login')
        mycursor = mydb.cursor()

        username = user.get()
        password = password.get()
        email = email.get()

        mycursor.execute("insert into register values(%s,%s,%s)", (username, password, email))
        mydb.commit()

        msg.showinfo("Registration details", "Registered successfully")

    def login_user():
        mydb = mysql.connector.connect(host='localhost', port='3306', user='root', password='indranee123',
                                       database='register_login')
        mycursor = mydb.cursor()

        username1 = user_login.get()
        password1 = login_password.get()

        mycursor.execute("select * from register where username=%s and password=%s", (username1, password1))

        c = 0
        for i in mycursor:
            c = c + 1

        if c >= 1:
            mycursor.execute("insert into login values(%s,%s)", (username1, password1))
            mydb.commit()
            mycursor.execute(second_page())

        else:
            msg.showinfo("login details", "Invalid credentials")

    def forget_user():
        mydb = mysql.connector.connect(host='localhost', port='3306', user='root', password='indranee123',
                                       database='register_login')
        mycursor = mydb.cursor()

        username2 = email.get()
        new_password =New_password.get()

    def about():
        about = Tk()
        about.title("About")
        about.geometry("900x750+100+50")

    root = Tk()
    root.title("Homepage")
    root.geometry("900x750+100+50")
    root.configure(bg='#fff')
    root.resizable(False, False)
    # self.img = PhotoImage(file="sign1.png", master= root)
    root.bg = ImageTk.PhotoImage(file="ltts2.jpg")
    Label(root, image=root.bg, border=0, bg='white').place(x=0, y=0)

    title = Label(root, text="Welcome to L&T Technology Services Field test tool", bd='5', width="60",
                  fg="#63666A", bg='white', font=("Arial", 18, 'italic', 'bold'))
    title.pack()

    About_button = Button(root, text="About", cursor='hand2', bd="3", height="2", width="10",
                          font=("Microdoft Yahei UI Light", 11), command=about)
    About_button.place(x=550, y=60)

    register_button = Button(root, text="Register", cursor='hand2', bd="3", height="2", width="10",
                             font=("Microdoft Yahei UI Light", 11), command=register)
    register_button.place(x=670, y=60)

    login_button = Button(root, text="Login", cursor='hand2', bd="3", height="2", width="10",
                          font=("Microdoft Yahei UI Light", 11), command=login)
    login_button.place(x=790, y=60)





def second_page():
    def op1():
        window.destroy()
        field_page()

    def op2():
        window.destroy()
        devices_check()

    def op3():
        window.destroy()
        login_page()


    def op4():
        window.destroy()


    def op5():
        window.destroy()

    def reports_check():
        #   window.destroy()
            filename = filedialog.askopenfilename(
            initialdir="/home/indranee/Mobile application/Reports/",
            title="Select the report file",
            filetypes=(("Text files",
                        "*.txt*"),
                       ("all files",
                        "*.*")))
            webbrowser.open_new_tab(filename)

    window = Tk()
    window.title("Second Page")
    window.geometry("1000x750+100+50")
    window.configure(bg='#fff')
    window.resizable(False, False)
    window.img = PhotoImage(file="sign.png", master=window)
    Label(window, image=window.img, border=0, bg='white').place(x=50, y=60)
    window.img2 = PhotoImage(file="test_l.png", master=window)
    Label(window, image=window.img2, border=0, bg='white').place(x=50, y=460)
    Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)


    frame = Frame(window, width=350, height=390, bg='#fff')
    frame.place(x=550, y=70)

    heading = Label(frame, text="Field Test Tool", fg="#57a1f8", bg="white",
                    font=("Microdoft Yahei UI Light", 23, 'italic', 'bold'))
    heading.place(x=40, y=5)

    bt1 = Button(frame, text="Field Test", bg="#014b88", fg='black', bd='5', height="2", width="25", cursor='hand2',
                 font=("Microdoft Yahei UI Light", 11, 'bold'), command=op1)
    bt1.place(x=40, y=90)

    bt2 = Button(frame, text="Check Connected Devices", bg="#014b88", fg='black', bd='5', height="2", width="25",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=op2)
    bt2.place(x=40, y=160)

    bt3 = Button(frame, text="Reports", bg="#014b88", fg='black', bd='5', height="2", width="25", cursor='hand2',
                 font=("Microdoft Yahei UI Light", 11, 'bold'),command=reports_check)
    bt3.place(x=40, y=230)
    bt4 = Button(frame, text="Back", bg="#014b88", fg='black', bd='5', height="2", width="25", cursor='hand2',
                 font=("Microdoft Yahei UI Light", 11, 'bold'), command=op3)
    bt4.place(x=40, y=300)
    window.mainloop()

#########







##################################################################



##############################################################################


###############################################################################################




def field_page():
    def op1():
        window.destroy()
        create_field()

    def op2():
        window.destroy()
        exist_field()


    def op3():
        window.destroy()
        second_page()

    window = Tk()
    window.title("Field Page")
    window.geometry("1000x750+100+50")
    window.configure(bg='#fff')
    window.resizable(False, False)
    window.img = PhotoImage(file="sign.png", master=window)
    Label(window, image=window.img, border=0, bg='white').place(x=50, y=60)
    window.img2 = PhotoImage(file="test_l.png", master=window)
    Label(window, image=window.img2, border=0, bg='white').place(x=50, y=460)
    Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)

    frame = Frame(window, width=350, height=390, bg='#fff')
    frame.place(x=480, y=70)

    heading = Label(frame, text="Field Test Tool", fg="#57a1f8", bg="white",
                    font=("Microdoft Yahei UI Light", 23, 'italic', 'bold'))
    heading.place(x=40, y=5)

    bt1 = Button(frame, text="Create test run", bg="white", fg='black', bd='5', height="2", width="25", cursor='hand2',
                 font=("Microdoft Yahei UI Light", 11, 'bold'), command=op1)
    bt1.place(x=40, y=90)

    bt2 = Button(frame, text="Check Existing run", bg="#014b88", fg='black', bd='5', height="2", width="25",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=op2)
    bt2.place(x=40, y=160)


    bt3 = Button(frame, text="Back", bg="white", fg='black', bd='5', height="2", width="25",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=op3)
    bt3.place(x=40, y=230)
    window.mainloop()

def create_field():
    def op1():
        window.destroy()
        test_plan()

    def op2():
        window.destroy()
        field_page()

    window = Tk()
    window.title("Create Field Page")
    window.geometry("1000x750+100+50")
    window.configure(bg='#fff')
    window.resizable(False, False)
    window.img = PhotoImage(file="sign.png", master=window)
    Label(window, image=window.img, border=0, bg='white').place(x=50, y=60)
    window.img2 = PhotoImage(file="test_l.png", master=window)
    Label(window, image=window.img2, border=0, bg='white').place(x=50, y=460)
    Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)
    frame = Frame(window, width=350, height=390, bg='#fff')
    frame.place(x=480, y=70)

    heading = Label(frame, text="Enter the details", fg="#57a1f8", bg="white",
                    font=("Microdoft Yahei UI Light", 23, 'italic', 'bold'))
    heading.place(x=40, y=5)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        if user.get() == '':
            user.insert(0, 'Product Version')


    user = Entry(frame, fg='black',width='30', border=0, bg='#57a1f8', font=("Microdoft Yahei UI Light", 11), bd=5, relief='raised')
    user.place(x=40, y=80)
    user.insert(0, 'Product Version')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        if user.get() == '':
            user.insert(0, 'OS Type')

    user = Entry(frame, fg='black', width='30', border=0, bg='#57a1f8', font=("Microdoft Yahei UI Light", 11),bd=5, relief='raised')
    user.place(x=40, y=120)
    user.insert(0, 'OS Type')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        if user.get() == '':
            user.insert(0, 'Android Version')

    user = Entry(frame, fg='black', border=0, width='30', bg='#57a1f8', font=("Microdoft Yahei UI Light", 11),bd=5, relief='raised')
    user.place(x=40, y=160)
    user.insert(0, 'Android Version')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        if user.get() == '':
            user.insert(0, 'H/w type')

    user = Entry(frame, fg='black', border=0, width='30',  bg='#57a1f8', font=("Microdoft Yahei UI Light", 11), bd=5, relief='raised')

    user.place(x=40, y=200)
    user.insert(0, 'H/W type')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)
    bt1 = Button(frame, text="Test selector", bg="#014b88", fg='black', bd='5', height="2", width="25", cursor='hand2',
                 font=("Microdoft Yahei UI Light", 11, 'bold'), command=op1)
    bt1.place(x=40, y=240)
    bt2 = Button(frame, text="Back", bg="#014b88", fg='black', bd='5', height="2", width="25", cursor='hand2',command=op2)
    bt2.place(x=40, y=320)

    window.mainloop()

def test_plan():

    def test_plan_selector():
        global test_run_no
        test_run_no = test_run_no + 1
        path = filedialog.askdirectory()
        print(path)
        files = os.listdir(path)
        print(files)
        i = 0
        length = len(files)
        while i < length:
            list1.append(files[i])
            i = i + 1


    def select_single_file():
        global test_run_no
        test_run_no = test_run_no + 1
        filename = filedialog.askopenfilename(initialdir="/home/indranee/Mobile application/Test_suite/",
                                              title="Select a File",
                                              filetypes=(("Text files",
                                                          "*.txt*"),
                                                         ("all files",
                                                          "*.*")))

        print(filename)
        list1.append(filename)

    def select_multiple_file():
        global test_run_no
        test_run_no = test_run_no + 1
        messagebox.showinfo("showinfo", "Please press Control to select multiple files")
        filename = filedialog.askopenfilenames(initialdir="/home/indranee/Mobile application/Test_suite/",
                                               title="Select a File",
                                               filetypes=(("Text files",
                                                           "*.txt*"),
                                                          ("all files",
                                                           "*.*")))

        print(filename)
        i = 0
        length = len(filename)
        print(length)
        while i < length:
            print(filename[i])
            list1.append(filename[i])
            i = i + 1

    def test_run():
        if(test_run_no==0):
           messagebox.showinfo("showinfo", "Please select atleast one test file before clicking on run")
           return
        length = len(list1)
        print(length)
        i = 1

        # Iterating using while loop
        while i < length:
            file_exec = list1[i]
            print(file_exec)
            i = i + 1
            messagebox.showinfo("showinfo", "Your selected test case run started")
            logFile = open('mylog.txt', 'w')
            robot.run(file_exec)

            messagebox.showinfo("showinfo", "Your selected test case run has successfully ended")
            # file_exec = file_exec[::-1]
            file_exec = file_exec.split('/')
            print(file_exec)
            report_file = file_exec[-1] + str(today)
            report_file = report_file + '.html'
            print(report_file)
            path = '/home/indranee/Mobile application/Reports/TC77_4G LTE Lab_' + str(today)
            isdir = os.path.isdir(path)
            if (isdir == False):
                os.mkdir(path)
            with open('/home/indranee/Mobile application/Test_suite/report.html', 'r') as firstfile, open(
                    path + '/' + report_file, 'w') as secondfile:

                for line in firstfile:
                    # write content to second file
                    secondfile.write(line)

    def op1():
        window.destroy()
        field_page()

    def test_by_num():
        window.destroy()
        test_select_num()

    window = Tk()
    window.title("Create run field Page")
    window.title("Exist Field Page")
    window.geometry("1000x900+100+50")
    window.configure(bg='#fff')
    window.resizable(False, False)
    window.img = PhotoImage(file="sign.png", master=window)
    Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)
    window.img2 = PhotoImage(file="test2l.png", master=window)
    Label(window, image=window.img2, border=0, bg='white').place(x=80, y=660)
    window.img3 = PhotoImage(file="test2l.png", master=window)
    Label(window, image=window.img3, border=0, bg='white').place(x=500, y=660)
    frame = Frame(window, width=350, height=550, bg='#fff')
    frame.place(x=480, y=40)

    frame = Frame(window, width=350, height=550, bg='#fff')
    frame.place(x=480, y=70)

    heading = Label(frame, text="Field Test Tool", fg="#57a1f8", bg="white",
                    font=("Microdoft Yahei UI Light", 23, 'italic', 'bold'))
    heading.place(x=40, y=5)
    bt1 = Button(frame, text="Select single test file run", bg="#014b88", fg='black', bd='5', height="2", width="25", cursor='hand2',
                 font=("Microdoft Yahei UI Light", 11, 'bold'), command=select_single_file)
    bt1.place(x=40, y=90)

    bt2 = Button(frame, text="Select multiple file run", bg="#014b88", fg='black', bd='5', height="2", width="25",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=select_multiple_file)
    bt2.place(x=40, y=160)

    bt3 = Button(frame, text="Select test plan folder", bg="#014b88", fg='black', bd='5', height="2", width="25",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=test_plan_selector)
    bt3.place(x=40, y=240)



    bt3 = Button(frame, text="Select test by number", bg="white", fg='black', bd='5', height="2", width="25",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=test_by_num)
    bt3.place(x=40, y=300)
    bt3 = Button(frame, text="Run", bg="#57a1f8", fg='black', bd='5', height="2", width="25",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=test_run)
    bt3.place(x=40, y=360)
    bt3 = Button(frame, text="Back", bg="#57a1f8", fg='black', bd='5', height="2", width="25",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=op1)
    bt3.place(x=40, y=420)
    window.mainloop()



def exist_field():
    def status_open():
        window.destroy()
        status()
        #os.system('scrcpy')

    def progress():
        subprocess.call(['gnome-terminal'])




    def ret():
        window.destroy()
        field_page()

    window = Tk()
    window.title("existing run page")
    window.geometry("900x800+100+50")
    window.configure(bg='white')
    window.resizable(False, False)

    img = PhotoImage(file="sign.png")
    Label(window, image=img, border=0, bg='white').place(x=10, y=80)
    window.img2 = PhotoImage(file='lt4_2.png', master=window)
    Label(window, image=window.img2, border=0, bg='white').place(x=5, y=550)


    frame = Frame(window, width=800, height=500, bg='white')
    frame.place(x=450, y=70)


    b1 = Button(frame, width=39, height=1, pady=7, text='Completion status', bg='#57a1f8', fg='white', border=2, bd=5,
                relief='raised', command=progress).place(x=75,y=70)
    b1 = Button(frame, width=39, height=1, pady=7, text='Status', bg='#57a1f8', fg='white', border=2, bd=5,
                relief='raised', command=status_open).place(x=75, y=150)
   # b3 = Button(frame, width=39, pady=7, text='Reports', bg='#57a1f8', fg='white', border=0).place(x=75, y=250)
    b1 = Button(frame, width=39, pady=2, height=1,  text='Back', bg='#57a1f8', fg='white', border=2, bd=5,
                relief='raised', command=ret).place(x=75, y=240)

    window.mainloop()


def devices_check():
    def op2():
        t = subprocess.check_output("adb devices", shell=True)
        t = t.decode('utf-8')
        window.destroy()
        op3(t)


    def op3(t):
        def ret_here():
            window.destroy()
            devices_check()
        window= Tk()
        window.title("Devices check Page")
        window.geometry("900x600+100+50")
        window.configure(bg='#fff')
        window.resizable(False, False)

        img = PhotoImage(file="sign.png")
        Label(window, image=img, border=0, bg='#0000CD').place(x=10, y=80)
        l2 = Label(window, text=t, bg="#fff", fg='black', bd='5', relief='raised', borderwidth='5', width="40",
                   height="15", font=("Times New Roman", 13))

        l2.place(x=450,y=80)
        b1 = Button(frame, width=10, pady=7, text='Back', bg='#57a1f8', fg='white', border=0,
                    relief='raised', command=ret_here)
        b1.place(x=300, y=100)
        window.mainloop()

    def ret():
        window.destroy()
        second_page()

    window = Tk()
    window.title("Devices Options page")
    window.geometry("900x900+100+50")
    window.geometry("1200x600+100+50")
    window.configure(bg='#fff')
    window.resizable(False, False)

    img = PhotoImage(file="sign.png")
    Label(window, image=img, border=0, bg='#0000CD').place(x=10, y=80)
    window.img2 = PhotoImage(file='lt4_2.png', master=window)
    Label(window, image=window.img2, border=0, bg='white').place(x=1, y=550)
    frame = Frame(window, width=500, height=500, bg='#fff')
    frame.place(x=400, y=70)

    heading = Label(frame, text="Devices page", fg="#57a1f8", bg="white", relief='raised',
                    font=("Microdoft Yahei UI Light", 23, 'bold'))
    heading.place(x=80, y=5)
    b1 = Button(frame, width=39,height=2, pady=7, text='Check Connected devices', bg='#57a1f8', fg='white', border=0,bd=5, relief='raised', command=op2).place(
        x=75, y=70)
    b1 = Button(frame, width=39, height=2, pady=7, text='Assign new device', bg='#57a1f8', fg='white', border=0,
                bd=5, relief='raised', command=op2).place(
        x=75, y=150)
    b1 = Button(frame, width=39, height=2, pady=7, text='Back', bg='#57a1f8', fg='white', border=0,
                bd=5, relief='raised', command=op2).place(
        x=75, y=250)

    window.mainloop()


def login_page():


    window = Tk()
    window.title("Login page")
    window.geometry("1200x900+100+50")
    window.configure(bg='#fff')
    window.resizable(False, False)

    def signup():
        username = user.get()
        pass_word = password.get()
        confirm_password = confirm.get()

        if pass_word == confirm_password:
            try:
                file = open('datasheet.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {username: password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open("datasheet.txt", 'w')
                w = file.write(str(r))

                messagebox.showinfo('Signup', 'Successfully sign up')
            except:
                file = open("datasheet.txt", 'w')
                pp = str({'Username': 'password'})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror('Invalid', "Both Password should match")

    ###############################################################
    def SignIn():
        username = user.get()
        pass_word = password.get()
        confirm_password = confirm.get()
        if pass_word == confirm_password:
            if username=='Indranee' and pass_word=='indranee' :
                window.destroy()
                second_page()


    def callback(url):
        webbrowser.open_new_tab(url)

    ################################################################

    img = PhotoImage(file="sign.png")
    Label(window, image=img, border=0, bg='white').place(x=50, y=80)
    heading1 = Label(window, text="Important links", fg="#57a1f8", bg="white",
                    font=("Microdoft Yahei UI Light", 23, 'bold'))
    heading1.place(x=50, y=550)
    link1 = Label(window, text="www.microsoftOffice.com", font=('Times New Roman', 15,'bold','italic'), fg="black", bg="white", cursor="hand2")
    link1.place(x=50, y=600)
    link1.bind("<Button-1>", lambda e:
    callback("https://www.office.com/"))
    link2 = Label(window, text="www.rainbow.ltts.com", font=('Times New Roman', 15, 'bold', 'italic'), fg="black",
                  bg="white", cursor="hand2")
    link2.place(x=50, y=650)
    link2.bind("<Button-1>", lambda e:
    callback("https://rainbow.ltts.com/"))
    link3 = Label(window, text="www.microsoftOutlook.com", font=('Times New Roman', 15, 'bold', 'italic'), fg="black",
                  bg="white", cursor="hand2")
    link3.place(x=50, y=700)
    link3.bind("<Button-1>", lambda e:
    callback("https://www.microsoft.com/en-in/microsoft-365/outlook/email-and-calendar-software-microsoft-outlook"))
    link4 = Label(window, text="www.google.com", font=('Times New Roman', 15, 'bold', 'italic'), fg="black",
                  bg="white", cursor="hand2")
    link4.place(x=50, y=750)
    link4.bind("<Button-1>", lambda e:
    callback("https.//google.com"))
    frame1 = Frame(window, width=350, height=390, bg='#fff')
    frame1.place(x=600, y=70)

    heading = Label(frame1, text="Enter credentials", fg="#57a1f8", bg="white", font=("Microdoft Yahei UI Light", 23, 'bold'))
    heading.place(x=50, y=5)



    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        if user.get() == '':
            user.insert(0, 'Username')

    user = Entry(frame1, fg='black', border=0, bg='white', font=("Microdoft Yahei UI Light", 11))
    user.place(x=80, y=80)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame1, width=295, height=2, bg='black').place(x=75, y=107)

    ##################################################################
    def on_enter(e):
        password.delete(0, 'end')

    def on_leave(e):
        if password.get() == '':
            password.insert(0, 'Password')

    password = Entry(frame1, fg='black', border=0, bg='white', font=("Microdoft Yahei UI Light", 11), show='*')
    password.place(x=80, y=150)
    password.insert(0, 'Password')
    password.bind("<FocusIn>", on_enter)
    password.bind("<FocusOut>", on_leave)

    Frame(frame1, width=295, height=2, bg='black').place(x=75, y=177)

    ##############################################################################
    def on_enter(e):
        confirm.delete(0, 'end')

    def on_leave(e):
        if confirm.get() == '':
            confirm.insert(0, 'Confirm Password')

    confirm = Entry(frame1, fg='black', border=0, bg='white', font=("Microdoft Yahei UI Light", 11))
    confirm.place(x=80, y=220)
    confirm.insert(0, 'Confirm Password')
    confirm.bind("<FocusIn>", on_enter)
    confirm.bind("<FocusOut>", on_leave)

    Frame(frame1, width=295, height=2, bg='black').place(x=75, y=247)
    ####
    Button(frame1, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=75,
                                                                                                              y=280)
    label = Label(frame1, text='I have an account', fg='black', bg='white', font=("Microdoft Yahei UI Light", 9))
    label.place(x=125, y=340)

    signin = Button(frame1, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=SignIn)
    signin.place(x=250, y=340)
    forgot_pass = Button(window, width=15, text='Forgot password', border=0, bg='white', cursor='hand2', fg='#57a1f8')
    forgot_pass.place(x=780, y=500)

    ###############################################################################################

    window.mainloop()

def test_select_num():
    def one():
        global test_sel_by_num
        test_sel_by_num=True
        global test_run_no
        test_run_no = test_run_no + 1
        test_var=Dict.get(1)
        test_var = initial_path + test_var
        list1.append(test_var)
    def two():
        global test_sel_by_num
        test_sel_by_num = True
        global test_run_no
        test_run_no = test_run_no + 1
        test_var=Dict.get(2)
        test_var=initial_path+test_var
        list1.append(test_var)
    def three():
        global test_sel_by_num
        test_sel_by_num = True
        global test_run_no
        test_run_no = test_run_no + 1
        test_var=Dict.get(3)
        test_var = initial_path + test_var
        list1.append(test_var)
    def four():
        global test_sel_by_num
        test_sel_by_num = True
        global test_run_no
        test_run_no = test_run_no + 1
        test_var=Dict.get(4)
        test_var = initial_path + test_var
        list1.append(test_var)
    def five():
        global test_sel_by_num
        test_sel_by_num = True
        global test_run_no
        test_run_no = test_run_no + 1
        test_var=Dict.get(5)
        test_var = initial_path + test_var
        list1.append(test_var)
    def six():
        global test_sel_by_num
        test_sel_by_num = True
        global test_run_no
        test_run_no = test_run_no + 1
        test_var = Dict.get(6)
        test_var = initial_path + test_var
        list1.append(test_var)
    def seven():
        global test_sel_by_num
        test_sel_by_num = True
        global test_run_no
        test_run_no = test_run_no + 1
        test_var = Dict.get(7)
        test_var = initial_path + test_var
        list1.append(test_var)
    def op1():
        window.destroy()
        test_plan()
    window = Tk()
    window.title("test_run Page")
    window.geometry("1000x900+100+50")
    window.configure(bg='#fff')
    window.resizable(False, False)
    window.img = PhotoImage(file="sign.png", master=window)
    Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)

    frame = Frame(window, width=350, height=550, bg='#fff')
    frame.place(x=480, y=70)

    heading = Label(frame, text="Field Test Tool", fg="#57a1f8", bg="white",
                    font=("Microdoft Yahei UI Light", 23, 'italic', 'bold'))
    heading.place(x=40, y=5)
    bt1 = Button(frame, text="ONE", bg="white", fg='black', bd='5', height="1", width="10",
                 cursor='hand2',
                 font=("Microdoft Yahei UI Light", 11, 'bold'), command=one)
    bt1.place(x=40, y=90)

    bt2 = Button(frame, text="TWO", bg="white", fg='black', bd='5', height="1", width="10",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=two)
    bt2.place(x=40, y=130)

    bt3 = Button(frame, text="THREE", bg="white", fg='black', bd='5', height="1", width="10",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=three)
    bt3.place(x=40, y=170)
    bt3 = Button(frame, text="FOUR", bg="white", fg='black', bd='5', height="1", width="10",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=four)
    bt3.place(x=40, y=220)
    bt3 = Button(frame, text="FIVE", bg="white", fg='black', bd='5', height="1", width="10",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=five)
    bt3.place(x=40, y=270)
    bt3 = Button(frame, text="SIX", bg="white", fg='black', bd='5', height="1", width="10",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=six)
    bt3.place(x=40, y=320)
    bt3 = Button(frame, text="SEVEN", bg="white", fg='black', bd='5', height="1", width="10",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=seven)
    bt3.place(x=40, y=370)
    bt3 = Button(frame, text="Back", bg="#57a1f8", fg='black', bd='5', height="2", width="25",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=op1)
    bt3.place(x=40, y=420)
    window.mainloop()

def status():
    def op1():
        window.destroy()
        subprocess.call('scrcpy')
    def op2():
        window.destroy()
        subprocess.call('scrcpy')

    def op3():
        window.destroy()
        subprocess.call('scrcpy')

    def back():
        window.destroy()
        exist_field()

    window = Tk()
    window.title("Status Page")
    window.geometry("1000x900+100+50")
    window.configure(bg='#fff')
    window.resizable(False, False)
    window.img = PhotoImage(file="sign.png", master=window)
    Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)

    window.img2 = PhotoImage(file='lt4_2.png', master=window)
    Label(window, image=window.img2, border=0, bg='white').place(x=5, y=650)

    frame = Frame(window, width=450, height=550, bg='#fff')
    frame.place(x=480, y=70)

    heading = Label(frame, text="Ongoing Test runs are:", fg="#57a1f8", bg="white",
                    font=("Microdoft Yahei UI Light", 23, 'italic', 'bold'))
    heading.place(x=40, y=5)
    length=len(list1)
    i=1
    vary=60
    while(i<length):
        str=list1[i].split('/')
        str1=str[-1]
        bt3 = Button(frame, text=str1, bg="#57a1f8", fg='black', bd='5', height="2", width="25",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold'), command=op1)
        bt3.place(x=40, y=vary)
        i=i+1
        vary=vary+70
    bt3 = Button(frame, text="Back", bg="#57a1f8", fg='black', bd='5', height="2", width="25",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold'), command=back)
    bt3.place(x=40, y=vary)
    window.mainloop()


login_page()


