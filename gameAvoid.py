import pygame
import sys
import random
import images


"""
***수정할 것***
1. 똥과 하트가 서로 겹쳐서 나오는 문제
2. 오브젝트 수량 증가. 한 번에 여러 개가 내려오도록 (스크래치, 엔트리의 도장 찍기, 유니티의 오브젝트 풀)
"""


class AvoidGame():
    def __init__(self):
        self.screen_width = 480
        self.screen_height = 640
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.Font("NanumBarunGothic.ttf", 20)  # 폰트 객체 생성 (폰트(디폴트 값), 크기)
        self.centerPos = [(self.screen_width / 2), (self.screen_height / 2)]
        self.score = 0

    def quitGame(self):
        pygame.quit()
        sys.exit()

    def setScore(self):
        self.score = 0

    def gamePlay(self):
        # 캐릭터, 배경 불러오기
        background = images.bgImg

        character = images.playerImg
        character_width = character.get_rect().size[0]  # 가로 크기
        character_height = character.get_rect().size[1]  # 세로 크기
        character_x_pos = self.centerPos[0] - character_width / 2  # 화면 가로의 가운데 위치
        character_y_pos = self.screen_height - character_height  # 화면 세로 크기 가장 아래

        # 점수 아이템 불러오기
        point = images.heartImg
        point_width = point.get_rect().size[0]  # 가로 크기
        point_x_pos = random.randint(0, self.screen_width - point_width)  # 화면 가로의 랜덤 위치
        point_y_pos = self.screen_height + 1

        # 꽝 아이템 불러오기
        enemy = images.enemyImg
        enemy_width = enemy.get_rect().size[0]  # 가로 크기
        enemy_x_pos = random.randint(0, self.screen_width - enemy_width)  # 화면 가로의 랜덤 위치
        enemy_y_pos = self.screen_height + 1

        # 이동 방향
        moveDir = 0
        # 캐릭터 속도
        character_speed = 0.5

        # 시간 계산
        start_ticks = pygame.time.get_ticks()  # 시작 tick 받기
        # 게임 제한 시간
        total_time = 10

        score = 0
        running = True

        while True:
            # 제한 시간 동안 실행
            while running:
                dt = self.clock.tick(60)  # 60프레임

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quitGame()
                    if event.type == pygame.KEYDOWN:  # 키 입력
                        if event.key == pygame.K_LEFT:
                            moveDir = -character_speed
                        elif event.key == pygame.K_RIGHT:
                            moveDir = character_speed
                    elif event.type == pygame.KEYUP:  # 키 입력 종료
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                            moveDir = 0

                character_x_pos += moveDir * dt  # 좌우 이동

                point_y_pos += 0.5 * dt  # 점수 아이템 하강
                enemy_y_pos += 0.5 * dt  # 꽝 아이템 하강

                # 캐릭터가 화면 밖으로 나가지 않도록
                if character_x_pos < 0:
                    character_x_pos = 0
                elif character_x_pos > self.screen_width - character_width:
                    character_x_pos = self.screen_width - character_width

                if point_y_pos > self.screen_height:
                    point_y_pos = 0
                    point_x_pos = random.randint(0, self.screen_width - point_width)

                if enemy_y_pos > self.screen_height:
                    enemy_y_pos = 0
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

                # 아이템 충돌, 점수
                if character_rect.colliderect(point_rect):
                    score += 1
                    point_y_pos = self.screen_height + 1
                if character_rect.colliderect(enemy_rect):
                    score -= 1 if score > 0 else 0
                    enemy_y_pos = self.screen_height + 1
                scoreTxt = self.game_font.render("점수: " + str(score), True, (0, 0, 0))

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

            if score > self.score:
                self.score = score
            return


if __name__ == "__main__":
    game = AvoidGame()
    game.gamePlay()
