import tkinter as tk
from tkinter import *


def load():
    pass

def save():
    pass

top=Tk()
top.title('Simple Editor')

contents=Text()
contents.pack(side=BOTTOM,expand=True,fill=BOTH)

filename=Entry()
filename.pack(side=LEFT,expand=True,fill=X)

Button(text='Open',command=load).pack(side=LEFT)
Button(text='Save',command=save).pack(side=LEFT)
mainloop()