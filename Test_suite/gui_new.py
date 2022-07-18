from tkinter import *
from tkinter import messagebox
import os
import subprocess
import robot
import webbrowser
from tkinter import ttk
from tkinter import filedialog

def first_page():
    def op1():
        mainscreen.destroy()
        login_page()

    def op2():
        mainscreen.destroy()

    def op3():
        mainscreen.destroy()
        register_page()

    mainscreen = Tk()  # create a GUI window
    mainscreen.geometry("800x800")  # set the configuration of GUI window
    mainscreen.title(" First page")  # set the title of GUI window
    mainscreen.configure(bg="grey")
    photo1 = PhotoImage(file="ltts_2.png")

    # l1.place(x=250, y=250)
    # create Login Button
    f1 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f1.pack(side=TOP)
    f2 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f2.pack(side=TOP)
    f3 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f3.pack(side=TOP)
    l0 = Label(f1, image=photo1, bg="white")
    l0.pack(side=TOP)
    # create a Form label
    l1 = Label(f1, text="Welcome to LTTS Field test tool", bg="grey", fg='white', relief='raised', borderwidth='5',
               bd='5', width="30", height="3", font=("Times New Roman", 13))
    l1.pack(side=BOTTOM)
    bt1 = Button(f2, text="About", bg="black", fg='white', bd="5", height="2", width="30")
    # bt1.place(x=280, y=350)
    # create a register button
    bt1.pack(side=TOP)
    bt2 = Button(f3, text="Register", bg="black", fg="white", bd="5", height="2", width="30", command=op3)
    # bt2.place(x=150, y=450)
    bt2.pack(side=TOP)
    bt3 = Button(f3, text="Login", bg="black", fg="white", bd="5", height="2", width="30", command=op1)
    # bt3.place(x=450, y=450)
    bt3.pack(side=TOP)
    bt4 = Button(f3, text="Exit", bg="black", fg="white", bd="5", height="2", width="30", command=op2)
    # bt4.place(x=300, y=550)
    bt4.pack(side=TOP)

    f1.pack(padx=1, pady=1)
    f2.pack(padx=20, pady=20)
    f3.pack(padx=20, pady=20)
    mainscreen.mainloop()  # start the GUI

list1=['1']

def login_page():
    def op1():
        data_username = textentry1.get()
        data_password = textentry2.get()
        if data_username == "Indranee" and data_password == "indranee":
            mainscreen.destroy()
            second_page()

    def op2():
        mainscreen.destroy()
        first_page()

    mainscreen = Tk()  # create a GUI window
    mainscreen.geometry("800x800")  # set the configuration of GUI window
    mainscreen.title(" Login Page")  # set the title of GUI window
    mainscreen.configure(bg="grey")
    photo1 = PhotoImage(file="ltts_2.png")
    f1 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f1.pack(side=TOP)
    f2 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f2.pack(side=TOP)
    Label(f1, image=photo1, bg="white").pack()

    # create a Form label
    l1 = Label(f1, text="Please enter your credentials", bg="grey", fg='white', bd='5', relief='raised',
               borderwidth='5', width="30", height="2", font=("Times New Roman", 13))
    l1.place(x=250, y=250)
    l2 = Label(text="UserName", bg="grey", fg='white', bd='5', relief='raised', borderwidth='3', width="30", height="1",
               font=("Times New Roman", 13))
    l2.place(x=50, y=350)
    textentry1 = Entry(mainscreen, width="30", bg="grey", fg="white", bd='5')
    textentry1.place(x=450, y=350)
    l3 = Label(text="Password", bg="grey", fg='white', bd='5', relief='raised', borderwidth='3', width="30", height="1",
               font=("Times New Roman", 13))
    l3.place(x=50, y=450)
    textentry2 = Entry(mainscreen, width="30", bg="grey", fg="white", bd='5', show="*")
    textentry2.place(x=450, y=450)
    b1 = Button(text="Submit", bg="black", fg='white', bd='5', height="2", width="30", command=op1)
    b1.place(x=50, y=650)
    b2 = Button(text="Back", bg="black", fg='white', bd='5', height="2", width="30", command=op2)
    b2.place(x=450, y=650)
    b3 = Button(text="Forgot Password", bg="black", fg='white', bd='5', height="1", width="30", command=op2)
    b3.place(x=250, y=500)
    mainscreen.mainloop()


