from Tkinter import *
import ttk

from vector import Vector
import calc
root = Tk()

content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=50)

ux = IntVar()
uy = IntVar()
uz = IntVar()
vx = IntVar()
vy = IntVar()
vz = IntVar()
ans = IntVar()

u1 = ttk.Entry(content, width=5)
u2 = ttk.Entry(content, width=5)
u3 = ttk.Entry(content, width=5)
v1 = ttk.Entry(content, width=5)
v2 = ttk.Entry(content, width=5)
v3 = ttk.Entry(content, width=5)
ansBox = ttk.Entry(content)

label = ttk.Label(frame, text='Welcome to Vector Calculator!')


content.grid()
frame.grid()
label.grid(column=0, row=0, columnspan=2)
u1.grid()
u2.grid()
u3.grid()
v1.grid(column = 1, row = 1)
v2.grid(column = 1, row = 2)
v3.grid(column = 1, row = 3)
ansBox.grid(column = 2, row = 2)

root.mainloop()