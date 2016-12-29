import pygame
import snek, components

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
        self.score = 0

    def loadSneks(self, num):
        a = True
        i = 0
        numx = num + 1
        sectionsX = round(((self.window.width - 25) / numx)/25.0) * 25.0
        y = (self.window.height / 2) - 25

        for s in range(num):
            x = sectionsX * i
            print sectionsX
            print x
            self.sneks.append(snek.Snek(x, y, a))
            a = False
            i = i + 1

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
            self.gameDisplay.fill(self.colors.red)
            self.gameDisplay.blit(game_over, [self.window["Width"] / 2, self.window["Height"] / 2])
            pygame.display.update()

    def gameRender(self):
        score_display = self.font.render('Score: '+ str(self.score), True, self.colors.black)
        self.gameDisplay.fill(self.colors.white)
        i = 0
        for x in self.sneks:
            r = x.update('n', self.food)
            print r
            if r[0]:
                self.food.pop(r[1])
                self.loadFood(1)
                self.score += 1

        for x in self.food:
            pygame.draw.rect(self.gameDisplay, x.color, [x.x, x.y, x.size, x.size])

        for i in self.sneks:
            for x in i.render():
                # rect -> x, y, width, height
                # pygame.draw.rect(self.gameDisplay, self.colors.red, [self.lead["x"], self.lead["y"], self.square_size, self.square_size])
                pygame.draw.rect(self.gameDisplay, x.color, [x.x, x.y, x.square_size, x.square_size])
        self.gameDisplay.blit(score_display, [self.window.width - 150, self.window.height - 50])

    def inGameLoop(self):
        self.loadSneks(self.states.level + 1)
        self.loadFood(self.states.level + 1)

        while self.states.inGame:
            for event in pygame.event.get():
                t = event.type

                if t == pygame.QUIT:
                    self.endGame()

                elif t == pygame.KEYDOWN:
                    k = event.key

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