def register_page():
    def op2():
        mainscreen.destroy()
        first_page()

    mainscreen = Tk()  # create a GUI window
    mainscreen.geometry("800x900")  # set the configuration of GUI window
    mainscreen.title(" Register Page")  # set the title of GUI window
    mainscreen.configure(bg="grey")
    photo1 = PhotoImage(file="ltts_2.png")
    f1 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f1.pack(side=TOP)
    f2 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f2.pack(side=TOP)
    Label(f1, image=photo1, bg="white").pack()

    # Label (mainscreen, image=photo1, bg="white") .pack()

    # create a Form label
    l1 = Label(text="Please enter your credentials", bg="grey", fg='white', bd='5', relief='raised', borderwidth='3',
               width="30", height="2", font=("Times New Roman", 13))
    l1.place(x=250, y=250)
    l2 = Label(text="First Name", bg="grey", fg='white', bd='5', relief='raised', borderwidth='3', width="30",
               height="1", font=("Times New Roman", 13))
    l2.place(x=50, y=350)
    textentry1 = Entry(mainscreen, width="30", bg="grey", fg='white', bd='5')
    textentry1.place(x=450, y=350)
    l3 = Label(text="Last name", bg="grey", fg='white', bd='5', relief='raised', borderwidth='3', width="30",
               height="1", font=("Times New Roman", 13))
    l3.place(x=50, y=450)
    textentry2 = Entry(mainscreen, width="30", bg="grey", fg='white', bd='5')
    textentry2.place(x=450, y=450)
    l4 = Label(text="PS number", bg="grey", fg='white', bd='5', relief='raised', borderwidth='3', width="30",
               height="1", font=("Times New Roman", 13))
    l4.place(x=50, y=550)
    textentry3 = Entry(mainscreen, width="30", bg="grey", fg='white', bd='5')
    textentry3.place(x=450, y=550)
    l5 = Label(text="Phone Number", bg="grey", fg='white', bd='5', relief='raised', borderwidth='3', width="30",
               height="1", font=("Times New Roman", 13))
    l5.place(x=50, y=650)
    textentry4 = Entry(mainscreen, width="30", bg="grey", fg='white', bd='5')
    textentry4.place(x=450, y=650)
    l6 = Label(text="Email id", bg="grey", fg='white', bd='5', relief='raised', borderwidth='3', width="30", height="1",
               font=("Times New Roman", 13))
    l6.place(x=50, y=750)
    textentry5 = Entry(mainscreen, width="30", bg="grey", fg='white', bd='5')
    textentry5.place(x=450, y=750)
    bt = Button(text="Submit", bg="black", fg='white', bd='5', height="2", width="20")
    bt.place(x=100, y=800)
    bt1 = Button(text="Back", bg="black", fg='white', bd='5', height="2", width="20", command=op2)
    bt1.place(x=500, y=800)

    mainscreen.mainloop()


def second_page():
    def op1():
        mainscreen.destroy()
        third_page()

    def op2():
        mainscreen.destroy()
        field_page()

    def op3():
        mainscreen.destroy()
        intro_page()

    def op4():
        mainscreen.destroy()
        login_page()

    def op5():
        mainscreen.destroy()
        dashboard()


    def web_open():
       # mainscreen.destroy()
        webbrowser.open_new_tab("report.html")

    mainscreen = Tk()  # create a GUI window
    mainscreen.geometry("800x1000")  # set the configuration of GUI window
    mainscreen.title(" Second Page")  # set the title of GUI window
    mainscreen.configure(bg="grey")
    photo1 = PhotoImage(file="ltts_2.png")
    f1 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f1.pack(side=TOP)
    f2 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f3 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f4 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f3.pack(side=TOP)
    f2.pack(side=TOP)
    f4.pack(side=TOP)
    Label(f1, image=photo1, bg="white").pack()

    # l1=Label (f1, image=photo1, bg="white")
    # l1.place(x=10,y=10)
    l2 = Label(f3, text="Laursen and Turbo Technology Services Field test tool", bg="grey", fg='white', bd='10',
               relief='raised', borderwidth='5', width="50", height="3", font=("Times New Roman", 13)).pack()
    # l2.place(x=250,y=10)
    bt1 = Button(f2, text="TEST", bg="black", fg='white', bd='5', height="2", width="25", command=op2)
    # bt1.place(x=50, y=300)
    bt1.pack()
    bt2 = Button(f2, text="CHECK CONNECTED DEVICES", bg="black", fg='white', bd='5', height="2", width="25",
                 command=op1)
    # bt2.place(x=300, y=300)
    bt2.pack()
    bt3 = Button(f2, text="REPORTS", bg="black", fg='white', bd='5', height="2", width="25", command=web_open)
    # bt3.place(x=550, y=300)
    bt3.pack()
    bt4 = Button(f2, text="DASHBOARD", bg="black", fg='white', bd='5', height="2", width="25", command=op5)
    # bt4.place(x=50, y=400)
    bt4.pack()
    bt5 = Button(f2, text="TEST PLANS", bg="black", fg='white', bd='5', height="2", width="25")
    # bt5.place(x=550, y=400)
    bt5.pack()
    bt6 = Button(f4, text="Introduction", bg="black", fg='white', bd='5', height="2", width="25", command=op3)
    # bt6.place(x=50, y=500)
    bt6.pack()
    bt7 = Button(f4, text="Objectives", bg="black", fg='white', bd='5', height="2", width="25")
    # bt7.place(x=550, y=500)
    bt7.pack()
    bt8 = Button(f4, text="Back", bg="black", fg='white', bd='5', height="2", width="35", command=op4)
    # bt8.place(x=250, y=600)
    bt8.pack()
    f1.pack(padx=1, pady=1)
    f3.pack(padx=20, pady=20)
    f2.pack(padx=20, pady=20)
    f4.pack(padx=20, pady=20)
    mainscreen.mainloop()


