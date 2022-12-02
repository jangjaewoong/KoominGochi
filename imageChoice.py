import tkinter
import random

class image:
    def __init__(self):
        self.kookmin_image = tkinter.PhotoImage(file='images/sleep.png')
        self.x = 160
        self.y = 180

    def imageOut(self, btn):
        if btn == 'club':
            self.kookmin_image = tkinter.PhotoImage(file='images/club1.png')
            self.x = 200
        elif btn == 'sleep':
            self.kookmin_image = tkinter.PhotoImage(file='images/sleep.png')
            self.x = 160
        elif btn == 'lectureRoom':
            self.kookmin_image = tkinter.PhotoImage(file='images/class.png')
            self.x = 200
        elif btn == 'gym':
            self.kookmin_image = tkinter.PhotoImage(file='images/health.png')
            self.x = 200
        elif btn == 'gs':
            self.kookmin_image = tkinter.PhotoImage(file='images/gs.png')
            self.x = 200
        elif btn == 'build':
            self.kookmin_image = tkinter.PhotoImage(file='images/build.png')
            self.x = 210
        elif btn == 'pc':
            self.kookmin_image = tkinter.PhotoImage(file='images/pc.png')
            self.x = 140
        elif btn == 'movie':
            self.kookmin_image = tkinter.PhotoImage(file='images/movie.png')
            self.x = 200
        elif btn == 'shopping':
            self.kookmin_image = tkinter.PhotoImage(file='images/shopping.png')
            self.x = 220


