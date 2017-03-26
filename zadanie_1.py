from tkinter import *
from tkinter import messagebox

def sprawdz():
    if v.get().isdigit() and len(v.get())==11:
        messagebox.showinfo('Informacja','PESEL został wpisany poprawnie.')
    else:
        messagebox.showinfo('Informacja', 'PESEL został wpisany NIEpoprawnie.')


okno= Tk()
okno.title('Zadanie 1')
Label(okno, text='PESEL:').grid(row=0,column=0)
v = StringVar()
Entry(okno,textvariable=v,width=11).grid(row=0,column=1)
Button(okno,text='Sprawdz!',command=sprawdz).grid(columnspan=2)
okno.mainloop()

