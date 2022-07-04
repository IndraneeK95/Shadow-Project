from tkinter import *

def op1():
    data_username=textentry1.get()
    data_password=textentry2.get()
    if data_username=="Indranee" and data_password=="indranee" :
        mainscreen.destroy()
        import second_page


def op2():
     mainscreen.destroy()
     import  first_page


mainscreen = Tk()  # create a GUI window
mainscreen.geometry("800x800")  # set the configuration of GUI window
mainscreen.title(" Login Page")  # set the title of GUI window
mainscreen.configure(bg="navy blue")
photo1 = PhotoImage(file="ltts_2.png")
f1=Frame(mainscreen,bg='grey', relief='raised', width="800", height="100",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f1.pack(side = TOP)
f2=Frame(mainscreen,bg='grey', relief='raised', width="800", height="800",
       highlightcolor="grey",highlightbackground="white",
       highlightthickness=10)
f2.pack(side = TOP)
Label (f1, image=photo1, bg="white") .pack()

# create a Form label
l1=Label(f1,text="Please enter your credentials", bg="grey",fg='white',bd='5', relief='raised', borderwidth='5', width="30", height="2", font=("Times New Roman", 13))
l1.place(x=250,y=250)
l2=Label(text="UserName", bg="grey",fg='white', bd='5',relief='raised', borderwidth='3', width="30", height="1", font=("Times New Roman", 13))
l2.place(x=50, y=350)
textentry1= Entry(mainscreen, width="30" ,bg="grey",fg="white", bd='5')
textentry1.place(x=450, y=350)
l3=Label(text="Password", bg="grey", fg='white', bd='5', relief='raised', borderwidth='3', width="30", height="1", font=("Times New Roman", 13))
l3.place(x=50, y=450)
textentry2 = Entry(mainscreen, width="30", bg="grey", fg="white", bd='5', show="*")
textentry2.place(x=450,y=450)
b1=Button(text="Submit", bg="black", fg='white', bd='5', height="2", width="30", command=op1)
b1.place(x=50,y=550)
b2=Button(text="Back", bg="black", fg='white', bd='5', height="2", width="30", command=op2)
b2.place(x=450,y=550)
mainscreen.mainloop()

