import pygame
import sys
import random
import images


"""
***수정할 것***
- 게임 시작 시 매개변수 받음. 그 값에 따라 오브젝트 수량 증가를 통한 난이도 조절. 오브젝트 속도로도 난이도 조절 가능할지?
    - 오브젝트 수량 증가에 따른 오브젝트 간 충돌 체크는 어떻게?

***효과음? 브금?
"""


class MiniGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("미니 게임")

        self.game_font = pygame.font.Font("NanumBarunGothic.ttf", 20)  # 폰트 객체 생성 (폰트(디폴트 값), 크기)
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.score = 0

    def quitGame(self):
        pygame.quit()
        sys.exit()

    def setScore(self):
        self.score = 0


class AvoidGame(MiniGame):
    def __init__(self):
        super().__init__()
        self.screen_width = 480
        self.screen_height = 640
        self.centerPos = [(self.screen_width / 2), (self.screen_height / 2)]

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), flags=pygame.HIDDEN)

    # 게임 실행할 때 호출해 줄 함수
    def set(self, know):
        self.setScore()
        diff = 0
        if know < 30:
            diff = 1.5
        elif 30 <= know < 70:
            diff = 1.0
        elif 70 <= know:
            diff = 0.5
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), flags=pygame.SHOWN)

        self.gamePlay(diff)

    def gamePlay(self, diff):
        # 캐릭터, 배경
        background = images.bgImg

        character = images.playerImg
        character_width = character.get_rect().size[0]  # 가로 크기
        character_height = character.get_rect().size[1]  # 세로 크기
        character_x_pos = self.centerPos[0] - character_width / 2  # 화면 가로의 가운데 위치
        character_y_pos = self.screen_height - character_height  # 화면 세로 크기 가장 아래

        # 점수 아이템
        point = images.Aobj
        point_width = point.get_rect().size[0]  # 가로 크기
        point_x_pos = random.randint(0, self.screen_width - point_width)  # 화면 가로의 랜덤 위치
        point_y_pos = -point_width * 4

        # 꽝 아이템
        enemy = images.Fobj
        enemy_width = enemy.get_rect().size[0]  # 가로 크기
        enemy_x_pos = random.randint(0, self.screen_width - enemy_width)  # 화면 가로의 랜덤 위치
        enemy_y_pos = -enemy_width

        # 이동 방향
        moveDir = 0
        # 캐릭터 속도
        character_speed = 0.5
        point_speed = 1
        enemy_speed = diff
        moveLeft = False
        moveRight = False

        # 시간 계산
        start_ticks = pygame.time.get_ticks()  # 시작 tick 받기
        # 게임 제한 시간
        total_time = 20

        score = 0
        running = True

        while True:
            # 제한 시간 동안 실행
            while running:
                dt = self.clock.tick(60)  # 60프레임

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quitGame()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            moveLeft = True
                        if event.key == pygame.K_RIGHT:
                            moveRight = True
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            moveLeft = False
                        if event.key == pygame.K_RIGHT:
                            moveRight = False

                if moveLeft: moveDir = -character_speed
                if moveRight: moveDir = character_speed
                if not moveLeft and not moveRight: moveDir = 0

                character_x_pos += moveDir * dt  # 좌우 이동

                # 오브젝트가 화면 밖으로 나가지 않도록
                if character_x_pos < 0:
                    character_x_pos = 0
                elif character_x_pos > self.screen_width - character_width:
                    character_x_pos = self.screen_width - character_width

                if point_y_pos > self.screen_height:
                    point_y_pos = -point_width
                    point_x_pos = random.randint(0, self.screen_width - point_width)

                if enemy_y_pos > self.screen_height:
                    enemy_y_pos = -enemy_width
                    enemy_x_pos = random.randint(0, self.screen_width - enemy_width)

                # rect정보 업데이트
                character_rect = character.get_rect()
                character_rect.left = character_x_pos
                character_rect.top = character_y_pos

                enemy_rect = enemy.get_rect()
                enemy_rect.left = enemy_x_pos
                enemy_rect.top = enemy_y_pos

                point_rect = point.get_rect()
                point_rect.left = point_x_pos
                point_rect.top = point_y_pos

                if point_rect.colliderect(enemy_rect):
                    if enemy_y_pos >= point_y_pos:
                        point_x_pos = random.randint(0, self.screen_width - point_width)
                    else:
                        enemy_y_pos = random.randint(0, self.screen_width - point_width)

                # 아이템 충돌, 점수
                if character_rect.colliderect(point_rect):
                    score += 1
                    point_y_pos = self.screen_height + 10
                if character_rect.colliderect(enemy_rect):
                    score -= 1 if score > 0 else 0
                    enemy_y_pos = self.screen_height + 10
                scoreTxt = self.game_font.render("점수: " + str(score), True, (0, 0, 0))

                point_y_pos += point_speed * dt  # 점수 아이템 하강
                enemy_y_pos += enemy_speed * dt  # 꽝 아이템 하강

                # 게임 시간 및 타이머
                elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # get_ticks() 단위: 밀리초
                timer = self.game_font.render(str(int(total_time - elapsed_time)), True, (0, 0, 0))  # 문자열, 안티엘리어싱 여부, 색상
                # 만약 시간이 0 이하면 게임 종료
                if total_time - elapsed_time <= 0:
                    running = False

                # 스크린 업데이트
                self.screen.blit(background, (0, 0))  # 배경 그리기
                self.screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
                self.screen.blit(point, (point_x_pos, point_y_pos))  # 점수 아이템 그리기
                self.screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 꽝 아이템 그리기
                self.screen.blit(timer, (10, 10))
                self.screen.blit(scoreTxt, (10, 50))
                pygame.display.update()  # 게임 화면 업데이트

            self.score = score
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), flags=pygame.HIDDEN)
            return


