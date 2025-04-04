import tkinter as tk
import random
def check():
 global guesses
 num=int(entry.get())
 guesses+=1
 if num<secret:
  label['text']="Too small, try again"
 elif num>secret:
  label['text']="Too large, try again"
 else:
  label['text']=f"Correct! Guesses: {guesses}"
def new_game():
 global secret
 global guesses
 secret=random.randint(1,100)
 guesses=0
 label['text']="Guess a number between 1 and 100"
root=tk.Tk()
secret=random.randint(1,100)
guesses=0
entry=tk.Entry(root)
entry.pack()
button=tk.Button(root,text="Guess",command=check)
button.pack()
label=tk.Label(root,text="Guess a number between 1 and 100")
label.pack()
new_button=tk.Button(root,text="New Game",command=new_game)
new_button.pack()
root.mainloop()
