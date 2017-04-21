from tkinter import *

napis = ''


def sprawdz(z):
    global e1, e2, e3, t, napis
    ile_liczb = 0
    ile_liter = 0

    if z.keycode == 8:

        napis = napis[:-1]

        e1.config(state='normal')
        e1.delete(0, END)
        e1.insert(0, 'Znaków:' + str(len(napis)))
        e1.config(state='readonly')

        e2.config(state='normal')
        e2.delete(0, END)
        for i in napis:
            if i.isalpha():
                ile_liter += 1

        e2.insert(0, 'Liter:' + str(ile_liter))
        e2.config(state='readonly')

        e3.config(state='normal')
        e3.delete(0, END)

        for i in napis:
            if i.isnumeric():
                ile_liczb += 1

        e3.insert(0, 'Cyfr:' + str(ile_liczb))
        e3.config(state='readonly')
    else:

        napis = napis + z.char

        e1.config(state='normal')
        e1.delete(0, END)
        e1.insert(0, 'Znaków:' + str(len(napis)))
        e1.config(state='readonly')

        e2.config(state='normal')
        e2.delete(0, END)
        for i in napis:
            if i.isalpha():
                ile_liter += 1

        e2.insert(0, 'Liter:' + str(ile_liter))
        e2.config(state='readonly')

        e3.config(state='normal')
        e3.delete(0, END)

        for i in napis:
            if i.isnumeric():
                ile_liczb += 1

        e3.insert(0, 'Cyfr:' + str(ile_liczb))
        e3.config(state='readonly')


ok = Tk()

ok.title('Teksty')
t = Text(ok, font=('Times', '12'), height=5, width=40)
t.grid(columnspan=4, row=0)
t.bind('<Key>', sprawdz)

e1 = Entry(ok)
e1.grid(column=0, row=1)
e1.insert(0, 'Znaków:0')
e1.config(state='readonly')

e2 = Entry(ok)
e2.insert(0, 'Liter:0')
e2.config(state='readonly')
e2.grid(column=1, row=1)

e3 = Entry(ok)
e3.insert(0, 'Cyfr:0')
e3.config(state='readonly')
e3.grid(column=3, row=1)

ok.mainloop()
