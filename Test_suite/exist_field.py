from tkinter import *

def op1():
    mainscreen.destroy()
    import third_page

def op2():
    mainscreen.destroy()
    import test_cases_gui

def op3():
    mainscreen.destroy()
    import test_cases_gui

def op5():
    mainscreen.destroy()
    import field



mainscreen = Tk()  # create a GUI window
mainscreen.geometry("800x4000")  # set the configuration of GUI window
mainscreen.title(" Login Page")  # set the title of GUI window
mainscreen.configure(bg="silver")
photo1 = PhotoImage(file="ltts_2.png")
#l1=Label (mainscreen, image=photo1, bg="white")
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
f4=Frame(mainscreen,bg='grey', relief='raised', width="800", height="800",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f4.pack(side = TOP)
f5=Frame(mainscreen,bg='grey', relief='raised', width="800", height="800",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f5.pack(side = TOP)
f6=Frame(mainscreen,bg='grey', relief='raised', width="800", height="800",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f6.pack(side = TOP)
f7=Frame(mainscreen,bg='grey', relief='raised', width="800", height="2000",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f7.pack(side = TOP)
Label (f1, image=photo1, bg="white") .pack()
#l1.place(x=10,y=10)
f1 = Frame(mainscreen, background="red")
l2=Label(f2,text="FIELD TEST TOOL", bg="grey", fg='black', bd='5', relief='raised', borderwidth='5', width="50", height="3", font=("Times New Roman", 13))
#l2.place(x=250,y=10)
l2.pack(side=RIGHT)
bt1 = Button(f3,text="FIELD", bg="grey", fg='white', bd='5', height="2", width="20")
#bt1.place(x=50, y=300)
bt1.pack(side=RIGHT)
bt2 = Button(f3,text="CHECK CONNECTED DEVICES", bg="grey", fg='white', bd='5' , height="2", width="20", command=op1)
#bt2.place(x=300, y=300)
bt2.pack(side=RIGHT)
bt3 = Button(f4,text="REPORTS", bg="grey", fg='white', bd='5', height="2", width="20")
#bt3.place(x=550, y=300)
bt3.pack(side=RIGHT)
bt4 = Button(f4, text="DASHBOARD", bg="grey", fg='white', bd='5', height="2", width="20")
#bt4.place(x=50, y=400)
bt4.pack(side=RIGHT)
bt5 = Button(f4, text="TEST PLANS", bg="grey", fg='white' , bd='5', height="2", width="20")
#bt5.place(x=550, y=400)
bt5.pack(side=RIGHT)
bt6 = Button(f5, text="Introduction", bg="grey", fg='white', bd='5', height="2", width="35")
#bt6.place(x=50, y=500)
bt6.pack(side=RIGHT)
bt7 = Button(f5,text="Objectives", bg="grey", fg='white', bd='5',  height="2", width="35")
#bt7.place(x=550, y=500)
bt7.pack(side=RIGHT)
l3=Label(f6,text="Existing run progress", bg="black", fg='white', bd='5', relief='raised', borderwidth='3', width="50", height="2", font=("Times New Roman", 13))
#l3.place(x=50,y=600)
l3.pack(side=TOP)
bt7 = Button(f7, text="% COMPLETED", bg="black", fg='white', bd='5', height="2", width="20")
#bt7.place(x=50, y=650)
bt7.pack(side=TOP)
bt8 = Button(f7,text="MANUAL TEST CASES", bg="black", fg='white', bd='5', height="2", width="20")
#bt8.place(x=50, y=700)
bt8.pack(side=TOP)
bt9 = Button(f7,text="AUTOMATED TEST CASES", bg="black", fg='white', bd='5', height="2", width="20", command=op3)
#bt9.place(x=50, y=750)
bt9.pack(side=TOP)
bt10 = Button(f7,text="AUTOMABLE TEST CASES", bg="black", fg='white', bd='5', height="2", width="20")
#bt10.place(x=50, y=800)
bt10.pack(side=TOP)
bt11 = Button(f7,text="STATUS", bg="black", fg='white', bd='5', height="2", width="20")
#bt11.place(x=50, y=850)
bt11.pack(side=TOP)
bt12 = Button(f7,text="Back", bg="grey", fg='black', bd='5' , height="2", width="20", command=op5)
#bt12.place(x=350, y=900)
bt12.pack(side=LEFT)
f1.pack(padx=1,pady=1)
f2.pack(padx=5,pady=5)
f3.pack(padx=5,pady=5)
f4.pack(padx=5, pady=5)
f5.pack(padx=5, pady=10)
f6.pack(padx=5, pady=5)
f7.pack(padx=1, pady=1)
mainscreen.mainloop()

