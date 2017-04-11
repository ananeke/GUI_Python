from tkinter import *

def lodka():
    c.create_line(25, 400, 425, 400, 375, 450, 75, 450, 25, 400, fill ='red', width = 2)
    c.pack()

def maszt_1():
    c.create_line(325, 400, 320, 400, 320, 100, 325, 100, 325, 400, fill='red', width=2)
    c.create_line(325, 360, 380, 305, 325, 250, 380, 195, 325, 140 ,  fill='red', width=2)
    c.pack()

def maszt_2():
    c.create_line(200, 400, 205, 400, 205, 305, 200, 305, 200, 400, fill="red", width=2)
    c.create_line(200, 195, 205, 195,205, 100, 200, 100, 200, 195, fill="red", width=2)
    c.create_line(150, 305, 255, 305, fill='red', width=2)
    c.create_line(150, 195, 255, 195, fill='red', width=2)
    c.create_arc(120, 195, 180, 305, outline='red', width=2, style='arc', start=90, extent=-180)
    c.create_arc(225, 195, 285, 305, outline='red', width=2, style='arc', start=90, extent=180)

def ster():
    c.create_line(100, 400, 100, 350, fill='orange', width=2)
    c.create_oval(75, 390, 125, 360, outline='orange', width=2)
    c.create_line(60, 375, 140, 375,  fill='orange', width=2)
    c.create_line(75, 390, 125, 360, fill='orange', width=2)
    c.create_line(75,360, 125, 390, fill='orange', width=2)

def flaga():
    c.create_line(40, 400, 40, 365, 15, 365, 15, 375, 40, 375, fill='red', width=2)
    c.create_rectangle(15, 376, 40, 383, fill='red', outline='red', width=2)

def okienka():
    c.create_oval(350, 415, 375, 440, outline='red', width=2)
    c.create_oval(300, 415, 325, 440, outline='red', width=2)

def napis():
    c.create_text(150, 420, text='TSR 2017', font=('Times', '14'))

def morze():
    i = 0
    j = 10
    k = 20
    for p in range(25):
        c.create_line(i, 460, j, 445, k, 460, fill='blue', width=2, smooth=True)
        i += 20
        j += 20
        k += 20


okno = Tk()
c = Canvas(okno, width = 500, height=500)
lodka()
maszt_1()
maszt_2()
ster()
flaga()
okienka()
napis()
morze()
okno.mainloop()