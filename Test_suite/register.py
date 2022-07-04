from tkinter import *


def op2():
    mainscreen.destroy()
    import first_page

mainscreen = Tk()  # create a GUI window
mainscreen.geometry("800x900")  # set the configuration of GUI window
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

#Label (mainscreen, image=photo1, bg="white") .pack()

# create a Form label
l1=Label(text="Please enter your credentials", bg="grey", fg='white', bd='5', relief='raised', borderwidth='3', width="30", height="2", font=("Times New Roman", 13))
l1.place(x=250,y=250)
l2=Label(text="First Name", bg="grey", fg='white', bd='5', relief='raised', borderwidth='3', width="30", height="1", font=("Times New Roman", 13))
l2.place(x=50, y=350)
textentry1= Entry(mainscreen, width="30" ,bg="grey", fg='white', bd='5')
textentry1.place(x=450, y=350)
l3=Label(text="Last name", bg="grey", fg='white', bd='5', relief='raised', borderwidth='3', width="30", height="1", font=("Times New Roman", 13))
l3.place(x=50, y=450)
textentry2 = Entry(mainscreen, width="30", bg="grey", fg='white', bd='5')
textentry2.place(x=450,y=450)
l4=Label(text="PS number", bg="grey", fg='white', bd='5', relief='raised', borderwidth='3', width="30", height="1", font=("Times New Roman", 13))
l4.place(x=50, y=550)
textentry3 = Entry(mainscreen, width="30", bg="grey", fg='white', bd='5')
textentry3.place(x=450,y=550)
l5=Label(text="Phone Number", bg="grey", fg='white', bd='5', relief='raised', borderwidth='3', width="30", height="1", font=("Times New Roman", 13))
l5.place(x=50, y=650)
textentry4 = Entry(mainscreen, width="30", bg="grey", fg='white', bd='5')
textentry4.place(x=450,y=650)
l6=Label(text="Email id", bg="grey", fg='white', bd='5', relief='raised', borderwidth='3', width="30", height="1", font=("Times New Roman", 13))
l6.place(x=50, y=750)
textentry5 = Entry(mainscreen, width="30", bg="grey", fg='white', bd='5')
textentry5.place(x=450,y=750)
bt = Button(text="Submit", bg="black", fg='white' , bd='5', height="2", width="20")
bt.place(x=100, y=800)
bt1 = Button(text="Back", bg="black", fg='white' , bd='5', height="2", width="20", command=op2)
bt1.place(x=500, y=800)

mainscreen.mainloop()