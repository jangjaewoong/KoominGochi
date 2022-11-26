import tkinter
import tkinter.ttk as ttk
from PyQt5.QtWidgets import*
from tkinter import*
import random
from Day import day

from Action import Action
class KoominGochi():

    def __init__(self):
        d = day()
        Act = Action()
        #윈도우 창 띄우기
        self.window = Tk()
        self.window.title("KoominGochi")
        self.window.geometry("600x800")
        #window.configure(bg='white')
        self.window.resizable(width=False, height=False)

        #장소 버튼들
        button_school = tkinter.Button(self.window, text='학교',width=8,height=2, fg="blue")
        button_school.place(x=80, y=460)
        button_club = tkinter.Button(self.window, text='동아리', width=6, height=2, fg="blue", state="normal" , command=Act.goClub())
        button_club.place(x=90, y=515)
        button_lectureRoom = tkinter.Button(self.window, text='강의실', width=6, height=2, fg="blue")
        button_lectureRoom.place(x=90, y=560)
        button_gym = tkinter.Button(self.window, text='웰니스', width=6, height=2, fg="blue")
        button_gym.place(x=90, y=605)

        button_job = tkinter.Button(self.window, text='알바',width=8,height=2, fg='red')
        button_job.place(x=250, y=460)
        button_gs = tkinter.Button(self.window, text='편의점', width=6, height=2, fg="red")
        button_gs.place(x=260, y=515)
        button_build = tkinter.Button(self.window, text='공사장', width=6, height=2, fg="red")
        button_build.place(x=260, y=560)

        button_joy = tkinter.Button(self.window, text='여가생활',width=8,height=2, fg='green')
        button_joy.place(x=430, y=460)
        button_pc = tkinter.Button(self.window, text='PC방', width=6, height=2, fg="green")
        button_pc.place(x=440, y=515)
        button_movie = tkinter.Button(self.window, text='영화관', width=6, height=2, fg="green")
        button_movie.place(x=440, y=560)
        button_shopping = tkinter.Button(self.window, text='쇼핑', width=6, height=2, fg="green")
        button_shopping.place(x=440, y=605)

        #쿠민이 이미지
        self.kookmin_image = tkinter.PhotoImage(file='sleep.png')
        self.label = tkinter.Label(self.window, image=self.kookmin_image)
        self.label.place(x=150, y=180)

        #말풍선
        text_image = tkinter.PhotoImage(file='text.png')
        label2 = tkinter.Label(self.window, image=text_image)
        label2.place(x=350, y=65)

        #능력치 이름바[지능, 매력, 돈, 외로움, 스트레스]
        button_intellect = tkinter.Label(self.window, text='지능',width=6, height=1)
        button_intellect.place(x=0, y=102)
        button_charm = tkinter.Label(self.window, text='매력',width=6,height=1)
        button_charm.place(x=0, y=132)
        button_money = tkinter.Label(self.window, text='돈',width=6, height=1)
        button_money.place(x=0, y=162)
        button_lonely = tkinter.Label(self.window, text='외로움',width=6, height=1)
        button_lonely.place(x=0, y=192)
        button_stress = tkinter.Label(self.window, text='스트레스',width=6, height=1)
        button_stress.place(x=0, y=222)

        #능력치 상태바[지능, 매력, 돈, 외로움, 스트레스]
        bar_intellect = tkinter.Button(self.window, text=Act.int, width=6, bg='green')
        bar_intellect.place(x=60, y=100)
        bar_charm = tkinter.Button(self.window, text=Act.char, width=6, bg='green')
        bar_charm.place(x=60, y=130)
        bar_money = tkinter.Button(self.window, text=Act.money , width=6, bg='green')
        bar_money.place(x=60, y=160)
        bar_lonely = tkinter.Button(self.window, text=Act.lon, width=6, bg='green')
        bar_lonely.place(x=60, y=190)
        bar_stress = tkinter.Button(self.window, text=Act.str, width=6, bg='green')
        bar_stress.place(x=60, y=220)

        #날짜
        button_day = tkinter.Label(self.window, text=d.showday(),width=6)
        button_day.place(x=0, y=12)
        #날짜 상태바
        bar_day = tkinter.Button(self.window, text=d.daypercent(), width=10, bg='green')
        bar_day.place(x=60, y=10)

        self.window.mainloop()

    def schoolWindow(self):
        self.kookmin_image = tkinter.PhotoImage(file='kookmin1.png')
        self.label = tkinter.Label(self.window, image=self.kookmin_image)
        self.label.place(x=140, y=170)








if __name__ == "__main__":
    game = KoominGochi()
