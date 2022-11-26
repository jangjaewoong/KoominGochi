import tkinter
import tkinter.ttk as ttk
from PyQt5.QtWidgets import*
from tkinter import*
import random

class KoominGochi():

    def __init__(self):
        #윈도우 창 띄우기
        window = Tk()
        window.title("KoominGochi")
        window.geometry("600x800")
        #window.configure(bg='white')
        window.resizable(width=False, height=False)

        button_school = tkinter.Button(window, text='학교',width=6,height=2, fg="blue")
        button_job = tkinter.Button(window, text='알바',width=6,height=2, fg='red')
        button_joy = tkinter.Button(window, text='여가생활',width=6,height=2, fg='green')
        button_school.place(x=100,y=600)
        button_job.place(x=250, y=600)
        button_joy.place(x=400, y=600)

        #쿠민이 이미지
        kookmin_image = tkinter.PhotoImage(file='kookmin1.png')
        label = tkinter.Label(window, image=kookmin_image)
        label.place(x=140, y=170)

        #말풍선
        text_image = tkinter.PhotoImage(file='text.png')
        label2 = tkinter.Label(window, image=text_image)
        label2.place(x=350, y=65)

        #능력치 이름바[지능, 매력, 돈, 외로움, 스트레스]
        button_intellect = tkinter.Button(window, text='지능',width=2, height=1)
        button_intellect.place(x=0, y=100)
        button_charm = tkinter.Button(window, text='매력',width=2, height=1)
        button_charm.place(x=0, y=130)
        button_money = tkinter.Button(window, text='돈',width=2, height=1)
        button_money.place(x=0, y=160)
        button_lonely = tkinter.Button(window, text='외로움',width=2, height=1)
        button_lonely.place(x=0, y=190)
        button_stress = tkinter.Button(window, text='스트레스',width=2, height=1)
        button_stress.place(x=0, y=220)

        #능력치 상태바[지능, 매력, 돈, 외로움, 스트레스]
        bar_intellect = tkinter.Button(window, text='50', width=5, bg='green')
        bar_intellect.place(x=50, y=100)
        bar_charm = tkinter.Button(window, text='50', width=5, bg='green')
        bar_charm.place(x=50, y=130)
        bar_money = tkinter.Button(window, text='10', width=5, bg='green')
        bar_money.place(x=50, y=160)
        bar_lonely = tkinter.Button(window, text='90', width=5, bg='green')
        bar_lonely.place(x=50, y=190)
        bar_stress = tkinter.Button(window, text='90', width=5, bg='green')
        bar_stress.place(x=50, y=220)

        #날짜
        button_day = tkinter.Button(window, text='Day 1',width=3)
        button_day.place(x=0, y=10)

        #날짜 상태바
        bar_day = tkinter.Button(window, text='10%', width=10, bg='green')
        bar_day.place(x=60, y=10)

        def school(self):





        window.mainloop()

game = KoominGochi()
