
# Second Page

from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.state('zoomed')
ws.title('UNO GAME')
ws['bg'] = 'yellow'


def sel():
    value = {var.get()}

    print(f"How many Players you Want? : {var.get()}")

    if value == {2}:
        twoplayer()
    elif value == {3}:
        threeplayer()
    else:
        fourplayer()


def twoplayer():
    ws.destroy()
    import twoplayer


def threeplayer():
    ws.destroy()
    import threeplayer


def fourplayer():
    ws.destroy()
    import fourplayer


var = IntVar()

Label(ws, text="How many Players you want?", bg="yellow", fg="red",
      font="georgia 32 bold").place(x=480, y=220)

R1 = Radiobutton(ws, text="2 Players", variable=var, value=2, bg="yellow", fg="red",
                 font="georgia 20 bold", activebackground="yellow", activeforeground="red")
R1.place(x=650, y=300)

R2 = Radiobutton(ws, text="3 Players", variable=var, value=3, bg="yellow", fg="red",
                 font="georgia 20 bold", activebackground="yellow", activeforeground="red")
R2.place(x=650, y=350)

R3 = Radiobutton(ws, text="4 Players", variable=var, value=4, bg="yellow", fg="red",
                 font="georgia 20 bold", activebackground="yellow", activeforeground="red")
R3.place(x=650, y=400)

Button(ws, text="LEAVE", font="georgia 14 bold", padx=30, borderwidth=5, bg="red", fg="white",
       activebackground="red", activeforeground="white", command=quit).place(x=1360, y=8)
Button(ws, text="PLAY", font="georgia 16 bold", padx=30, borderwidth=5, bg='#00C800', fg="white",
       activebackground='#00C800', activeforeground="white", command=sel).place(x=650, y=480)

ws.mainloop()