class ClickGame(MiniGame):
    def __init__(self):
        super().__init__()
        self.screen_width = 640
        self.screen_height = 360
        self.centerPos = [(self.screen_width / 2), (self.screen_height / 2)]

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), flags=pygame.HIDDEN)

    # 게임 실행할 때 호출해 줄 함수
    def set(self, know):
        self.setScore()
        diff = 0
        if know < 30:
            diff = 4
        elif 30 <= know < 70:
            diff = 7
        elif 70 <= know:
            diff = 10
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), flags=pygame.SHOWN)

        self.gamePlay(diff)

    def gamePlay(self, diff):
        score = 0
        btnCenterPos = [self.centerPos[0] - 50, self.centerPos[1] - 25]

        # 시간
        total_time = diff
        enlapsed_time = 0

        gaming = False
        timeOut = False

        timer = self.game_font.render(str(total_time), True, (0, 0, 0))
        while True:
            self.screen.fill((255, 255, 255))

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if btnCenterPos[0] + 100 > mouse[0] > btnCenterPos[0] and btnCenterPos[1] + 50 > mouse[1] > btnCenterPos[1] \
                    and not timeOut:  # 마우스가 버튼 위에 위치할 때
                self.screen.blit(images.clickGameBtn2, (btnCenterPos[0], btnCenterPos[1]))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and click:
                        if not gaming:
                            self.start_ticks = pygame.time.get_ticks()  # 시작 tick 받기
                            gaming = True
                        score += 1
            else:
                self.screen.blit(images.clickGameBtn1, (btnCenterPos[0], btnCenterPos[1]))
            if gaming and not timeOut:
                start_ticks = pygame.time.get_ticks()  # 시작 tick 받기
                enlapsed_time = (pygame.time.get_ticks() - self.start_ticks) / 1000 - 1
                if enlapsed_time > total_time:
                    timeOut = True
            if gaming and timeOut:
                self.score = score
                self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), flags=pygame.HIDDEN)
                return

            timer = self.game_font.render(str(int(total_time - enlapsed_time)), True, (0, 0, 0))
            scoreTxt = self.game_font.render('점수: ' + str(score), True, (0, 0, 0))

            self.screen.blit(timer, (10, 10))
            self.screen.blit(scoreTxt, (10, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()

            pygame.display.update()