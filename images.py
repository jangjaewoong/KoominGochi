import pygame
import sys

fileLocation = "images/"

avoidBtn1 = pygame.image.load(fileLocation + "avoid1.png")
avoidBtn2 = pygame.image.load(fileLocation + "avoid2.png")
clickBtn1 = pygame.image.load(fileLocation + "click1.png")
clickBtn2 = pygame.image.load(fileLocation + "click2.png")

clickGameBtn1 = pygame.image.load(fileLocation + "clickBtn1.png")
clickGameBtn2 = pygame.image.load(fileLocation + "clickBtn2.png")

clearImg1 = pygame.image.load(fileLocation + "clear1.png")
clearImg2 = pygame.image.load(fileLocation + "clear2.png")
failImg1 = pygame.image.load(fileLocation + "fail1.png")
failImg2 = pygame.image.load(fileLocation + "fail2.png")

bgImg = pygame.image.load(fileLocation + "bg.png")

playerImg = pygame.image.load(fileLocation + "player.png")
enemyImg = pygame.image.load(fileLocation + "dung.png")
heartImg = pygame.image.load(fileLocation + "heart.png")


if __name__ == '__main__':
    pygame.init()
    screen_width = 480
    screen_height = 640
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    clock.tick(60)


    class Button:
        def __init__(self, img_in, img_act, x, y, width, height):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()[0]
            if x + width > mouse[0] > x and y + height > mouse[1] > y:
                screen.blit(img_act, (x, y))
                if pygame.event.poll().type == pygame.MOUSEBUTTONDOWN:
                    print('hello')
            else:
                screen.blit(img_in, (x, y))


    while True:
        avoidGameBtn = Button(avoidBtn1, avoidBtn2, 240 - 50, 320 - 100,
                              100, 50)
        clickGameBtn = Button(clickBtn1, clickBtn2, 240 - 50, 320 + 50,
                              100, 50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
