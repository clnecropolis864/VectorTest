from Tkinter import *
import ttk
import vector
import calc

def submitForm():
	vec1 = vector.Vector3d(int(u1.get()), int(u2.get()), int(u3.get()))
	vec2 = vector.Vector3d(int(v1.get()), int(v2.get()), int(v3.get()))
	#ansBox['text'] = str(calc.crossProduct(v1, v2))
	ans.set(str(calc.crossProduct(vec1, vec2)))
root = Tk()

content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=50)

ans = StringVar()

u1 = ttk.Entry(content, width=5)
u2 = ttk.Entry(content, width=5)
u3 = ttk.Entry(content, width=5)
v1 = ttk.Entry(content, width=5)
v2 = ttk.Entry(content, width=5)
v3 = ttk.Entry(content, width=5)
ansBox = ttk.Entry(content, textvariable=ans)
calculate = ttk.Button(content, text='Calculate', command=submitForm)

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
calculate.grid(column = 2, row = 1)

root.mainloop()