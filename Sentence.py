def sentence(str1):
    import pygame, sys
    import random, math
    from pygame import mixer

    # Initialising pygame and setting up window
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("The Sentence!")
    #icon = pygame.image.load("assets\\target.png")
    #pygame.display.set_icon(icon)
    background = pygame.image.load("Assets\\sentence.png")
    clock = pygame.time.Clock()
    #mixer.music.load("assets\\textToSpeech.mp3")
    #mixer.music.play(1)



    textfont = pygame.font.Font("Assets\\telegrafico.ttf", 48)
    text = textfont.render(str1, True, (255, 255, 255))

    running = True
    while running:
        # screen.fill((255,255,255))
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.blit(text,(250,300))
        clock.tick(60)
        pygame.display.update()
