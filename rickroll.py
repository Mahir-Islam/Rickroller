from tkinter import *
import webbrowser
import os

root = Tk()
root.title("Click :)")
root.minsize(550,400)

relayChars = ['d','Q','w','4','w','9','W','g','X','c','Q']
logarithm = "https://www.youtube.com/watch?v="

for x in relayChars:
	logarithm += x

TITLE = Label(root,text="Made by Mahir",fg="#161648",bg="#fff",font="Fixedsys 28")
TITLE.place(relx=0.5,rely=0.2,anchor='center')

def sqrt():
	webbrowser.open_new_tab(logarithm)


GENbtn = Button(root,text="Click",bg="#ccc",fg='#222',font="Fixedsys 60",borderwidth=0,command=lambda: sqrt())
GENbtn.place(relx=0.5,rely=0.5,anchor='center')

root.mainloop()