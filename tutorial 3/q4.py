import tkinter as tk
def f_to_c():
 f=float(entry_f.get())
 c=(f-32)*5/9
 entry_c.delete(0,tk.END)
 entry_c.insert(0,str(round(c,2)))
def c_to_f():
 c=float(entry_c.get())
 f=c*9/5+32
 entry_f.delete(0,tk.END)
 entry_f.insert(0,str(round(f,2)))
root=tk.Tk()
label_f=tk.Label(root,text="Fahrenheit")
label_f.grid(row=0,column=0)
label_c=tk.Label(root,text="Celsius")
label_c.grid(row=0,column=1)
entry_f=tk.Entry(root)
entry_f.grid(row=1,column=0)
entry_f.insert(0,"32")
entry_c=tk.Entry(root)
entry_c.grid(row=1,column=1)
entry_c.insert(0,"0.0")
button1=tk.Button(root,text=">>>>",command=f_to_c)
button1.grid(row=2,column=0)
button2=tk.Button(root,text="<<<<",command=c_to_f)
button2.grid(row=2,column=1)
root.mainloop()
