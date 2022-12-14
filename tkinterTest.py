# [게임이미지]
# 배경 : 480*640(가로세로)
# 캐릭터 : 50*50
# 똥 : 50*50
# 버튼 : 100*50

import tkinter
import minigame

avoidGame = minigame.AvoidGame()
clickGame = minigame.ClickGame()

window = tkinter.Tk()
score1 = tkinter.StringVar()
score1.set(str(avoidGame.score))
score2 = tkinter.StringVar()
score2.set(str(clickGame.score))


def playAvoidGame():
    avoidGame.set(70)
    score1.set(str(avoidGame.score))


def playClickGame():
    clickGame.set(70)
    score2.set(str(clickGame.score))


window.title('히힠 티킨터 히히힠')
window.geometry("640x400+100+100")
button = tkinter.Button(window, command=playAvoidGame, text='야! 이건 똥피하기다!!!')
button.pack()
label = tkinter.Label(window, textvariable=score1)
label.pack()
button = tkinter.Button(window, command=playClickGame, text='야! 이건 수강신청 게임이다!!!')
button.pack()
label = tkinter.Label(window, textvariable=score2)
label.pack()

window.mainloop()
