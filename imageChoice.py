import tkinter
import random

class image:
    def __init__(self):
        self.kookmin_image = tkinter.PhotoImage(file='image/sleep.png')
        self.x = 160
        self.y = 180

    def imageOut(self, btn):
        if btn == 'club':
            self.kookmin_image = tkinter.PhotoImage(file='image/club1.png')
            self.x = 200
        elif btn == 'sleep':
            self.kookmin_image = tkinter.PhotoImage(file='image/sleep.png')
            self.x = 160
        elif btn == 'lectureRoom':
            self.kookmin_image = tkinter.PhotoImage(file='image/class.png')
            self.x = 200
        elif btn == 'gym':
            self.kookmin_image = tkinter.PhotoImage(file='image/health.png')
            self.x = 200
        elif btn == 'gs':
            self.kookmin_image = tkinter.PhotoImage(file='image/gs.png')
            self.x = 200
        elif btn == 'build':
            self.kookmin_image = tkinter.PhotoImage(file='image/build.png')
            self.x = 210
        elif btn == 'pc':
            self.kookmin_image = tkinter.PhotoImage(file='image/pc.png')
            self.x = 140
        elif btn == 'movie':
            self.kookmin_image = tkinter.PhotoImage(file='image/movie.png')
            self.x = 200
        elif btn == 'shopping':
            self.kookmin_image = tkinter.PhotoImage(file='image/shopping.png')
            self.x = 220


