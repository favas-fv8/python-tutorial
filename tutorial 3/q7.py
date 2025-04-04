import tkinter as tk
from tkinter import messagebox
import math
def compute():
 try:
  num=int(entry.get())
  res=math.sqrt(num)
  result.delete(0,tk.END)
  result.insert(0,str(res))
 except:
  messagebox.showerror("Error","Invalid input")
root=tk.Tk()
entry=tk.Entry(root)
entry.pack()
button=tk.Button(root,text="Compute",command=compute)
button.pack()
result=tk.Entry(root)
result.pack()
root.mainloop()
