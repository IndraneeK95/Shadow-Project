from tkinter import *
# from PIL import ImageTk
from tkinter import messagebox
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


list1=['1']
today=date.today()

def second_page():
    def op1():
        window.destroy()
        field_page()

    def op2():
        window.destroy()
        devices_check()

    def op3():
        window.destroy()


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
    window.title("Field Page")
    window.geometry("900x750+100+50")
    window.configure(bg='#fff')
    window.resizable(False, False)
    window.img = PhotoImage(file="sign.png", master=window)
    Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)

    frame = Frame(window, width=350, height=390, bg='#fff')
    frame.place(x=480, y=70)

    heading = Label(frame, text="Field Test Tool", fg="#57a1f8", bg="white",
                    font=("Microdoft Yahei UI Light", 23, 'italic', 'bold'))
    heading.place(x=40, y=5)

    bt1 = Button(frame, text="Field Test", bg="white", fg='black', bd='5', height="2", width="25", cursor='hand2',
                 font=("Microdoft Yahei UI Light", 11, 'bold'), command=op1)
    bt1.place(x=40, y=90)

    bt2 = Button(frame, text="Check Connected Devices", bg="white", fg='black', bd='5', height="2", width="25",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=op2)
    bt2.place(x=40, y=160)

    bt3 = Button(frame, text="Reports", bg="white", fg='black', bd='5', height="2", width="25", cursor='hand2',
                 font=("Microdoft Yahei UI Light", 11, 'bold'),command=reports_check)
    bt3.place(x=40, y=230)
    bt4 = Button(frame, text="Back", bg="white", fg='black', bd='5', height="2", width="25", cursor='hand2',
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
        field_page()

    window = Tk()
    window.title("Field Page")
    window.geometry("900x750+100+50")
    window.configure(bg='#fff')
    window.resizable(False, False)
    window.img = PhotoImage(file="sign.png", master=window)
    Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)

    frame = Frame(window, width=350, height=390, bg='#fff')
    frame.place(x=480, y=70)

    heading = Label(frame, text="Field Test Tool", fg="#57a1f8", bg="white",
                    font=("Microdoft Yahei UI Light", 23, 'italic', 'bold'))
    heading.place(x=40, y=5)

    bt1 = Button(frame, text="Create test run", bg="white", fg='black', bd='5', height="2", width="25", cursor='hand2',
                 font=("Microdoft Yahei UI Light", 11, 'bold'), command=op1)
    bt1.place(x=40, y=90)

    bt2 = Button(frame, text="Check Existing run", bg="white", fg='black', bd='5', height="2", width="25",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=op2)
    bt2.place(x=40, y=160)

    bt3 = Button(frame, text="Back", bg="white", fg='black', bd='5', height="2", width="25",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=op3)
    bt3.place(x=40, y=230)


def create_field():
    def test_plan_selector():
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
        filename = filedialog.askopenfilename(initialdir="/home/indranee/Mobile application/Test_suite/",
                                              title="Select a File",
                                              filetypes=(("Text files",
                                                          "*.txt*"),
                                                         ("all files",
                                                          "*.*")))

        print(filename)
        list1.append(filename)

    def select_multiple_file():
        messagebox.showinfo("showinfo", "Please press Control to select multiple files")
        filename = filedialog.askopenfilenames(initialdir="/home/indranee/Mobile application/Test_suite/",
                                               title="Select a File",
                                               filetypes=(("Text files",
                                                           "*.txt*"),
                                                          ("all files",
                                                           "*.*")))

        i = 0
        length = len(filename)
        while i < length:
            list1.append(filename[i])
            i = i + 1

    def test_run():
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

    window = Tk()
    window.title("Field Page")
    window.geometry("900x750+100+50")
    window.configure(bg='#fff')
    window.resizable(False, False)
    window.img = PhotoImage(file="sign.png", master=window)
    Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)

    frame = Frame(window, width=350, height=390, bg='#fff')
    frame.place(x=480, y=70)

    heading = Label(frame, text="Field Test Tool", fg="#57a1f8", bg="white",
                    font=("Microdoft Yahei UI Light", 23, 'italic', 'bold'))
    heading.place(x=40, y=5)

    l1 = Label(frame, text="Username", fg="#57a1f8", bg="white", width='5', height='5',
                    font=("Microdoft Yahei UI Light", 11, 'italic', 'bold'))
    l1.place(x=40, y=30)
    bt1 = Button(frame, text="Select single file run", bg="white", fg='black', bd='5', height="2", width="25", cursor='hand2',
                 font=("Microdoft Yahei UI Light", 11, 'bold'), command=select_single_file)
    bt1.place(x=40, y=90)

    bt2 = Button(frame, text="Select multiple file run", bg="white", fg='black', bd='5', height="2", width="25",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=select_multiple_file)
    bt2.place(x=40, y=160)

    bt3 = Button(frame, text="Select test plan folder", bg="white", fg='black', bd='5', height="2", width="25",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=test_plan_selector)
    bt3.place(x=40, y=230)
    bt3 = Button(frame, text="Test Run", bg="white", fg='black', bd='5', height="2", width="25",
                 cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=op1)
    bt3.place(x=40, y=300)


