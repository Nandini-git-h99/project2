# Import module
from tkinter import *
# Create object
window = Tk()

# Adjust size
window.title("Restuarant app ")
window.geometry("700x500")

#Registration form
l1=Label(window, text="Registration form", font="times 12 bold")
l1.grid(row=0,column=0)
l2=Label(window, text="Login", font="times 8 bold")
l2.grid(row=1,column=0)
l3=Label(window, text="Signup", font="times 8 bold")
l3.grid(row=2,column=0)
name_text=StringVar()
e1=Entry(window,textvariable=name_text)
e1.grid(row=1,column=1)
e1=Entry(window,textvariable=name_text)
e1.grid(row=2,column=1)

#tile
l6=Label(window, text="XYZ Restuarant ", font="times 25 bold")
l6.place(x=380,y=20,anchor="center")

#Menu bar
l1=Label(window, text="Menu", font="times 24 bold")
l1.place(x=460,y=70)
l2=Label(window, text="Pizza    Rs180", font="times 15 bold")
l2.place(x=450,y=120)
l3=Label(window, text="Burger Rs120", font="times 15 bold")
l3.place(x=450,y=150)
l4=Label(window, text="Cake     Rs80", font="times 15 bold")
l4.place(x=450,y=180)
l5=Label(window, text="Juice    Rs50", font="times 15 bold")
l5.place(x=450,y=210)

# Execute tkinter
window.mainloop()