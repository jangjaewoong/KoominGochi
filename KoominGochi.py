import tkinter.font
import tkinter.ttk
from tkinter import *
import random
import pickle
from PyQt5.QtWidgets import QApplication
from imageChoice import image
from Day import day
from questions import cls_text, club_text, gym_text,\
                      Cu_text, gada_text, Pc_text, Mov_text, shop_text, sleep_text
import tkinter.ttk
from Ending import ending
from action import Action
import midtermtest
import sys
import time
from ifdie import ifdie
from PIL import Image, ImageTk


class KoominGochi():

    def __init__(self):
        # 윈도우 창 띄우기
        self.d = day()
        self.act = Action()
        self.window = Tk()
        self.img = image()
        self.window.title("KoominGochi")
        self.window.geometry("600x800")
        self.s = tkinter.ttk.Style()
        self.s.theme_use("default")
        self.s.configure("Pink.Horizontal.TProgressbar", troughcolor='white',
                         bordercolor='white', background='pink', lightcolor='pink',
                         darkcolor='pink', thickness=10)
        self.s.configure("Green.Horizontal.TProgressbar", troughcolor='white',
                         bordercolor='white', background='green', lightcolor='green',
                         darkcolor='green', thickness=10)
        # window.configure(bg='white')
        self.window.resizable(width=False, height=False)
        self.app = QApplication(sys.argv)
        self.test = midtermtest.MidTermTest(0)

        self.p_var2 = DoubleVar()
        # 프레임 설정
        self.frame = Frame(self.window)
        self.frame.pack()
        # 캔버스 설정
        self.canvas = Canvas(self.frame, bg="black", width=600, height=800)
        self.canvas.pack()

        # 배경화면 설정
        self.image = Image.open('images/back_home.png')
        self.image_resize = self.image.resize((1200,1600))
        self.back_image = ImageTk.PhotoImage(self.image_resize)
        self.canvas.create_image(0,0,image = self.back_image)
        # self.backimg = tkinter.Label(self.window, image=self.back_image)
        # self.backimg.place(x=-2, y=-2)

        # self.window.wm_attributes('-transparentcolor', "white")

        # 장소 버튼들
        self.button_school = tkinter.Label(self.window, text='학교', width=8, height=2, fg="blue")
        self.button_school.place(x=90, y=530)
        self.button_club = tkinter.Button(self.window, text='동아리', width=6, height=2, fg="blue",
                                          command=lambda: self.btn_clicked('club'))
        self.button_club.place(x=95, y=585)
        self.button_lectureRoom = tkinter.Button(self.window, text='강의실', width=6, height=2, fg="blue",
                                                 command=lambda: self.btn_clicked('lectureRoom'))
        self.button_lectureRoom.place(x=95, y=640)
        self.button_gym = tkinter.Button(self.window, text='웰니스', width=6, height=2, fg="blue",
                                         command=lambda: self.btn_clicked('gym'))
        self.button_gym.place(x=95, y=695)

        self.button_job = tkinter.Label(self.window, text='알바', width=8, height=2, fg='red')
        self.button_job.place(x=265, y=530)
        self.button_gs = tkinter.Button(self.window, text='편의점', width=6, height=2, fg="red",
                                        command=lambda: self.btn_clicked('gs'))
        self.button_gs.place(x=270, y=585)
        self.button_build = tkinter.Button(self.window, text='공사장', width=6, height=2, fg="red",
                                           command=lambda: self.btn_clicked('build'))
        self.button_build.place(x=270, y=640)

        self.button_joy = tkinter.Label(self.window, text='여가생활', width=8, height=2, fg='green')
        self.button_joy.place(x=440, y=530)
        self.button_pc = tkinter.Button(self.window, text='PC방', width=6, height=2, fg="green",
                                        command=lambda: self.btn_clicked('pc'))
        self.button_pc.place(x=445, y=585)
        self.button_movie = tkinter.Button(self.window, text='영화관', width=6, height=2, fg="green",
                                           command=lambda: self.btn_clicked('movie'))
        self.button_movie.place(x=445, y=640)
        self.button_shopping = tkinter.Button(self.window, text='쇼핑', width=6, height=2, fg="green",
                                              command=lambda: self.btn_clicked('shopping'))
        self.button_shopping.place(x=445, y=695)
        self.button_sleep = tkinter.Button(self.window, text='자러가기', width=6, height=2, fg="black",
                                           command=lambda: self.btn_clicked('sleep'))
        self.button_sleep.place(x=270, y=720)

        # 쿠민이 이미지
        # self.label = tkinter.Label(self.window, image=self.img.kookmin_image)
        # self.label.place(x=self.img.x, y=self.img.y)
        self.canvas.create_image(300, 310, image=self.img.kookmin_image,tags='kookmin image')

        # 말풍선

        self.text_image = ImageTk.PhotoImage(Image.open('messageBox.png'))
        self.canvas.create_image(300,455,image = self.text_image)
        # label2 = tkinter.Label(self.window, image=text_image)
        # label2.place(x=85, y=400)
        font1 = tkinter.font.Font(size=16, weight="bold")
        self.label3 = tkinter.Label(self.window, text="안녕하세요!", bg="white", compound="top", font=font1)

        self.label3.place(x=130, y=445)

        # 능력치 이름바[지능, 매력, 돈, 외로움, 스트레스, 체력]
        button_intellect = tkinter.Label(self.window, text='지능', width=6, height=1)
        button_intellect.place(x=0, y=102)
        button_charm = tkinter.Label(self.window, text='매력', width=6, height=1)
        button_charm.place(x=0, y=132)
        button_money = tkinter.Label(self.window, text='돈', width=6, height=1)
        button_money.place(x=0, y=162)
        button_lonely = tkinter.Label(self.window, text='외로움', width=6, height=1)
        button_lonely.place(x=0, y=192)
        button_stress = tkinter.Label(self.window, text='스트레스', width=6, height=1)
        button_stress.place(x=0, y=222)
        button_hp = tkinter.Label(self.window, text='HP', width=6, height=1)
        button_hp.place(x=470, y=252)

        # 능력치 상태바[지능, 매력, 돈, 외로움, 스트레스, 체력, 잠자기]
        # self.bar_intellect = tkinter.Button(self.window, text=self.act.int, width=6, bg='green')
        # self.bar_intellect.place(x=60, y=100)
        self.intellect = IntVar()
        self.intellect.set(50)
        self.bar_intellect = tkinter.ttk.Progressbar(self.window, maximum=100, orient='horizontal',
                                                     length=150, style='Pink.Horizontal.TProgressbar'
                                                     , variable=self.intellect)
        self.bar_intellect.place(x=60, y=100)
        # self.bar_charm = tkinter.Button(self.window, text=self.act.char, width=6, bg='green')
        # self.bar_charm.place(x=60, y=130)
        self.charm = IntVar()
        self.charm.set(50)
        self.bar_charm = tkinter.ttk.Progressbar(self.window, maximum=100, orient='horizontal',
                                                 length=150, style='Pink.Horizontal.TProgressbar'
                                                 , variable=self.charm)
        self.bar_charm.place(x=60, y=130)

        self.bar_money = tkinter.Button(self.window, text=self.act.money, width=10, bg='green')
        self.bar_money.place(x=60, y=160)

        # self.bar_lonely = tkinter.Button(self.window, text=self.act.lon, width=6, bg='green')
        # self.bar_lonely.place(x=60, y=190)
        self.lonely = IntVar()
        self.lonely.set(50)
        self.bar_lonely = tkinter.ttk.Progressbar(self.window, maximum=100, orient='horizontal',
                                                  length=150, style='Pink.Horizontal.TProgressbar',
                                                  variable=self.lonely)
        self.bar_lonely.place(x=60, y=190)
        # self.bar_stress = tkinter.Button(self.window, text=self.act.str, width=6, bg='green')
        # self.bar_stress.place(x=60, y=220)
        self.stress = IntVar()
        self.stress.set(50)
        self.bar_stress = tkinter.ttk.Progressbar(self.window, maximum=100, orient='horizontal',
                                                  length=150, style='Pink.Horizontal.TProgressbar',
                                                  variable=self.stress)
        self.bar_stress.place(x=60, y=220)

        self.bar_hp = tkinter.Button(self.window, text=self.act.HP, width=6, bg='green')
        self.bar_hp.place(x=520, y=250)
        # 날짜
        self.day = IntVar()
        self.day.set(self.d.daypercent(self.act.day))
        self.button_day = tkinter.Label(self.window, text="Day " + str(self.act.day), width=6)
        self.button_day.place(x=0, y=12)
        # 날짜 상태바
        self.bar_day = tkinter.ttk.Progressbar(self.window, maximum=100, orient='horizontal',
                                               length=400, style="Green.Horizontal.TProgressbar",
                                               variable=self.day)
        self.bar_day.place(x=60, y=10)
        # 프로그래스바
        self.progressbar = tkinter.ttk.Progressbar(self.window, maximum=100, length=150, variable=self.p_var2)
        '''
        # 엔딩 버튼 생성
        font = tkinter.font.Font(family='Consolas', size=100)
        self.ending = tkinter.Label(self.window, text="Ending.calu()", fg="pink", font=font)
        self.ending.pack(side='right')
        '''

        # 저장 불러오기 버튼
        self.button_save = tkinter.Button(self.window, text="저장하기", width=6, command=lambda: self.btn_clicked('save'))
        self.button_save.place(x=500, y=12)
        self.button_load = tkinter.Button(self.window, text="불러오기", width=6, command=lambda: self.btn_clicked('load'))
        self.button_load.place(x=500, y=48)

        self.window.mainloop()

    def progressbar_status(self):
        self.progressbar = tkinter.ttk.Progressbar(self.window, maximum=100, length=150, variable=self.p_var2)
        self.progressbar.place(x=225, y=295)
        for i in range(1, 101):
            time.sleep(0.01)
            self.p_var2.set(i)
            self.progressbar.update()
        self.progressbar.destroy()

    # 버튼 클릭 후 정보 UPdate!!
    def btn_clicked(self, button):
        if button == 'club':
            self.act.goClub()
            self.img.imageOut('club')
            self.progressbar_status()
            self.label3["text"] = self.selecttext(0)
        elif button == 'lectureRoom':
            self.act.goClass()
            self.img.imageOut('lectureRoom')
            self.progressbar_status()
            self.label3["text"] = self.selecttext(1)
        elif button == 'gym':
            self.act.goGym()
            self.img.imageOut('gym')
            self.progressbar_status()
            self.label3["text"] = self.selecttext(2)
        elif button == 'gs':
            self.act.goCU()
            self.img.imageOut('gs')
            self.progressbar_status()
            self.label3["text"] = self.selecttext(3)
        elif button == 'build':
            self.act.goNogada()
            self.img.imageOut('build')
            self.progressbar_status()
            self.label3["text"] = self.selecttext(4)
        elif button == 'pc':
            self.act.goPC()
            self.img.imageOut('pc')
            self.progressbar_status()
            self.label3["text"] = self.selecttext(5)
        elif button == 'movie':
            self.act.goMovie()
            self.img.imageOut('movie')
            self.progressbar_status()
            self.label3["text"] = self.selecttext(6)

        elif button == 'shopping':
            self.act.goshop()
            self.img.imageOut('shopping')
            self.progressbar_status()
            self.label3["text"] = self.selecttext(7)

        elif button == 'sleep':
            self.act.gosleep()
            self.img.imageOut('sleep')
            self.progressbar_status()
            self.label3["text"] = self.selecttext(8)

        elif button == 'save':
            self.saving()
            self.label3["text"] = "저장되었습니다!"
        elif button == 'load':
            self.loading()
            self.label3["text"] = "게임 정보를 불러왔습니다.!"

        self.bar_hp['text'] = self.act.HP
        self.intellect.set(self.act.int)
        self.charm.set(self.act.char)
        self.bar_money['text'] = self.act.money
        self.lonely.set(self.act.lon)
        self.stress.set(self.act.str)
        self.button_day['text'] = "Day " + str(self.act.day)
        self.day.set(self.d.daypercent(self.act.day))
        self.canvas.create_image(300, 310, image=self.img.kookmin_image,tags='kookmin image')
        self.no_HP()

        if not self.act.Gameover():
            self.app2 = QApplication(sys.argv)
            self.dieWindow = ifdie()
            self.dieWindow.show()
            self.app2.exec_()

    def saving(self):

        savefile = [self.act.HP, self.act.int, self.act.char, self.act.str, self.act.lon, self.act.money, self.act.day]

        with open("data.pickle", "wb") as file:
            pickle.dump(savefile, file)

    def loading(self):

        with open("data.pickle", "rb") as file:
            try:
                data = pickle.load(file)
            except EOFError:
                pass

            self.act.HP = data[0]
            self.act.int = data[1]
            self.act.char = data[2]
            self.act.str = data[3]
            self.act.lon = data[4]
            self.act.money = data[5]
            self.act.day = data[6]

    def schoolWindow(self):
        self.kookmin_image = tkinter.PhotoImage(file='kookmin1.png')
        self.label = tkinter.Label(self.window, image=self.kookmin_image)
        self.label.place(x=140, y=170)

    def selecttext(self, n):

        selText = [cls_text, club_text, gym_text, Cu_text, gada_text, Pc_text,
                   Mov_text, shop_text, sleep_text]
        return random.choice(selText[n])

    def no_HP(self):
        cost_2 = [self.button_gs, self.button_gym]
        cost_3 = [self.button_movie, self.button_pc, self.button_club
            , self.button_shopping, self.button_lectureRoom]
        cost_7 = [self.button_build]
        all_buttons = cost_2 + cost_3 + cost_7
        if self.act.HP < 7:
            for i in cost_7:
                i["state"] = tkinter.DISABLED

        if self.act.HP < 3:
            for i in cost_3:
                i["state"] = tkinter.DISABLED
        if self.act.HP < 2:
            for i in cost_2:
                i["state"] = tkinter.DISABLED
        if self.act.HP == 10:
            for i in all_buttons:
                i["state"] = tkinter.NORMAL


if __name__ == "__main__":
    game = KoominGochi()
    sys.exit(game.app.exec_())
