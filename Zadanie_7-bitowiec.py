from tkinter import *


def koniec():
    okno.destroy()


def licz():
    global a1, a2, a3, a4, a5, a6, a7, a8, wynik
    wynik = int(a1.get())*128 + int(a2.get())*64 + int(a3.get())*32 + int(a4.get())*16 + int(a5.get())*8 \
            + int(a6.get())*4 + int(a7.get())*2 + int(a8.get())*1
    l.config(text=wynik)

okno = Tk()
okno.title('Bitowiec')
a1 = IntVar()
c1 = Checkbutton(okno, text='7', variable=a1, command=licz).grid(column=0, row=0)
a2 = IntVar()
c2 = Checkbutton(okno, text='6', variable=a2, command=licz).grid(column=1, row=0)
a3 = IntVar()
c3 = Checkbutton(okno, text='5', variable=a3, command=licz).grid(column=2, row=0)
a4 = IntVar()
c4 = Checkbutton(okno, text='4', variable=a4, command=licz).grid(column=3, row=0)
a5 = IntVar()
c5 = Checkbutton(okno, text='3', variable=a5, command=licz).grid(column=4, row=0)
a6 = IntVar()
c6 = Checkbutton(okno, text='2', variable=a6, command=licz).grid(column=5, row=0)
a7 = IntVar()
c7 = Checkbutton(okno, text='1', variable=a7, command=licz).grid(column=6, row=0)
a8 = IntVar()
c8 = Checkbutton(okno, text='0', variable=a8, command=licz).grid(column=7, row=0)


l = Label(okno, width=5, height=5, font=('Arial', '20', 'bold'), anchor=CENTER)
l.grid(columnspan=8)
b = Button(okno, text='Koniec', command=koniec)
b.grid(columnspan=8)
okno.mainloop()
