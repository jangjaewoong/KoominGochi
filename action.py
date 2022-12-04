import random
from Day import day
import sys
from PyQt5.QtWidgets import QApplication
import midtermtest
import minigame


class Action():

    def __init__(self):
        self.d = day()
        self.HP = 10
        self.int = 50
        self.char = 50
        self.lon= 50
        self.str = 50
        self.money = 10000
        self.day = 1
        self.midtestscore = 0

        self.avoidGameLauncher = minigame.AvoidGame()
        self.clickGameLauncher = minigame.ClickGame()

    def goClub(self):
        if self.HP < 3:
            return "체력이 부족합니다"
        else:
            self.str -= 5
            self.HP -= 3
            self.lon -= 5
            self.money -= 1500

    def goClass(self):
        #게임 불러오기
        if self.HP < 3:
            return "체력이 부족합니다"
        else:
            gameChoice = random.randint(0, 2)
            if gameChoice == 0:
                self.avoidGameLauncher.set(self.int)
                self.int += self.avoidGameLauncher.score // 4
            elif gameChoice == 1:
                self.clickGameLauncher.set(self.int)
                self.int += self.clickGameLauncher.score // 20
            # self.int += 5 #게임점수 계산
            self.str += 7
            self.lon += 7
            self.HP -= 3


    def goGym(self):

        if self.HP < 2:
            return "체력이 부족합니다"
        else:
            self.HP -= 2
            self.lon += 5
            self.money-= 1000
            self.char +=5

    def goCU(self):
        if self.HP < 3:
            return "체력이 부족합니다"
        else:
            self.HP -= 3
            self.money += 2500
            self.str += 5

    def goNogada(self):
        if self.HP < 7:
            return "체력이 부족합니다"
        else:
            self.HP -= 7
            self.money += 5500
            self.str += 8

    def goPC(self):
        if self.HP < 2:
            return "체력이 부족합니다"
        else:
            self.HP -= 2
            self.money -= 1500
            self.lon -= 4
            self.str -= 4
            self.int -= 10

    def goMovie(self):
        if self.HP < 3:
            return "체력이 부족합니다"
        else:
            self.HP -= 3
            self.money -= 2000
            self.lon -= 5
            self.str -= 6
            self.int -= 10

    def goshop(self):
        if self.HP < 3:
            return "체력이 부족합니다"
        else:
            self.HP -= 3
            self.money -= 3000
            self.char += 7
            self.int -= 10

    def gosleep(self):
        self.HP = 10
        self.money -= 1000
        self.lon += 5
        self.char -= 5
        self.day += 1
        self.int -= 5
        self.d.daypercent(self.day)

    def Test(self, difficulty):

        app = QApplication(sys.argv)
        test = midtermtest.MidTermTest(difficulty)
        test.show()
        app.exec_()

        self.midtestscore = test.score
        self.HP = 0


    def Gameover(self):
        self.gameover = True
        if self.money < 0:
            print("game over")
            self.gameover = False
            return self.gameover
        elif self.lon >= 100:
            print("game over")
            self.gameover = False
            return self.gameover
        elif self.str >= 100:
            print("game over")
            self.gameover = False
            return self.gameover
        elif self.day == 22:
            pass
        else:
            return self.gameover
