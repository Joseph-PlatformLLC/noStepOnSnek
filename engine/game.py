import pygame
from . import snek, components

pygame.init()
pygame.display.set_caption("No step on Snek")

class GameInstance():
    def __init__(self):
        self.colors = components.Colors()
        self.window = components.Window()
        self.gameDisplay = pygame.display.set_mode(( self.window.width, self.window.height ))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 50)
        self.sneks = []
        self.states = components.States()
        self.food = []

    def loadSneks(self, num):
        a = True
        i = 0
        sectionsX = round((self.window.width - 25 / num)/25.0) * 25.0
        y = (self.window.height / 2) - 25

        while (i < num):
            i = i + 1
            x = sectionsX * i

            sneks.append(snek.Snek(x, y, a))
            a = False

    def loadFood(self, num):
        for i in range(num):
            self.food.append(components.Food())

    def endGame(self):
        pygame.quit()
        quit()

    def activateSnek(self, num):
        a = num - 1
        self.states.activeSnek = a

        for i in self.sneks:
            if i != a:
                i.active = False
            else:
                i.active = True

    def afterGameScreen(self):
        game_over = self.font.render("Game Over", True, self.colors.black)

        while not states.exit:
            for event in pygame.event.get():


            self.gameDisplay.fill(self.colors.red)
            self.gameDisplay.blit(self.game_over, [self.window["Width"] / 2, self.window["Height"] / 2])
            pygame.display.update()

    def gameRender(self):
        self.gameDisplay.fill(self.colors.white)
        i = 0
        for x in self.sneks:
            x.update('n')

        for x in self.food:
            pygame.draw.rect(self.gameDisplay, x.color, x.x, x.y, x.square_size, x.square_size)

        for i in self.sneks:
            for x in i.render():
                # rect -> x, y, width, height
                # pygame.draw.rect(self.gameDisplay, self.colors.red, [self.lead["x"], self.lead["y"], self.square_size, self.square_size])
                pygame.draw.rect(self.gameDisplay, x.color, x.x, x.y, x.square_size, x.square_size)

    def inGameLoop(self):
        self.loadSneks(self.states.level)
        self.loadFood(self.states.level)

        while self.states.inGame:

            for event in pygame.event.get():
                t = event.type

                if t == pygame.QUIT:
                    self.endGame()

                elif t == pygame.KEYDOWN:
                    k = event.key.name()

                    if k == pygame.K_1:
                        self.activateSnek(1)

                    elif k == pygame.K_2:
                        self.activateSnek(2)

                    elif k == pygame.K_3:
                        self.activateSnek(3)

                    elif k == pygame.K_4:
                        self.activateSnek(4)

                    elif k == pygame.K_5:
                        self.activateSnek(5)

                    else:
                        self.sneks[self.states.activeSnek].eventHandler(event)
                        
            self.gameRender()
            pygame.display.update()
            self.clock.tick(2)