def field_page():
    def op1():
        mainscreen.destroy()
        second_page()


    def op2():
        mainscreen.destroy()
        exist_field_page()


    def op3():
        mainscreen.destroy()
        create_field_page()


    mainscreen = Tk()  # create a GUI window
    mainscreen.geometry("800x500")  # set the configuration of GUI window
    mainscreen.title(" Field Page")  # set the title of GUI window
    mainscreen.configure(bg="silver")
    photo1 = PhotoImage(file="ltts_2.png")
    f1 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
           highlightcolor="grey", highlightbackground="white",
           highlightthickness=10)
    f1.pack(side=TOP)
    f2 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
           highlightcolor="grey", highlightbackground="white",
           highlightthickness=10)
    f2.pack(side=TOP)
    f3 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
           highlightcolor="grey", highlightbackground="white",
           highlightthickness=10)
    f3.pack(side=TOP)
    Label(f1, image=photo1, bg="white").pack()
    bt1 = Button(f2, text="CREATE NEW TEST", bg="black", fg='white', bd='5', height="2", width="30", command=op3)
# bt1.place(x=100, y=300)
    bt1.pack(side=LEFT)
    bt2 = Button(f2, text="CHECK EXISTING TEST", bg="black", fg='white', bd='5', height="2", width="30", command=op2)
# bt2.place(x=500, y=300)
    bt2.pack(side=LEFT)
    bt3 = Button(f3, text="Back", bg="black", fg='white', bd='5', height="2", width="30", command=op1)
# bt3.place(x=250, y=400)
    bt3.pack(side=BOTTOM)
    f1.pack(padx=1, pady=1)
    f2.pack(padx=20, pady=20)
    f3.pack(padx=20, pady=20)
    mainscreen.mainloop()


