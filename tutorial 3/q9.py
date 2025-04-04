import tkinter as tk
def guess():
 global low
 global high
 global mid
 mid=(low+high)//2
 label['text']=f"Is it {mid}?"
def too_small():
 global low
 low=mid+1
 guess()
def too_large():
 global high
 high=mid-1
 guess()
def correct():
 label['text']=f"Guessed it! Number is {mid}"
 button1['state']='disabled'
 button2['state']='disabled'
 button3['state']='disabled'
def new_game():
 global low
 global high
 low=1
 high=100
 button1['state']='normal'
 button2['state']='normal'
 button3['state']='normal'
 guess()
root=tk.Tk()
low=1
high=100
label=tk.Label(root,text="")
label.pack()
button1=tk.Button(root,text="Too Small",command=too_small)
button1.pack()
button2=tk.Button(root,text="Too Large",command=too_large)
button2.pack()
button3=tk.Button(root,text="Correct",command=correct)
button3.pack()
new_button=tk.Button(root,text="New Game",command=new_game)
new_button.pack()
new_game()
root.mainloop()
