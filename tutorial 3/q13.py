import tkinter as tk
import math
def compute():
 num=float(entry.get())
 result.delete(0,tk.END)
 result.insert(0,str(math.sqrt(num)))
root=tk.Tk()
entry=tk.Entry(root)
entry.pack()
button=tk.Button(root,text="Square Root",command=compute)
button.pack()
result=tk.Entry(root)
result.pack()
root.mainloop()
