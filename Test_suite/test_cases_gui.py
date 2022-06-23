from tkinter import *
import os
import subprocess
import robot


def op1():
    #os.system('cmd /k "robot --test TC7 Field_test.robot"')
     #subprocess.run('ls')
     #subprocess.run('robot --test TC7 Field_test.robot')


     logFile = open('mylog.txt', 'w')
     robot.run("TC1.robot")


mainscreen = Tk()  # create a GUI window
mainscreen.geometry("800x800")  # set the configuration of GUI window
mainscreen.title(" Login Page")  # set the title of GUI window
mainscreen.configure(bg="teal")
photo1 = PhotoImage(file="ltts_2.png")
Label (mainscreen, image=photo1, bg="white") .pack()
l2=Label(text="TEST CASES", bg="white", width="30", height="3", font=("Calibri", 13))
l2.place(x=230, y=250)
bt1 = Button(text="Calculate HTTPS download link speed", bg="light blue", height="2", width="40", command=op1)
bt1.place(x=100, y=350)
bt2 = Button(text="Calculate FTP download link speed", bg="light blue", height="2", width="40")
bt2.place(x=100, y=400)
bt3 = Button(text="Calculate HTTPS upload link speed", bg="light blue", height="2", width="40")
bt3.place(x=100, y=450)
bt4 = Button(text="Calculate FTP upload link speed", bg="light blue", height="2", width="40")
bt4.place(x=100, y=500)
bt5 = Button(text="Check IPV4 connectivity", bg="light blue", height="2", width="40")
bt5.place(x=100, y=550)
bt6 = Button(text="Check IPV6 connectivity", bg="light blue", height="2", width="40")
bt6.place(x=100, y=600)
bt7 = Button(text="Exit", bg="orange", height="2", width="20")
bt7.place(x=300, y=700)
mainscreen.mainloop()
