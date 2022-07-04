from tkinter import *

def op1():
       mainscreen.destroy()
       import  field

mainscreen = Tk()  # create a GUI window
mainscreen.geometry("800x800")  # set the configuration of GUI window
mainscreen.title(" Login Page")
# set the title of GUI window
mainscreen.configure(bg="silver")
photo1 = PhotoImage(file="ltts_2.png")
f1=Frame(mainscreen,bg='grey', relief='raised', width="800", height="100",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f1.pack(side = TOP)
f2=Frame(mainscreen,bg='grey', relief='raised', width="800", height="100",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f2.pack(side = TOP)
f3=Frame(mainscreen,bg='grey', relief='raised', width="800", height="100",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f3.pack(side = TOP)
f4=Frame(mainscreen,bg='grey', relief='raised', width="800", height="100",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f4.pack(side = TOP)
f5=Frame(mainscreen,bg='grey', relief='raised', width="800", height="100",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f5.pack(side = TOP)
f6=Frame(mainscreen,bg='grey', relief='raised', width="800", height="100",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f6.pack(side = TOP)

Label (f1, image=photo1, bg="white") .pack()
bt1=Button(f2,text="PRODUCT", bg="black", fg='white', bd='5', height="2", width="30")
#bt1.place(x=100, y=250)
bt1.pack(side=LEFT)
bt2=Button(f2, text="PRODUCT VERSION", bg="black", fg='white', bd='5' ,height="2", width="30")
#bt2.place(x=400, y=250)
bt2.pack(side=LEFT)
bt3=Button(f3,text="TEST RUN NAME", bg="black", fg='white', bd='5', height="2", width="30")
#bt3.place(x=100, y=350)
bt3.pack(side=LEFT)
bt4=Button(f3,text="MAIN FUNCTIONALITY", bg="black", fg="white", bd='5', height="2", width="30")
#bt4.place(x=400, y=350)
bt4.pack(side=LEFT)
bt5=Button(f4,text="TEST PLAN SELECTOR", bg="black", fg='white', bd='5', height="2", width="30")
#bt5.place(x=100, y=450)
bt5.pack(side=LEFT)
bt6=Button(f4, text="RUN TYPE", bg="black", fg='white' , bd='5',  height="2", width="30")
#bt6.place(x=400, y=450)
bt6.pack(side=LEFT)
bt7=Button(f5,text="SELECT DEMO 1", bg="black", fg='white' , bd='5', height="2", width="30")
#bt7.place(x=100, y=550)
bt7.pack(side=LEFT)
bt8=Button(f5,text="SELECT DEMO 2", bg="black", fg='white' , bd='5',  height="2", width="30")
#bt8.place(x=400, y=550)
bt8.pack(side=LEFT)
bt9=Button(f6,text="RUN", bg="black", fg='white', bd='5',  height="2", width="30")
#bt9.place(x=200, y=650)
bt9.pack(side=BOTTOM)
bt9=Button(f6,text="Back", bg="black", fg='white', bd='5',  height="2", width="30", command=op1)
#bt9.place(x=200, y=650)
bt9.pack(side=BOTTOM)
f1.pack(padx=5,pady=5)
f2.pack(padx=10,pady=10)
f3.pack(padx=10,pady=10)
f4.pack(padx=10, pady=10)
f5.pack(padx=10, pady=10)
f6.pack(padx=10, pady=10)



mainscreen.mainloop()