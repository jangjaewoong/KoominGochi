import pygame
import sys

fileLocation = "images/"

avoidBtn1 = pygame.image.load(fileLocation + "avoid1.png")
avoidBtn2 = pygame.image.load(fileLocation + "avoid2.png")
clickBtn1 = pygame.image.load(fileLocation + "click1.png")
clickBtn2 = pygame.image.load(fileLocation + "click2.png")

clickGameBtn1 = pygame.image.load(fileLocation + "clickGameBtn1.png")
clickGameBtn2 = pygame.image.load(fileLocation + "clickGameBtn2.png")

clearImg1 = pygame.image.load(fileLocation + "clear1.png")
clearImg2 = pygame.image.load(fileLocation + "clear2.png")
failImg1 = pygame.image.load(fileLocation + "fail1.png")
failImg2 = pygame.image.load(fileLocation + "fail2.png")

bgImg = pygame.image.load(fileLocation + "kookminUniv.png")

playerImg = pygame.image.load(fileLocation + "koominRun.png")
Aobj = pygame.image.load(fileLocation + "Aobj.png")
Fobj = pygame.image.load(fileLocation + "Fobj.png")