def exist_field():
    window = Tk()
    window.title("SignUp")
    window.geometry("900x600+100+50")
    window.configure(bg='#0000CD')
    window.resizable(False, False)

    img = PhotoImage(file="sign.png")
    Label(window, image=img, border=0, bg='#0000CD').place(x=10, y=80)

    frame = Frame(window, width=500, height=500, bg='#0000CD')
    frame.place(x=400, y=70)

    heading = Label(frame, text="LTTS Field test tool", fg="#57a1f8", bg="white", relief='raised',
                    font=("Microdoft Yahei UI Light", 23, 'bold'))
    heading.place(x=80, y=5)
    b1 = Button(frame, width=39, pady=7, text='% completed', bg='#57a1f8', fg='white', border=0, relief='raised').place(x=75, y=70)
    b2 = Button(frame, width=39, pady=7, text='Status', bg='#57a1f8', fg='white', border=0).place(x=75, y=150)
   # b3 = Button(frame, width=39, pady=7, text='Reports', bg='#57a1f8', fg='white', border=0).place(x=75, y=250)
    b4 = Button(frame, width=29, pady=7, text='Back', bg='#57a1f8', fg='white', border=0).place(x=110, y=350)

    #########

    ##################################################################

    ##############################################################################

    ###############################################################################################

    window.mainloop()


def devices_check():
    def op2():
        t = subprocess.check_output("adb devices", shell=True)
        t = t.decode('utf-8')
        window.destroy()
        op3(t)


    def op3(t):
        window= Tk()
        window.title("SignUp")
        window.geometry("900x600+100+50")
        window.configure(bg='#fff')
        window.resizable(False, False)

        img = PhotoImage(file="sign.png")
        Label(window, image=img, border=0, bg='#0000CD').place(x=10, y=80)
        l2 = Label(window, text=t, bg="#fff", fg='black', bd='5', relief='raised', borderwidth='5', width="40",
                   height="30", font=("Times New Roman", 13))

        l2.place(x=450,y=80)

        window.mainloop()


    window = Tk()
    window.title("SignUp")
    window.geometry("900x600+100+50")
    window.configure(bg='#fff')
    window.resizable(False, False)

    img = PhotoImage(file="sign.png")
    Label(window, image=img, border=0, bg='#0000CD').place(x=10, y=80)

    frame = Frame(window, width=500, height=500, bg='#fff')
    frame.place(x=400, y=70)

    heading = Label(frame, text="LTTS Field test tool", fg="#57a1f8", bg="white", relief='raised',
                    font=("Microdoft Yahei UI Light", 23, 'bold'))
    heading.place(x=80, y=5)
    b1 = Button(frame, width=39, pady=7, text='Check Connected devices', bg='#57a1f8', fg='white', border=0, relief='raised', command=op2).place(
        x=75, y=70)
    b2 = Button(frame, width=39, pady=7, text='Assign more devices', bg='#57a1f8', fg='white', border=0).place(x=75, y=150)
    window.mainloop()

second_page()