def create_field_page():
    def op1():
        mainscreen.destroy()
        field_page()


    def op2():
        mainscreen.destroy()
        test_plan_selector()


    def op3():

        length = len(list1)
        print(length)
        i = 1

    # Iterating using while loop
        while i < length:
                file_exec=list1[i]
                print(file_exec)
                i=i+1
                messagebox.showinfo("showinfo", "Your selected test case run started")
                logFile = open('mylog.txt', 'w')
                robot.run(file_exec)
                messagebox.showinfo("showinfo", "Your selected test case run has successfully ended")


    mainscreen = Tk()  # create a GUI window
    mainscreen.geometry("800x800")  # set the configuration of GUI window
    mainscreen.title(" Create field Page")
    # set the title of GUI window
    mainscreen.configure(bg="silver")
    photo1 = PhotoImage(file="ltts_2.png")
    f1 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f1.pack(side=TOP)
    f2 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f2.pack(side=TOP)
    f3 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f3.pack(side=TOP)
    f4 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f4.pack(side=TOP)
    f5 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f5.pack(side=TOP)
    f6 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f6.pack(side=TOP)

    Label(f1, image=photo1, bg="white").pack()
    bt1 = Button(f2, text="PRODUCT", bg="black", fg='white', bd='5', height="2", width="30")
    # bt1.place(x=100, y=250)
    bt1.pack(side=LEFT)
    bt2 = Button(f2, text="PRODUCT VERSION", bg="black", fg='white', bd='5', height="2", width="30")
    # bt2.place(x=400, y=250)
    bt2.pack(side=LEFT)
    bt3 = Button(f3, text="TEST RUN NAME", bg="black", fg='white', bd='5', height="2", width="30")
    # bt3.place(x=100, y=350)
    bt3.pack(side=LEFT)
    bt4 = Button(f3, text="MAIN FUNCTIONALITY", bg="black", fg="white", bd='5', height="2", width="30")
    # bt4.place(x=400, y=350)
    bt4.pack(side=LEFT)
    bt5 = Button(f4, text="TEST PLAN SELECTOR", bg="black", fg='white', bd='5', height="2", width="30", command=op2)
    # bt5.place(x=100, y=450)
    bt5.pack(side=LEFT)
    bt6 = Button(f4, text="RUN TYPE", bg="black", fg='white', bd='5', height="2", width="30")
    # bt6.place(x=400, y=450)
    bt6.pack(side=LEFT)
    bt7 = Button(f5, text="SELECT DEMO 1", bg="black", fg='white', bd='5', height="2", width="30")
    # bt7.place(x=100, y=550)
    bt7.pack(side=LEFT)
    bt8 = Button(f5, text="SELECT DEMO 2", bg="black", fg='white', bd='5', height="2", width="30")
    # bt8.place(x=400, y=550)
    bt8.pack(side=LEFT)
    bt9 = Button(f6, text="RUN", bg="black", fg='white', bd='5', height="2", width="30", command=op3)
    # bt9.place(x=200, y=650)
    bt9.pack(side=BOTTOM)
    bt9 = Button(f6, text="Back", bg="black", fg='white', bd='5', height="2", width="30", command=op1)
    # bt9.place(x=200, y=650)
    bt9.pack(side=BOTTOM)
    f1.pack(padx=5, pady=5)
    f2.pack(padx=10, pady=10)
    f3.pack(padx=10, pady=10)
    f4.pack(padx=10, pady=10)
    f5.pack(padx=10, pady=10)
    f6.pack(padx=10, pady=10)

    mainscreen.mainloop()


def exist_field_page():
    def op1():
        mainscreen.destroy()
        third_page()

    def op2():
        mainscreen.destroy()
        test_cases()

    def op3():
        mainscreen.destroy()
        test_cases()

    def op5():
        mainscreen.destroy()
        field_page()

    def intro_op():
        mainscreen.destroy()
        intro_page()

    def single_test():
        mainscreen.destroy()
        test_cases()


    def multi_test():
        mainscreen.destroy()
        multiple_test_cases()


    def op6():
        mainscreen.destroy()
        progress()


    mainscreen = Tk()  # create a GUI window
    mainscreen.geometry("800x4000")  # set the configuration of GUI window
    mainscreen.title(" Exist Field  Page")  # set the title of GUI window
    mainscreen.configure(bg="silver")
    photo1 = PhotoImage(file="ltts_2.png")
    # l1=Label (mainscreen, image=photo1, bg="white")
    f1 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f1.pack(side=TOP)
    f2 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f2.pack(side=TOP)
    f3 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f3.pack(side=TOP)
    f4 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f4.pack(side=TOP)

    Label(f1, image=photo1, bg="white").pack()
    # l1.place(x=10,y=10)
    l2 = Label(f2, text="FIELD TEST TOOL", bg="grey", fg='black', bd='5', relief='raised', borderwidth='5', width="50",
               height="3", font=("Times New Roman", 13))
    # l2.place(x=250,y=10)
    l2.pack(side=RIGHT)
    l4 = Label(f3, text="TEST RUN VARIATIONS", bg="grey", fg='black', bd='5', relief='raised', borderwidth='5', width="50",
               height="3", font=("Times New Roman", 13))
    # l2.place(x=250,y=10)
    l4.pack(side=TOP)
    bt7 = Button(f3, text="SINGLE TEST RUN", bg="black", fg='white', bd='5', height="2", width="20", command=single_test)
    # bt7.place(x=50, y=650)
    bt7.pack(side=TOP)
    bt7 = Button(f3, text="MULTIPLE TESTS RUN", bg="black", fg='white', bd='5', height="2", width="20", command=multi_test)
    # bt7.place(x=50, y=650)
    bt7.pack(side=TOP)
    l3 = Label(f4, text="Existing run progress", bg="grey", fg='black', bd='5', relief='raised', borderwidth='5',
               width="50", height="3", font=("Times New Roman", 13))
    # l3.place(x=50,y=600)
    l3.pack(side=TOP)
    bt7 = Button(f4, text="% COMPLETED", bg="black", fg='white', bd='5', height="2", width="20", command=op6)
    # bt7.place(x=50, y=650)
    bt7.pack(side=TOP)
    bt8 = Button(f4, text="MANUAL TEST CASES", bg="black", fg='white', bd='5', height="2", width="20")
    # bt8.place(x=50, y=700)
    bt8.pack(side=TOP)
    bt9 = Button(f4, text="AUTOMATED TEST CASES", bg="black", fg='white', bd='5', height="2", width="20", command=op3)
    # bt9.place(x=50, y=750)
    bt9.pack(side=TOP)
    bt10 = Button(f4, text="AUTOMABLE TEST CASES", bg="black", fg='white', bd='5', height="2", width="20")
    # bt10.place(x=50, y=800)
    bt10.pack(side=TOP)
    bt11 = Button(f4, text="STATUS", bg="black", fg='white', bd='5', height="2", width="20")
    # bt11.place(x=50, y=850)
    bt11.pack(side=TOP)
    bt12 = Button(f4, text="Back", bg="grey", fg='black', bd='5', height="2", width="20", command=op5)
    # bt12.place(x=350, y=900)
    bt12.pack(side=TOP)
    f1.pack(padx=1, pady=1)
    f2.pack(padx=5, pady=5)
    f3.pack(padx=5, pady=5)
    f4.pack(padx=10, pady=10)
   # f6.pack(padx=5, pady=5)
    #f7.pack(padx=10, pady=10)
    mainscreen.mainloop()

