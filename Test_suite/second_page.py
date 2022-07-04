from tkinter import *

def op1():
    mainscreen.destroy()
    import third_page

def op2():
    mainscreen.destroy()
    import field

def op4():
    mainscreen.destroy()
    import  login_page


mainscreen = Tk()  # create a GUI window
mainscreen.geometry("800x1000")  # set the configuration of GUI window
mainscreen.title(" Login Page")  # set the title of GUI window
mainscreen.configure(bg="dark blue")
photo1 = PhotoImage(file="ltts_2.png")
f1=Frame(mainscreen,bg='grey', relief='raised', width="800", height="100",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f1.pack(side = TOP)
f2=Frame(mainscreen,bg='grey', relief='raised', width="800", height="800",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f3=Frame(mainscreen,bg='grey', relief='raised', width="800", height="800",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f4=Frame(mainscreen,bg='grey', relief='raised', width="800", height="800",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f3.pack(side= TOP)
f2.pack(side = TOP)
f4.pack(side= TOP)
Label (f1, image=photo1, bg="white") .pack()

#l1=Label (f1, image=photo1, bg="white")
#l1.place(x=10,y=10)
l2=Label(f3,text="Laursen and Turbo Technology Services Field test tool", bg="grey", fg='white', bd='10', relief='raised', borderwidth='5',width="50", height="3", font=("Times New Roman", 13)).pack()
#l2.place(x=250,y=10)
bt1 = Button(f2, text="FIELD", bg="black", fg='white', bd='5', height="2", width="20", command=op2)
#bt1.place(x=50, y=300)
bt1.pack()
bt2 = Button(f2,text="CHECK CONNECTED DEVICES", bg="black", fg='white', bd='5', height="2", width="25", command=op1)
#bt2.place(x=300, y=300)
bt2.pack()
bt3 = Button(f2,text="REPORTS", bg="black", fg='white', bd='5', height="2", width="20")
#bt3.place(x=550, y=300)
bt3.pack()
bt4 = Button(f2, text="DASHBOARD", bg="black", fg='white', bd='5', height="2", width="20")
#bt4.place(x=50, y=400)
bt4.pack()
bt5 = Button(f2, text="TEST PLANS", bg="black", fg='white', bd='5', height="2", width="20")
#bt5.place(x=550, y=400)
bt5.pack()
bt6 = Button(f4, text="Introduction", bg="black", fg='white', bd='5', height="2", width="35")
#bt6.place(x=50, y=500)
bt6.pack()
bt7 = Button(f4, text="Objectives", bg="black", fg='white', bd='5', height="2", width="35")
#bt7.place(x=550, y=500)
bt7.pack()
bt8 = Button(f4,text="Back", bg="black", fg='white', bd='5', height="2", width="35", command=op4)
#bt8.place(x=250, y=600)
bt8.pack()
f1.pack(padx=1,pady=1)
f3.pack(padx=20, pady=20)
f2.pack(padx=20,pady=20)
f4.pack(padx=20, pady=20)
mainscreen.mainloop()

