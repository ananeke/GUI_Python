from tkinter import *

def chod(ruch):
    if ruch == '<Left>':
        b.place(x -=1, y -=1)
    elif ruch == '<Right>':
        b.place(x +=1, y +=1)

okno = Tk()
okno.title('Manipulator')
okno.geometry('500x500')
b = Button(okno, bitmap='questhead')
b.place(x=250, y=250)
b.bind(ruch, chod)

okno.mainloop()