def third_page():
    def op1():
        mainscreen.destroy()
        second_page()


    def op2():
        t = subprocess.check_output("adb devices", shell=True)
        t = t.decode('utf-8')
        mainscreen.destroy()
        op3(t)


    def op3(t):
        str_new = '\n' + '  '
        mainscreen2 = Tk()  # create a GUI window
        mainscreen2.geometry("800x500")  # set the configuration of GUI window
        mainscreen2.title(" Third Page")  # set the title of GUI window
        mainscreen2.configure(bg="silver")
        photo1 = PhotoImage(file="ltts_2.png")
        f1 = Frame(mainscreen2, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
        f1.pack(side=TOP)
        f2 = Frame(mainscreen2, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
        f2.pack(side=TOP)
        f3 = Frame(mainscreen2, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
        f3.pack(side=TOP)
        Label(f1, image=photo1, bg="white").pack()

    # for v in t.split('\n'):
    #                 str_new=v+str_new

        l2 = Label(f2, text=t, bg="grey", fg='black', bd='5', relief='raised', borderwidth='5', width="50",
               height="8", font=("Times New Roman", 13))

        l2.pack(side=TOP)

        def op_new():
            mainscreen2.destroy()
            third_page()

        bt3 = Button(f3, text="Back", bg="black", fg='white', bd='5', height="2", width="30", command=op_new)
    # bt3.place(x=250, y=400)
        bt3.pack(side=BOTTOM)
        f1.pack(padx=1, pady=1)
        f2.pack(padx=10, pady=10)
        f3.pack(padx=10, pady=10)
        mainscreen2.mainloop()

    mainscreen = Tk()  # create a GUI window
    mainscreen.geometry("800x500")  # set the configuration of GUI window
    mainscreen.title(" Login Page")  # set the title of GUI window
    mainscreen.configure(bg="silver")
    photo1 = PhotoImage(file="ltts_2.png")
    f1 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f1.pack(side=TOP)
    f2 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f2.pack(side=TOP)
    f3 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f3.pack(side=TOP)
    Label(f1, image=photo1, bg="white").pack()
    bt1 = Button(f2, text="ASSIGN MORE DEVICES", bg="black", fg='white', bd='5', height="2", width="30")
    # bt1.place(x=100, y=300)
    bt1.pack(side=LEFT)
    bt2 = Button(f2, text="SHOW CONNECTED DEVICES", bg="black", fg='white', bd='5', height="2", width="30", command=op2)
    # bt2.place(x=500, y=300)
    bt2.pack(side=LEFT)
    bt3 = Button(f3, text="Back", bg="black", fg='white', bd='5', height="2", width="30", command=op1)
    # bt3.place(x=250, y=400)
    bt3.pack(side=BOTTOM)
    f1.pack(padx=1, pady=1)
    f2.pack(padx=20, pady=20)
    f3.pack(padx=20, pady=20)
    mainscreen.mainloop()



def test_cases():
    def op1():
        root = Tk()
        root.geometry('300x120')
        root.title('Test run on progress')

        root.grid()

        # progressbar
        pb = ttk.Progressbar(
            root,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        # place the progressbar
        pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
        pb.start()
        logFile = open('mylog.txt', 'w')
        robot.run("download_speed_case.robot")


    def op2():
        root = Tk()
        root.geometry('300x120')
        root.title('Test run on progress')

        root.grid()

        # progressbar
        pb = ttk.Progressbar(
            root,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        # place the progressbar
        pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
        pb.start()
        logFile = open('mylog.txt', 'w')
        robot.run("upload_speed_case.robot")


    def op3():
        root = Tk()
        root.geometry('300x120')
        root.title('Test run on progress')

        root.grid()

        # progressbar
        pb = ttk.Progressbar(
            root,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        # place the progressbar
        pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
        pb.start()
        logFile = open('mylog.txt', 'w')
        robot.run("check_IPV6_case.robot")


    def op4():
        root = Tk()
        root.geometry('300x120')
        root.title('Test run on progress')

        root.grid()

        # progressbar
        pb = ttk.Progressbar(
            root,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        # place the progressbar
        pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
        pb.start()
        logFile = open('mylog.txt', 'w')
        robot.run("check_IPV4_case.robot")


    def op5():
        root = Tk()
        root.geometry('300x120')
        root.title('Test run on progress')

        root.grid()

        # progressbar
        pb = ttk.Progressbar(
            root,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        # place the progressbar
        pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
        pb.start()
        logFile = open('mylog.txt', 'w')
        robot.run("simul_data_voice_case.robot")
        subprocess.call("scrcpy", shell=True)


    def op6():
        root = Tk()
        root.geometry('300x120')
        root.title('Test run on progress')

        root.grid()

        # progressbar
        pb = ttk.Progressbar(
            root,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        # place the progressbar
        pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
        pb.start()
        logFile = open('mylog.txt', 'w')
        robot.run("msg_data_On_case.robot")


    def op7():
        messagebox.showinfo("showinfo", "Your selected test case run started")
        root = Tk()
        root.geometry('300x120')
        root.title('Test run on progress')

        root.grid()

        # progressbar
        pb = ttk.Progressbar(
            root,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        # place the progressbar
        pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
        pb.start()

       # subprocess.call("scrcpy", shell=True)

        logFile = open('mylog.txt', 'w')
        robot.run("call_data_On_case.robot")
        messagebox.showinfo("showinfo", "Your test case has executed and passed successfully")


    def op8():
        messagebox.showinfo("showinfo", "Your selected test case run started")
        root = Tk()
        root.geometry('300x120')
        root.title('Test run on progress')

        root.grid()

        # progressbar
        pb = ttk.Progressbar(
            root,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        # place the progressbar
        pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
        pb.start()
        logFile = open('mylog.txt', 'w')
        robot.run("send_a_msg_case.robot")
        messagebox.showinfo("showinfo", "Your test case has executed and passed successfully")


    def op9():
        mainscreen.destroy()
        exist_field_page()


    def op10():
        root = Tk()
        root.geometry('300x120')
        root.title('Test run on progress')

        root.grid()

        # progressbar
        pb = ttk.Progressbar(
            root,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        # place the progressbar
        pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
        pb.start()
        logFile = open('mylog.txt', 'w')
        robot.run("bidi_transf.robot")

    mainscreen = Tk()  # create a GUI window
    mainscreen.geometry("800x900")  # set the configuration of GUI window
    mainscreen.title(" Test cases Page")  # set the title of GUI window
    mainscreen.configure(bg="teal")
    mainscreen.configure(borderwidth='10')
    photo1 = PhotoImage(file="ltts_2.png")
    f1 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f1.pack(side=TOP)
    f2 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f2.pack(side=TOP)
    f3 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f3.pack(side=TOP)
    Label(f1, image=photo1, bg="white").pack()
    l2 = Label(f2, text="TEST CASES", relief='raised', borderwidth='5', bg="grey", fg='white', bd='5', width="40",
               height="2", font=("Times New Roman", 13))
    # l2.place(x=100, y=250)
    l2.pack(side=BOTTOM)
    bt1 = Button(f3, text="Calculate HTTPS download link speed", bg="black", fg='white', bd='5', height="2", width="40",
                 command=op1)
    # bt1.place(x=100, y=350)
    bt1.pack(side=TOP)
    bt2 = Button(f3, text="Calculate HTTPS upload link speed", bg="black", fg='white', bd='5', height="2", width="40",
                 command=op2)
    # bt2.place(x=100, y=400)
    bt2.pack(side=TOP)
    bt3 = Button(f3, text="Check IPV6 connectivity", bg="black", fg='white', bd='5', height="2", width="40",
                 command=op3)
    # bt3.place(x=100, y=450)
    bt3.pack(side=TOP)
    bt4 = Button(f3, text="Check IPV4 connectivity", bg="black", fg='white', bd='5', height="2", width="40",
                 command=op4)
    # bt4.place(x=100, y=500)
    bt4.pack(side=TOP)
    bt5 = Button(f3, text="Check simultaneous voice and data call", bg="black", fg='white', bd='5', height="2",
                 width="40", command=op5)
    # bt5.place(x=100, y=550)
    bt5.pack(side=TOP)
    bt6 = Button(f3, text="Check msg while data on", bg="black", fg='white', bd='5', height="2", width="40",
                 command=op6)
    # bt6.place(x=100, y=600)
    bt6.pack(side=TOP)
    bt7 = Button(f3, text="Check call while data on", bg="black", fg='white', bd='5', height="2", width="40",
                 command=op7)
    # bt7.place(x=100, y=650)
    bt7.pack(side=TOP)
    bt8 = Button(f3, text="bidirectional data transfer", bg="black", fg='white', bd='5', height="2", width="40",
                 command=op10)
    # bt8.place(x=100, y=700)
    bt8.pack(side=TOP)
    bt9 = Button(f3, text="send msg", bg="black", fg='white', bd='5', height="2", width="40", command=op8)
    # bt9.place(x=100, y=750)
    bt9.pack(side=TOP)
    bt10 = Button(f3, text="Back", bg="black", fg='white', bd='5', height="2", width="20", command=op9)
    # bt10.place(x=100, y=850)
    bt10.pack(side=TOP)
    f1.pack(padx=1, pady=1)
    f2.pack(padx=10, pady=10)
    f3.pack(padx=5, pady=5)
    mainscreen.mainloop()


def multiple_test_cases():
    mainscreen = Tk()  # create a GUI window
    mainscreen.geometry("800x900")  # set the configuration of GUI window
    mainscreen.title(" Test cases Page")  # set the title of GUI window
    mainscreen.configure(bg="teal")
    mainscreen.configure(borderwidth='10')
    photo1 = PhotoImage(file="ltts_2.png")
    f1 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f1.pack(side=TOP)
    f2 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f2.pack(side=TOP)
    Label(f1, image=photo1, bg="white").pack()
    Checkbutton1 = IntVar()
    Checkbutton2 = IntVar()
    Checkbutton3 = IntVar()
    Checkbutton4 = IntVar()
    Checkbutton5 = IntVar()
    Checkbutton6 = IntVar()
    Checkbutton7 = IntVar()
    Checkbutton8 = IntVar()
    Checkbutton9 = IntVar()

    Button1 = Checkbutton(f2, text="Test1",
                          variable=Checkbutton1,
                          onvalue=1,
                          offvalue=0,
                          height=2,
                          width=20, bg='grey', fg='black', relief='raised', padx=5, pady=5)

    Button2 = Checkbutton(f2, text="Test2",
                          variable=Checkbutton2,
                          onvalue=1,
                          offvalue=0,
                          height=2,
                          width=20, bg='grey', fg='black', relief='raised', padx=5, pady=5)

    Button3 = Checkbutton(f2, text="Test3",
                          variable=Checkbutton3,
                          onvalue=1,
                          offvalue=0,
                          height=2,
                          width=20, bg='grey', fg='black', relief='raised', padx=5, pady=5)

    Button1.pack(side=TOP)
    Button2.pack(side=TOP)
    Button3.pack(side=TOP)

    f1.pack(padx=1, pady=1)
    f2.pack(padx=20, pady=20)
    mainscreen.mainloop()



def intro_page():
    def op1():
        mainscreen.destroy()
        second_page()

    mainscreen = Tk()  # create a GUI window
    mainscreen.geometry("800x500")  # set the configuration of GUI window
    mainscreen.title(" Introduction Page")  # set the title of GUI window
    mainscreen.configure(bg="silver")
    photo1 = PhotoImage(file="ltts_2.png")
    f1 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f1.pack(side=TOP)
    f2 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f2.pack(side=TOP)
    f3 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f3.pack(side=TOP)
    Label(f1, image=photo1, bg="white").pack()
    l1 = Label(f2, text="Field testing is a critical step in the last phase of mobile testing. "
                        "After all regression tests pass, testers would go into the real environment to verify an application's usability and behavior. The purpose of field testing is to determine how an application works before releasing it to end-users.", bg="grey", fg='white', bd='5', relief='raised',
               borderwidth='5', width="100", height="30", font=("Times New Roman", 13))
    l1.pack(side=TOP)
    bt8 = Button(f3, text="Back", bg="black", fg='white', bd='5', height="2", width="35", command=op1)
    bt8.pack(side=BOTTOM)
    mainscreen.mainloop()





def progress():
    root = Tk()
    #root.geometry("600*600")
    # Progress bar widget
    progress = ttk.Progressbar(root, orient=HORIZONTAL,
                           length=700, mode='determinate')

    # Function responsible for the updation
    # of the progress bar value
    def bar():
        import time
        progress['value'] = 20
        root.update_idletasks()
        time.sleep(1)

        progress['value'] = 40
        root.update_idletasks()
        time.sleep(1)

        progress['value'] = 50
        root.update_idletasks()
        time.sleep(1)

        progress['value'] = 60
        root.update_idletasks()
        time.sleep(1)

        progress['value'] = 80
        root.update_idletasks()
        time.sleep(1)
        progress['value'] = 100

    progress.pack(pady=10)

    # This button will initialize
    # the progress bar
    Button(root, text='Start Run', command=bar).pack(pady=10)

    # infinite loop
    mainloop()


def test_plan_selector():

    def op1():
            filename = filedialog.askopenfilename(initialdir="/home/indranee/Mobile application/Test_suite/",
                                                  title="Select a File",
                                                  filetypes=(("Text files",
                                                              "*.txt*"),
                                                             ("all files",
                                                              "*.*")))

            print(filename)
            list1.append(filename)
           # logFile = open('mylog.txt', 'w')
            #robot.run(filename)

    def op2():
        mainscreen.destroy()
        create_field_page()

    mainscreen = Tk()  # create a GUI window
    mainscreen.geometry("800x900")  # set the configuration of GUI window
    mainscreen.title(" Test cases Page")  # set the title of GUI window
    mainscreen.configure(bg="teal")
    mainscreen.configure(borderwidth='10')
    photo1 = PhotoImage(file="ltts_2.png")
    f1 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="100",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f1.pack(side=TOP)
    f2 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f2.pack(side=TOP)
    f3 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
              highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f3.pack(side=TOP)
    f4 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f4.pack(side=TOP)
    f5 = Frame(mainscreen, bg='grey', relief='raised', width="800", height="800",
               highlightcolor="grey", highlightbackground="white",
               highlightthickness=10)
    f5.pack(side=TOP)
    Label(f1, image=photo1, bg="white").pack()


    bt1 = Button(f2, text="Select test plan folder", bg="black", fg='white', bd='5', height="2", width="40",
                 command=op1)
    # bt1.place(x=100, y=350)
    bt1.pack(side=TOP)
    l2 = Label(f3, text="Select test plan folder", bg="grey", fg='black', bd='5', relief='raised', borderwidth='5',
               width="50",
               height="2", font=("Times New Roman", 13))
    l2.pack(side=TOP)
    bt2 = Button(f4, text="Select single test file", bg="black", fg='white', bd='5', height="2", width="40",
                 command=op1)
    # bt2.place(x=100, y=400)
    bt2.pack(side=RIGHT)
    bt3 = Button(f4, text="Select multiple test files", bg="black", fg='white', bd='5', height="2", width="40",command=op2
                 )
    # bt3.place(x=100, y=450)
    bt3.pack(side=RIGHT)
    bt4 = Button(f5, text="Back", bg="black", fg='white', bd='5', height="2", width="40",
                 command=op2
                 )
    # bt3.place(x=100, y=450)
    bt4.pack(side=TOP)
    f1.pack(padx=10,pady=10)
    f2.pack(padx=10, pady=10)
    f3.pack(padx=10, pady=10)
    f4.pack(padx=10, pady=10)
    f5.pack(padx=10, pady=10)
    mainscreen.mainloop()

first_page()