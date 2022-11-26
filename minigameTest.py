# [게임이미지]
# 배경 : 480*640(가로세로)
# 캐릭터 : 50*50
# 똥 : 50*50
# 버튼 : 100*50


# ****게임 종료 후 메뉴로 돌아갈 때, 복귀 버튼과 게임 실행 버튼이 같은 좌표에 있다면 바로 실행됨. 버튼 배치에 유의할 것****


import pygame
import sys
import images
import gameAvoid, gameClick


# 초기 설정
pygame.init()
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("미니 게임")

clock = pygame.time.Clock()
clock.tick(60)

game_font = pygame.font.Font("NanumBarunGothic.ttf", 20)  # 폰트 객체 생성 (폰트(디폴트 값), 크기)
centerPos = [(screen_width / 2), (screen_height / 2)]
game1Score = 0
game2Score = 0

avoidGame = gameAvoid.AvoidGame()
clickGame = gameClick.ClickGame()


# 버튼 클래스
class Button:
    def __init__(self, img_in, img_act, x, y, width, height, action=None):
        mouse = pygame.mouse.get_pos()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            screen.blit(img_act, (x, y))
            if pygame.event.poll().type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                action()
        else:
            screen.blit(img_in, (x, y))


def quitGame():
    pygame.quit()
    sys.exit()


# 메인 화면
def mainMenu():
    while True:
        screen.fill((255, 255, 255))
        avoidGameBtn = Button(images.avoidBtn1, images.avoidBtn2, centerPos[0] - 50, centerPos[1] - 100,
                              100, 50, avoidGame.gamePlay)
        clickGameBtn = Button(images.clickBtn1, images.clickBtn2, centerPos[0] - 50, centerPos[1] + 50,
                              100, 50, clickGame.gamePlay)
        scoreTxt1 = game_font.render('똥피하기 최고점수: ' + str(avoidGame.score), True, (0, 0, 0))
        scoreTxt2 = game_font.render('클릭게임최고점수: ' + str(clickGame.score), True, (0, 0, 0))
        scoreTxt1Rect = scoreTxt1.get_rect(center=(centerPos[0], centerPos[1]-25))
        scoreTxt2Rect = scoreTxt2.get_rect(center=(centerPos[0], centerPos[1]+125))
        screen.blit(scoreTxt1, scoreTxt1Rect)
        screen.blit(scoreTxt2, scoreTxt2Rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        pygame.display.update()


if __name__ == '__main__':
    mainMenu()
