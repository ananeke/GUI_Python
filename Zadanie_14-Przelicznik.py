from tkinter import *

def licz():
    global s1, s2, s3, s4, wynik
    wynik = int(s1.get(),16)*16**3 + int(s2.get(),16)*16**2 + int(s3.get(),16)*16 + int(s4.get(),16)
    e.config(state='normal')
    e.delete(0, END)
    e.insert(0,str(wynik))
    e.config(state='readonly')

ok = Tk()
ok.title('Przelicznik')

od = '0x'
do = '0x'
lista=[]

for i in range(16):
    lista.append(str(hex(i)))

s1 = Spinbox(ok, values=lista, width=5, command=licz)
s2 = Spinbox(ok, values=lista, width=5, command=licz)
s3 = Spinbox(ok, values=lista, width=5, command=licz)
s4 = Spinbox(ok, values=lista, width=5, command=licz)
s1.grid(column=0, row=0)
s2.grid(column=1, row=0)
s3.grid(column=2, row=0)
s4.grid(column=3, row=0)

e = Entry(ok, width=20, justify=RIGHT, state='readonly')
e.grid(columnspan=4, row=1)
ok.mainloop()