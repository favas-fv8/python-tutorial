import tkinter as tk
def convert():
 s=entry.get()
 result.delete(0,tk.END)
 result.insert(0,s.upper())
root=tk.Tk()
entry=tk.Entry(root)
entry.pack()
button=tk.Button(root,text="Convert",command=convert)
button.pack()
result=tk.Entry(root)
result.pack()
root.mainloop()
