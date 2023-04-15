import pygame, sys
import random
from Test import wordtest
from Sentence import sentence
from Phrase import phrasetest

pygame.init()
screen = pygame.display.set_mode((800, 600))
#icon = pygame.image.load("Assets\\SignSense.jpeg")


def mainmenu():
    image = pygame.image.load("Assets\\sign.png")
    image2 = pygame.image.load("Assets\\phrase.png")
    imageold = image
    image2old = image2
    background = pygame.image.load("assets\\SignSense.png")
    font = pygame.font.Font("freesansbold.ttf", 24)
    pygame.display.set_caption("Sign Sense")
    click = False
    button1 = pygame.Rect(450, 250, 200, 75)
    str1 = ""
    button2 = pygame.Rect(450, 450, 200, 75)
    while True:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        mx, my = pygame.mouse.get_pos()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button1.collidepoint((mx, my)):
            imagenew = pygame.transform.scale(image, (215, 90))
            image = imagenew
            if click:
                str1 = wordtest()
                sentence(str1)


        if button2.collidepoint((mx, my)):
            image2new = pygame.transform.scale(image2, (215, 90))
            image2 = image2new

            if click:
                str1 = phrasetest.phrase()
                sentence(str1)


        screen.blit(image, button1)
        screen.blit(image2, button2)
        #screen.blit(image3, button3)
        image = imageold
        image2 = image2old
        #image3 = image3old

        # pygame.draw.rect(screen, (255,255,255), button1)
        # pygame.draw.rect(screen, (255, 255, 255), button2)
        # pygame.draw.rect(screen, (255, 255, 255), button3)




        pygame.display.update()


mainmenu()