import tkinter
import tkinter.font
from tkinter import*
import random
from PyQt5.QtWidgets import QApplication
from imageChoice import image
from Day import day
import tkinter.ttk
from Ending import ending
from action import Action
import midtermtest
import sys
import time

class KoominGochi():

    def __init__(self):
        #윈도우 창 띄우기
        self.d = day()
        self.act = Action()
        self.window = Tk()
        self.img = image()
        self.window.title("KoominGochi")
        self.window.geometry("600x800")
        #window.configure(bg='white')
        self.window.resizable(width=False, height=False)
        self.app = QApplication(sys.argv)
        self.test = midtermtest.MidTermTest(0)
        self.p_var2 = DoubleVar()

        #배경화면 설정
        self.back_image = tkinter.PhotoImage(file='images/back_home.png')
        self.backimg = tkinter.Label(self.window, image=self.back_image)
        self.backimg.place(x=-2, y=-2)

        # self.window.wm_attributes('-transparentcolor', "white")



        #장소 버튼들
        button_school = tkinter.Button(self.window, text='학교',width=8,height=2, fg="blue")
        button_school.place(x=80, y=500)
        button_club = tkinter.Button(self.window, text='동아리', width=6, height=2, fg="blue", command = lambda: self.btn_clicked('club'))
        button_club.place(x=90, y=555)
        button_lectureRoom = tkinter.Button(self.window, text='강의실', width=6, height=2, fg="blue", command= lambda: self.btn_clicked('lectureRoom'))
        button_lectureRoom.place(x=90, y=610)
        button_gym = tkinter.Button(self.window, text='웰니스', width=6, height=2, fg="blue", command= lambda: self.btn_clicked('gym'))
        button_gym.place(x=90, y=665)

        button_job = tkinter.Button(self.window, text='알바',width=8,height=2, fg='red')
        button_job.place(x=250, y=500)
        button_gs = tkinter.Button(self.window, text='편의점', width=6, height=2, fg="red", command= lambda: self.btn_clicked('gs'))
        button_gs.place(x=260, y=555)
        button_build = tkinter.Button(self.window, text='공사장', width=6, height=2, fg="red", command= lambda: self.btn_clicked('build'))
        button_build.place(x=260, y=610)

        button_joy = tkinter.Button(self.window, text='여가생활',width=8,height=2, fg='green')
        button_joy.place(x=430, y=500)
        button_pc = tkinter.Button(self.window, text='PC방', width=6, height=2, fg="green", command= lambda: self.btn_clicked('pc'))
        button_pc.place(x=440, y=555)
        button_movie = tkinter.Button(self.window, text='영화관', width=6, height=2, fg="green", command= lambda: self.btn_clicked('movie'))
        button_movie.place(x=440, y=610)
        button_shopping = tkinter.Button(self.window, text='쇼핑', width=6, height=2, fg="green", command= lambda: self.btn_clicked('shopping'))
        button_shopping.place(x=440, y=665)
        button_sleep = tkinter.Button(self.window, text='자러가기', width=6, height=2, fg="black", command= lambda: self.btn_clicked('sleep'))
        button_sleep.place(x=260, y=720)

        #쿠민이 이미지
        self.label = tkinter.Label(self.window, image=self.img.kookmin_image)
        self.label.place(x=self.img.x, y=self.img.y)

        #말풍선
        self.text_image = tkinter.PhotoImage(file='images/messageBox.png')
        self.label2 = tkinter.Label(self.window, image=self.text_image)
        self.label2.place(x=140, y=400)

        #능력치 이름바[지능, 매력, 돈, 외로움, 스트레스, 체력]
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
        button_hp = tkinter.Label(self.window, text='HP', width=6, height=1)
        button_hp.place(x=465, y=252)


        #능력치 상태바[지능, 매력, 돈, 외로움, 스트레스, 체력, 잠자기]
        self.bar_intellect = tkinter.Button(self.window, text=self.act.int, width=6, bg='green')
        self.bar_intellect.place(x=60, y=100)
        self.bar_charm = tkinter.Button(self.window, text=self.act.char, width=6, bg='green')
        self.bar_charm.place(x=60, y=130)
        self.bar_money = tkinter.Button(self.window, text=self.act.money, width=6, bg='green')
        self.bar_money.place(x=60, y=160)
        self.bar_lonely = tkinter.Button(self.window, text=self.act.lon, width=6, bg='green')
        self.bar_lonely.place(x=60, y=190)
        self.bar_stress = tkinter.Button(self.window, text=self.act.str, width=6, bg='green')
        self.bar_stress.place(x=60, y=220)
        self.bar_hp = tkinter.Button(self.window, text=self.act.HP, width=6, bg='green')
        self.bar_hp.place(x=450, y=280)


        #날짜
        self.button_day = tkinter.Label(self.window, text="Day " + str(self.act.day), width=6)
        self.button_day.place(x=0, y=12)
        #날짜 상태바
        self.bar_day = tkinter.Button(self.window, text=str(self.d.daypercent(self.act.day)) + "%", width=10, bg='green')
        self.bar_day.place(x=60, y=10)
        #프로그래스바
        self.progressbar = tkinter.ttk.Progressbar(self.window, maximum=100, length=150, variable=self.p_var2)
        '''
        # 엔딩 버튼 생성
        font = tkinter.font.Font(family='Consolas', size=100)
        self.ending = tkinter.Label(self.window, text="Ending.calu()", fg="pink", font=font)
        self.ending.pack(side='right')
        '''
        self.window.mainloop()
    def progressbar_status(self):
        self.progressbar = tkinter.ttk.Progressbar(self.window, maximum=100, length=150, variable=self.p_var2)
        self.progressbar.place(x=225, y=295)
        for i in range(1,101):
            time.sleep(0.01)
            self.p_var2.set(i)
            self.progressbar.update()
        self.progressbar.destroy()

    #버튼 클릭 후 정보 UPdate!!
    def btn_clicked(self, button):
        if button == 'club':
            self.act.goClub()
            self.img.imageOut('club')
            self.progressbar_status()
        elif button == 'lectureRoom':
            self.act.goClass()
            self.img.imageOut('lectureRoom')
            self.progressbar_status()
        elif button == 'gym':
            self.act.goGym()
            self.img.imageOut('gym')
            self.progressbar_status()
        elif button == 'gs':
            self.act.goCU()
            self.img.imageOut('gs')
            self.progressbar_status()
        elif button == 'build':
            self.act.goNogada()
            self.img.imageOut('build')
            self.progressbar_status()
        elif button == 'pc':
            self.act.goPC()
            self.img.imageOut('pc')
            self.progressbar_status()
        elif button == 'movie':
            self.act.goMovie()
            self.img.imageOut('movie')
            self.progressbar_status()
        elif button == 'shopping':
            self.act.goshop()
            self.img.imageOut('shopping')
            self.progressbar_status()
        elif button == 'sleep':
            self.act.gosleep()
            self.img.imageOut('sleep')
            self.progressbar_status()


        self.bar_hp['text'] = self.act.HP
        self.bar_intellect['text'] = self.act.int
        self.bar_charm['text'] = self.act.char
        self.bar_money['text'] = self.act.money
        self.bar_lonely['text'] = self.act.lon
        self.bar_stress['text'] = self.act.str
        self.button_day['text'] = "Day "+ str(self.act.day)
        self.bar_day['text'] = str(self.d.daypercent(self.act.day)) + "%"
        self.label['image'] = self.img.kookmin_image
        self.label.place(x=self.img.x, y=self.img.y)





if __name__ == "__main__":
    game = KoominGochi()
    sys.exit(game.app.exec_())
