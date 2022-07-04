from tkinter import *
import os
import subprocess
import robot


def op1():

     logFile = open('mylog.txt', 'w')
     robot.run("download_speed_case.robot")


def op2():
    logFile = open('mylog.txt', 'w')
    robot.run("upload_speed_case.robot")


def op3():
    logFile = open('mylog.txt', 'w')
    robot.run("check_IPV6_case.robot")


def op4():
    logFile = open('mylog.txt', 'w')
    robot.run("check_IPV4_case.robot")


def op5():
    logFile = open('mylog.txt', 'w')
    robot.run("simul_data_voice_case.robot")


def op6():
    logFile = open('mylog.txt', 'w')
    robot.run("msg_data_On_case.robot")


def op7():
    logFile = open('mylog.txt', 'w')
    robot.run("call_data_On_case.robot")


def op8():
    logFile = open('mylog.txt', 'w')
    robot.run("send_a_msg_case.robot")

def op9():
    mainscreen.destroy()
    import  exist_field


def op10():
    logFile = open('mylog.txt', 'w')
    robot.run("bidi_transf.robot")



mainscreen = Tk()  # create a GUI window
mainscreen.geometry("800x900")  # set the configuration of GUI window
mainscreen.title(" Login Page")  # set the title of GUI window
mainscreen.configure(bg="teal")
mainscreen.configure( borderwidth='10')
photo1 = PhotoImage(file="ltts_2.png")
f1=Frame(mainscreen,bg='grey', relief='raised', width="800", height="100",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f1.pack(side = TOP)
f2=Frame(mainscreen,bg='grey', relief='raised', width="800", height="800",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f2.pack(side = TOP)
f3=Frame(mainscreen,bg='grey', relief='raised', width="800", height="800",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f3.pack(side=TOP)
Label (f1, image=photo1, bg="white") .pack()
l2=Label(f2, text="TEST CASES",relief='raised', borderwidth='5',bg="grey", fg='white', bd='5',  width="40", height="2", font=("Times New Roman", 13))
#l2.place(x=100, y=250)
l2.pack(side=BOTTOM)
bt1 = Button(f3,text="Calculate HTTPS download link speed", bg="black", fg='white', bd='5', height="2", width="40", command=op1)
#bt1.place(x=100, y=350)
bt1.pack(side=TOP)
bt2 = Button(f3,text="Calculate HTTPS upload link speed", bg="black", fg='white', bd='5',  height="2", width="40", command=op2)
#bt2.place(x=100, y=400)
bt2.pack(side=TOP)
bt3 = Button(f3,text="Check IPV6 connectivity", bg="black", fg='white', bd='5',  height="2", width="40",command=op3)
#bt3.place(x=100, y=450)
bt3.pack(side=TOP)
bt4 = Button(f3,text="Check IPV4 connectivity", bg="black", fg='white', bd='5', height="2", width="40",command=op4)
#bt4.place(x=100, y=500)
bt4.pack(side=TOP)
bt5 = Button(f3,text="Check simultaneous voice and data call", bg="black", fg='white', bd='5', height="2", width="40", command=op5)
#bt5.place(x=100, y=550)
bt5.pack(side=TOP)
bt6 = Button(f3,text="Check msg while data on", bg="black", fg='white', bd='5', height="2", width="40", command=op6)
#bt6.place(x=100, y=600)
bt6.pack(side=TOP)
bt7 = Button(f3,text="Check call while data on", bg="black", fg='white', bd='5',  height="2", width="40", command=op7)
#bt7.place(x=100, y=650)
bt7.pack(side=TOP)
bt8 = Button(f3, text="bidirectional data transfer", bg="black", fg='white', bd='5',  height="2", width="40", command=op10)
#bt8.place(x=100, y=700)
bt8.pack(side=TOP)
bt9 = Button(f3,text="send msg", bg="black", fg='white', bd='5',  height="2", width="40", command=op8)
#bt9.place(x=100, y=750)
bt9.pack(side=TOP)
bt10 = Button(f3,text="Back", bg="black", fg='white', bd='5',  height="2", width="20", command=op9)
#bt10.place(x=100, y=850)
bt10.pack(side=TOP)
f1.pack(padx=1,pady=1)
f2.pack(padx=10,pady=10)
f3.pack(padx=5,pady=5)
mainscreen.mainloop()
