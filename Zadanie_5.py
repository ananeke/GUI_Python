from tkinter import *


a = 250
b = 250
f = 250
g = 250


def w_lewo(zdarz=None):
    global f, g
    if f <= 5:
        f = 5
        c.place(x=f, y=g)
    else:
        f -= 1
        c.place(x=f, y=g)


def w_lewoc(zdarz=None):
    global f, g
    if f <= 5:
        f = 5
        c.place(x=f, y=g)
    else:
        f -= 5
        c.place(x=f, y=g)


def w_prawo(zdarz=None):
    global f, g
    if f >= 470:
        f = 470
        c.place(x=f, y=g)
    else:
        f += 1
        c.place(x=f, y=g)


def w_prawoc(zdarz=None):
    global f, g
    if f >= 470:
        f = 470
        c.place(x=f, y=g)
    else:
        f += 5
        c.place(x=f, y=g)


def w_dol(zdarz=None):
    global f, g
    if g >= 470:
        g = 470
        c.place(x=f, y=g)
    else:
        g += 1
        c.place(x=f, y=g)


def w_dolc(zdarz=None):
    global f, g
    if g >= 470:
        g = 470
        c.place(x=f, y=g)
    else:
        g += 5
        c.place(x=f, y=g)


def w_gore(zdarz=None):
    global f, g
    if g <= 5:
        g = 5
        c.place(x=f, y=g)
    else:
        g -= 1
        c.place(x=f, y=g)


def w_gorec(zdarz=None):
    global f, g
    if g <= 5:
        g = 5
        c.place(x=f, y=g)
    else:
        g -= 5
        c.place(x=f, y=g)


def koniec(zdarz=None):
    okno.destroy()


okno = Tk()
okno.title('Manipulator')
okno.geometry('500x500')
c = Button(okno, bitmap='questhead')
c.place(x=a, y=b)
okno.bind('<Left>', w_lewo)
okno.bind('<Right>', w_prawo)
okno.bind('<Up>', w_gore)
okno.bind('<Down>', w_dol)
okno.bind('<Control-Left>', w_lewoc)
okno.bind('<Control-Right>', w_prawoc)
okno.bind('<Control-Up>', w_gorec)
okno.bind('<Control-Down>', w_dolc)
okno.bind('<Escape>', koniec)
okno.mainloop()