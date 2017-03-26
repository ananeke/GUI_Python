from tkinter import *
from tkinter import messagebox


def oblicz():
    global r1
    if r1.get() == 1:
        messagebox.showinfo('Wynik odejmowania :\n', str((float(a.get()) - float(b.get()))))
    elif r1.get() == 2:
        messagebox.showinfo('Wynik dodawania :\n', str((int(a.get()) + int(b.get()))))
    elif r1.get() == 3:
        messagebox.showinfo('Wynik mnożenia :\n', str(int(a.get()) * int(b.get())))
    elif r1.get() == 4:
        if b.get() == '0':
            messagebox.showinfo('Wynik', 'Nie można dzielić przez 0')
        else:
            messagebox.showinfo('Wynik dzielenia :\n', str(int(a.get()) / int(b.get())))
okno = Tk()
okno.title('Kalkulatorek liczb całkowitych- Zadanie 2')
a = StringVar()
a1 = Entry(okno, textvariable=a).grid(row=2, column=0)
b = StringVar()
b1 = Entry(okno, textvariable=b).grid(row=2, column=2)
r1 = IntVar()
r11 = Radiobutton(okno, text='-', variable=r1, value=1).grid(row=0, column=1)
r12 = Radiobutton(okno, text='+', variable=r1, value=2).grid(row=1, column=1)
r13 = Radiobutton(okno, text='*', variable=r1, value=3).grid(row=2, column=1)
r14 = Radiobutton(okno, text='/', variable=r1, value=4).grid(row=3, column=1)
Button(okno, text='Oblicz!', command=oblicz).grid(row=4, column=1)
okno.mainloop()
