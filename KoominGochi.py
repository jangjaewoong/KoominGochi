import tkinter
import tkinter.font
from tkinter import*
import random

import pickle



from PyQt5.QtWidgets import QApplication
from imageChoice import image
from Day import day
import tkinter.ttk
from Ending import ending
from action import Action
import midtermtest
import sys

import time

from ifdie import ifdie


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
        self.back_image = tkinter.PhotoImage(file='../../Desktop/소프/KoominGochi/images/back_home.png')
        self.backimg = tkinter.Label(self.window, image=self.back_image)
        self.backimg.place(x=-2, y=-2)

        # self.window.wm_attributes('-transparentcolor', "white")




        #장소 버튼들
        self.button_school = tkinter.Label(self.window, text='학교',width=8,height=2, fg="blue")
        self.button_school.place(x=90, y=530)
        self.button_club = tkinter.Button(self.window, text='동아리', width=6, height=2, fg="blue", command = lambda: self.btn_clicked('club'))
        self.button_club.place(x=95, y=585)
        self.button_lectureRoom = tkinter.Button(self.window, text='강의실', width=6, height=2, fg="blue", command= lambda: self.btn_clicked('lectureRoom'))
        self.button_lectureRoom.place(x=95, y=640)
        self.button_gym = tkinter.Button(self.window, text='웰니스', width=6, height=2, fg="blue", command= lambda: self.btn_clicked('gym'))
        self.button_gym.place(x=95, y=695)

        self.button_job = tkinter.Label(self.window, text='알바',width=8,height=2, fg='red')
        self.button_job.place(x=265, y=530)
        self.button_gs = tkinter.Button(self.window, text='편의점', width=6, height=2, fg="red", command= lambda: self.btn_clicked('gs'))
        self.button_gs.place(x=270, y=585)
        self.button_build = tkinter.Button(self.window, text='공사장', width=6, height=2, fg="red", command= lambda: self.btn_clicked('build'))
        self.button_build.place(x=270, y=640)

        self.button_joy = tkinter.Label(self.window, text='여가생활',width=8,height=2, fg='green')
        self.button_joy.place(x=440, y=530)
        self.button_pc = tkinter.Button(self.window, text='PC방', width=6, height=2, fg="green", command= lambda: self.btn_clicked('pc'))
        self.button_pc.place(x=445, y=585)
        self.button_movie = tkinter.Button(self.window, text='영화관', width=6, height=2, fg="green", command= lambda: self.btn_clicked('movie'))
        self.button_movie.place(x=445, y=640)
        self.button_shopping = tkinter.Button(self.window, text='쇼핑', width=6, height=2, fg="green", command= lambda: self.btn_clicked('shopping'))
        self.button_shopping.place(x=445, y=695)
        self.button_sleep = tkinter.Button(self.window, text='자러가기', width=6, height=2, fg="black", command= lambda: self.btn_clicked('sleep'))
        self.button_sleep.place(x=270, y=720)

        #쿠민이 이미지
        self.label = tkinter.Label(self.window, image=self.img.kookmin_image)
        self.label.place(x=self.img.x, y=self.img.y)

        #말풍선

        text_image = tkinter.PhotoImage(file='messageBox.png')
        label2 = tkinter.Label(self.window, image=text_image)
        label2.place(x=85, y=400)
        font1 = tkinter.font.Font(size=16, weight="bold")
        self.label3 = tkinter.Label(self.window, text="안녕하세요!", bg="white", compound="top", font=font1)

        self.label3.place(x=130,y=445)


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
        button_hp.place(x=470, y=252)


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
        self.bar_hp.place(x=520, y=250)




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

        #저장 불러오기 버튼
        self.button_save = tkinter.Button(self.window, text="저장하기", width=6, command= lambda: self.btn_clicked('save'))
        self.button_save.place(x=500, y=12)
        self.button_load = tkinter.Button(self.window, text="불러오기", width=6, command= lambda: self.btn_clicked('load'))
        self.button_load.place(x=500, y=48)


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
            self.label3["text"] = self.selecttext(6)
            self.progressbar_status()
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
        self.bar_intellect['text'] = self.act.int
        self.bar_charm['text'] = self.act.char
        self.bar_money['text'] = self.act.money
        self.bar_lonely['text'] = self.act.lon
        self.bar_stress['text'] = self.act.str
        self.button_day['text'] = "Day "+ str(self.act.day)
        self.bar_day['text'] = str(self.d.daypercent(self.act.day)) + "%"
        self.label['image'] = self.img.kookmin_image
        self.label.place(x=self.img.x, y=self.img.y)
        self.no_HP()

        if not self.act.Gameover():
            self.app2 = QApplication(sys.argv)
            self.dieWindow = ifdie()
            self.dieWindow.show()
            self.app2.exec_()


    def saving(self):

        savefile = [self.act.HP,self.act.int,self.act.char,self.act.str,self.act.lon,self.act.money,self.act.day]

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
        cls_text=["나도 쿠순이랑 친해지고 싶다" , "스트레스가 확 풀려!!", "10시에 지세 앞으로?? 오케이" , "오늘 술집은 어디로 가나요?ㅎㅎ"
                , "역시 대학 Life는 동아리지!", "선배! 밥 사주세요~", "이게 대학생활이지~크으~", "오늘은 회식이다!",
                  "실례가 안 된다면 밥 좀 사 주십쇼 선배!", "00101011001001001010110", "왜 컴파일이 안되냐고!!"]
        club_text=["이번 과제 꽤 어려운걸", "교수님 살려주세요", "할만한걸??" , "하.. 불태웠다..", "아 또!!! Error!!", "코딩은 그저 내 손이 해줄뿐 믿고 따라가 버렷!"
                    , "어? 이게 된다고?", "이...이게 왜 되는거여", "교수님 진도가 너무 빠릅니다", "아...집에 가고 싶다...", "동방에 사람 많나요??"
                   "오늘 회식은 주당끼리에서 할까요?", "신규 부원 모집~~" ]
        gym_text=["내 광배근에는 용이 살아", "내 대퇴사두의 데피니션을 보라구!", "마무리 유산소는 인정이지", "득근득근!!"
                    , "와 오늘 잘 먹었는데?", "프..로..틴…" , "고통은 잠시일뿐..", "이러다 보디빌더 되는 거 아닌가 몰라", "한다! 운동! 키운다! 근육!",
                  "프로티이이이인!!!", "오늘이 하체 하는 날인가?" , "3대 500을 향해서!!", "혹시.. 이 기구는 어떻게 사용하는 건가요?"]
        Cu_text=["어서오세요!!", "진짜 포켓몬 빵 없다니까요...", "열심히 돈 벌어야지!", "어서오세요~ KS25입니다."
            , "말보루 레드요??", "사장님!! 월급 언제 주시나요!!", "알바 언제 끝나지...", "삼각김밥 남는거 있나?"
                 ,"손님~ 민증 검사좀 하겠습니다.", "오늘은 제발 진상들 오지 말아라.. 제발!"]
        gada_text=["몸이 안움직여...", "자고 싶다", "김반장님 여기 월드콘 사왔습니다!" , "내 몸은 털털~ 잔고는 빵빵~", "반장님 : 어이 쿠씨! 여기 좀 와봐~~"
                , "하하하하핳ㅎ하하핳하하하하ㅏㅏ", "적게 일하고...많이 벌고 싶다..." , "힘세고 강한 노동!", "돈이...제일 소중해...최고여..."
                   , "이번 달 까지만 하고 그만두자...", "반장님 : 쿠씨! 끝나고 막걸리 한잔 어때?", "(도망가고 싶다)"]
        Pc_text=[ "서폿 야스오 한판 해볼까?", "이게 죽어?", "이게 맞아?", "소환사 협곡에 오신 여러분 환영합니다.", "삶의 낙은 역시 pc방에서 라면 먹는 거지!!!"
                , "아!!! 갱 좀 오라구!!!!", "우리 정글 뭐함?!?!", "아니! 이게 안 맞네?", "아아니! 이게 맞네?", "ㅈㄱㅊㅇ 오지네.."
                  , "우리 서폿은 어디서 뭐해!!"]
        Mov_text=["범죄도시11 진짜 미쳤다!", "이야 아이언맨이 살아있었다고??", "이런 복선이 숨어 있었구만", "12월 14일 아바타 개봉!!!!!", "나랑 같이 영화 보러 갈래?"
                  , "앞 사람 머리크기 때문에!!! 영화 3분의 1을 못 봤어!!!", "절름발이가 범인!!!", "팝콘은 단짠 반반이지~", "오...역시 세기의 명작..."
                  "혹시 오리지널 티켓 받을 수 있나요?", "이 영화관 팝콘 잘하네.. 냠냠"]
        shop_text=["욜로~!!" , "돈은 쓰려고 모으는거 아냐?" , "70%할인?? 바로 가야지", "빠끄~~ Flex 해버버렸지 모얌 빠끄~",
                   "오늘은 Gucci~Gucci~", "잔고는 텅텅~ 옷장은 빵빵~", "이게 삶의 낙이지~", "다음 달 생활비는 다음 달에 생각해야지~"
                   ,"플렉스 해버렸다!", "남탓은 해도 된다.. 우린 남이니까..", "내용은 좋은데 결말이 좀 아쉽네.."
                   , "무슨 옷 한벌이 50만원이야??", "정승같이 벌어서 개같이 쓴다!!", "3개월 할부요~"]
        sleep_text=["쿨..쿨...", "잘자요", "음...쩝쩝", "히히", "5분만 더...", "피로가 노곤노곤해져요" ]
        selText = [cls_text,club_text,gym_text,Cu_text,gada_text,Pc_text,
                   Mov_text,shop_text,sleep_text]
        return random.choice(selText[n])

    def no_HP(self):
        cost_2 = [self.button_gs,self.button_gym]
        cost_3 = [self.button_movie, self.button_pc, self.button_club
                  ,self.button_shopping,self.button_lectureRoom]
        cost_7 = [self.button_build]
        sum = cost_2+cost_3+cost_7
        if self.act.HP < 7:
            for i in cost_7:
                i["state"]=tkinter.DISABLED

        if self.act.HP <3:
            for i in cost_3:
                i["state"]= tkinter.DISABLED
        if self.act.HP <2:
            for i in cost_2:
                i["state"] = tkinter.DISABLED
        if self.act.HP == 10:
            for i in sum:
                i["state"] = tkinter.NORMAL





if __name__ == "__main__":
    game = KoominGochi()
    sys.exit(game.app.exec_())
