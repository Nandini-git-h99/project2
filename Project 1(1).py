# Import module
from tkinter import *
def function():
    pass
def do_popup(event):
    m.tk_popup(event.x_window,event.y_window)
    m.grab_release()
# Create object
window = Tk()

# Adjust size
window.title("right click menu ")
window.geometry("400x400")

#popup menu button
m = Menu(window,tearoff = 0)
m.add_command(Label='copy',command=function)
m.add_command(Label='cut',command=function)
m.add_command(Label='paste',command=function)
m.add_command(Label='refresh',command=function)
window.bind("<Button-3>", do_popup)

# Execute tkinter
window.mainloop()
