from tkinter import *

def op1():
     mainscreen.destroy()
     import second_page

def op2():
    mainscreen.destroy()
    import exist_field

def op3():
    mainscreen.destroy()
    import  create_field

mainscreen = Tk()  # create a GUI window
mainscreen.geometry("800x500")  # set the configuration of GUI window
mainscreen.title(" Login Page")  # set the title of GUI window
mainscreen.configure(bg="silver")
photo1 = PhotoImage(file="ltts_2.png")
f1=Frame(mainscreen,bg='grey', relief='raised', width="800", height="800",
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
Label (f1, image=photo1, bg="white") .pack()
bt1=Button(f2,text="CREATE NEW FIELD", bg="black", fg='white', bd='5', height="2", width="30", command=op3)
#bt1.place(x=100, y=300)
bt1.pack(side=LEFT)
bt2 = Button(f2,text="CHECK EXISTING FIELD", bg="black", fg='white', bd='5', height="2", width="30", command=op2)
#bt2.place(x=500, y=300)
bt2.pack(side=LEFT)
bt3 = Button(f3,text="Back", bg="black", fg='white', bd='5', height="2", width="30", command=op1)
#bt3.place(x=250, y=400)
bt3.pack(side=BOTTOM)
f1.pack(padx=1,pady=1)
f2.pack(padx=20,pady=20)
f3.pack(padx=20,pady=20)
mainscreen.mainloop()