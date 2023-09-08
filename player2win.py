from tkinter import *
from PIL import Image, ImageTk
import tkvideo
import time
import pygame

ws = Tk()
ws.state('zoomed')
ws.title('UNO GAME')
ws['bg'] = '#000000'
image = Image.open("images/player2win.png")
resize_img = image.resize((1550, 850), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resize_img)

can_widght = Canvas(ws, height=850, width=1550)
can_widght.create_image(768, 430, image=img)
can_widght.pack()

sec = StringVar()
sec.set('4')

pygame.mixer.init()


def play():
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.play(loops=0)


play()


def countdowntimer():
    times = int(sec.get())
    while times >= 0:
        ws.update()
        time.sleep(1)
        if times == 0:
            quit()
        times -= 1


countdowntimer()
ws.mainloop()
