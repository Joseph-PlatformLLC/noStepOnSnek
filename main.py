import pygame
windowWidth = 800
windowHeight = 600

pygame.init()
gameDisplay = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()
pygame.display.set_caption("No step on Snek")
pygame.display.update()



def afterGameScreen():
    windowWidth = 800
    windowHeight = 600
    white = (255, 255, 255)
    black = (0,0,0)
    red = (255,0,0)
    gameExit = False
    font = pygame.font.SysFont(None, 50)
    game_over = font.render("Game Over", True, black)

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                gameExit = True

        gameDisplay.fill(red)
        gameDisplay.blit(game_over, [windowWidth / 2, windowHeight / 2])
        pygame.display.update()



def inGameLoop():
    windowWidth = 800
    windowHeight = 600
    white = (255, 255, 255)
    black = (0,0,0)
    red = (255,0,0)
    backgroundColor = white
    inGame = True
    leadX = 300
    leadY = 300
    leadXSpeed = 0
    leadYSpeed = 0
    #Move across x on true, and y on false
    direction = True
    speed = 25
    square_size = 25
    while inGame:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                inGame = True

            elif event.type == pygame.KEYDOWN:
                if (inGame == False):
                    gameExit = True
                elif event.key == pygame.K_LEFT:
                    leadXSpeed = -speed
                    direction = True
                elif event.key == pygame.K_RIGHT:
                    leadXSpeed = speed
                    direction = True
                elif event.key == pygame.K_DOWN:
                    leadYSpeed = speed
                    direction = False
                elif event.key == pygame.K_UP:
                    leadYSpeed = -speed
                    direction = False



        if direction:
            leadX += leadXSpeed
        elif (direction == False):
            leadY += leadYSpeed
        if (leadX <= 0) or (leadX >= windowWidth) or (leadY <= 0) or (leadY >= windowHeight):
            backgroundColor = red
            inGame = False

        gameDisplay.fill(backgroundColor)
        # rect -> x, y, width, height

        pygame.draw.rect(gameDisplay, red, [leadX, leadY, square_size, square_size])
        pygame.display.update()

        clock.tick(2)


inGameLoop()
afterGameScreen()
pygame.quit()
quit()
