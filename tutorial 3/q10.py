import tkinter as tk
def compute():
 h=float(entry1.get())
 b=float(entry2.get())
 n=int(entry3.get())
 total=h
 for i in range(n-1):
  h*=b
  total+=2*h
 result.delete(0,tk.END)
 result.insert(0,str(round(total,2)))
root=tk.Tk()
entry1=tk.Entry(root)
entry1.insert(0,"Initial height")
entry1.pack()
entry2=tk.Entry(root)
entry2.insert(0,"Bounciness index")
entry2.pack()
entry3=tk.Entry(root)
entry3.insert(0,"Number of bounces")
entry3.pack()
button=tk.Button(root,text="Compute",command=compute)
button.pack()
result=tk.Entry(root)
result.pack()
root.mainloop()
