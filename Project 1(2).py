# Import module
from tkinter import *
# Create object
window = Tk()

# Adjust size
window.title("Form ")
window.geometry("400x400")

#define labels
l1=Label(window, text="Name")
l1.grid(row=0,column=0)
l1=Label(window, text="Contact number")
l1.grid(row=1,column=0)
l1=Label(window, text="email id")
l1.grid(row=2,column=0)

#define entries
name_text=StringVar()
e1=Entry(window,textvariable=name_text)
e1.grid(row=0,column=1)
e1=Entry(window,textvariable=name_text)
e1.grid(row=1,column=1)
e1=Entry(window,textvariable=name_text)
e1.grid(row=2,column=1)

# Execute tkinter
window.mainloop()