import pygame
import sys
import images


class ClickGame():
    def __init__(self):
        self.screen_width = 480
        self.screen_height = 640
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.game_font = pygame.font.Font("NanumBarunGothic.ttf", 20)  # 폰트 객체 생성 (폰트(디폴트 값), 크기)
        self.centerPos = [(self.screen_width / 2), (self.screen_height / 2)]
        self.score = 0

    def quitGame(self):
        pygame.quit()
        sys.exit()

    def setScore(self):
        self.score = 0


    def gamePlay(self):
        score = 0
        btnCenterPos = [self.centerPos[0] - 50, self.centerPos[1] - 25]

        # 시간
        start_ticks = pygame.time.get_ticks()  # 시작 tick 받기
        total_time = 10
        enlapsed_time = 0

        miniGame = True
        gaming = False
        timeOut = False

        timer = self.game_font.render(str(total_time), True, (0, 0, 0))
        while miniGame:
            self.screen.fill((255, 255, 255))

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if btnCenterPos[0] + 100 > mouse[0] > btnCenterPos[0] and btnCenterPos[1] + 50 > mouse[1] > btnCenterPos[1] \
                    and not timeOut:  # 마우스가 버튼 위에 위치할 때
                self.screen.blit(images.clickGameBtn2, (btnCenterPos[0], btnCenterPos[1]))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if not gaming:
                            gaming = True
                        score += 1
            else:
                self.screen.blit(images.clickGameBtn1, (btnCenterPos[0], btnCenterPos[1]))
            if gaming and not timeOut:
                enlapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 - 1
                if total_time - enlapsed_time <= 0:
                    timeOut = True
                # screen.blit(timer, (10, 10))
            if gaming and timeOut:
                if score > self.score:
                    self.score = score
                return

            timer = self.game_font.render(str(int(total_time - enlapsed_time)), True, (0, 0, 0))
            scoreTxt = self.game_font.render('점수: ' + str(score), True, (0, 0, 0))

            self.screen.blit(timer, (10, 10))
            self.screen.blit(scoreTxt, (10, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()

            pygame.display.update()


if __name__ == "__main__":
    game = ClickGame()
    game.gamePlay()
