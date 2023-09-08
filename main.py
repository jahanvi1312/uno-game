# Main Page

from tkinter import *
from PIL import Image, ImageTk

ws = Tk()
ws.state('zoomed')
ws.title('UNO GAME')
ws['bg'] = '#000000'


def nextPage():
    ws.destroy()
    import page2


image = Image.open("images/bac.png")
resize_img = image.resize((1550, 850), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resize_img)

can_widght = Canvas(ws, height=850, width=1550)
can_widght.create_image(768, 385, image=img)
can_widght.pack()

btn = Button(ws, text="PLAY", borderwidth=10, padx=20, command=nextPage, font="georgia 16 bold",
             bg="green", fg="white", activebackground="green", activeforeground="white")
btn.place(x=630, y=680)

btn1 = Button(ws, text="EXIT", borderwidth=10, padx=20, command=quit, font="georgia 16 bold",
             bg ="red", fg="white", activebackground="red", activeforeground="white")
btn1.place(x=780, y=680)

ws.mainloop()
