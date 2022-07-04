from tkinter import *

#window = Tk()
#window.title("first page")
#window.configure(background="white")
#photo1=PhotoImage(file="ltts_2.png")
#Label (window, image=photo1, bg="white") .grid(row=0, column=0, sticky=W)
#Label (window, text="Username" , font="none 12 bold") .grid(row=10,column=5, sticky=W)
#textentry1= Entry(window, width=20, bg="white")
#textentry1.grid(row=10, column=10)
#Label (window, text="Password" , font="none 12 bold") .grid(row=30,column=5, sticky=W)
#textentry2= Entry(window, width=20, bg="white")
#textentry2.grid(row=30, column=10)
#window.mainloop()
def op1():
    mainscreen.destroy()
    import login_page

def op2():
    mainscreen.destroy()

def op3():
    mainscreen.destroy()
    import register


mainscreen = Tk()  # create a GUI window
mainscreen.geometry("800x800")  # set the configuration of GUI window
mainscreen.title(" Login Page")  # set the title of GUI window
mainscreen.configure(bg="navy blue")
photo1 = PhotoImage(file="ltts_2.png")

#l1.place(x=250, y=250)
# create Login Button
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
f3.pack(side = TOP)
l0=Label (f1, image=photo1, bg="white")
l0.pack(side=TOP)
# create a Form label
l1=Label(f1,text="Welcome to LTTS Field test tool", bg="grey", fg='white', relief='raised', borderwidth='5', bd='5', width="30", height="2", font=("Times New Roman", 13))
l1.pack(side=BOTTOM)
bt1=Button(f2, text="About",bg="black", fg='white', bd="5",  height="2", width="30")
#bt1.place(x=280, y=350)
# create a register button
bt1.pack(side= TOP)
bt2=Button(f3,text="Register", bg="black", fg="white", bd="5", height="2", width="30",command=op3)
#bt2.place(x=150, y=450)
bt2.pack(side=TOP)
bt3=Button(f3,text="Login", bg="black", fg="white", bd="5", height="2", width="30", command=op1)
#bt3.place(x=450, y=450)
bt3.pack(side=TOP)
bt4=Button(f3,text="Exit", bg="black", fg="white", bd="5", height="2", width="30", command=op2)
#bt4.place(x=300, y=550)
bt4.pack(side=TOP)
f1.pack(padx=1,pady=1)
f2.pack(padx=20,pady=20)
f3.pack(padx=20,pady=20)
mainscreen.mainloop()  # start the GUI

