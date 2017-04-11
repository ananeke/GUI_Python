from tkinter import *
from tkinter import messagebox
import random

def zbieg(zdarz=None):
    a = random.randint(0, 450)
    c = random.randint(0, 450)
    b.place(x=a, y=c)

def klik():
    messagebox.showinfo('Gratulacje!', ' Złapałes mnie :)')
ok = Tk()
ok.title('Gonitwa')
ok.geometry("500x500")
b = Button(ok, text='Złap mnie!', command=klik)
b.place(x=100, y=100)
b.bind('<Enter>', zbieg)

ok.mainloop()