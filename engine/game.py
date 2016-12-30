import pygame
import snek, components, progress, render

pygame.init()
pygame.display.set_caption("No step on Snek")

class GameInstance():
    def __init__(self):
        self.colors = components.Colors()
        self.clock = pygame.time.Clock()
        self.progress = progress.ProgressHandler()
        self.score = 0
        self.render = render.RenderEngine()

    def loadSneks(self, num, first=False):
        a = first
        i = 0
        numx = num + 1
        sectionsX = round(((self.window.width - 25) / numx)/25.0) * 25.0
        y = (self.window.height / 2) - 25

        if first:
            for s in range(num):
                x = sectionsX * i
                self.progress.sneks.append(snek.Snek(x, y, a))
                a = False
                i = i + 1
        else:
            x = components.Dot(0,0,self.colors.black,True)
            self.progress.sneks.append(snek.Snek(x.x, x.y, False))

    def endGame(self):
        pygame.quit()
        quit()

    def afterGameScreen(self):
        game_over = self.font.render("Game Over", True, self.colors.black)

        while not states.exit:
            self.gameDisplay.fill(self.colors.red)
            self.gameDisplay.blit(game_over, [self.window["Width"] / 2, self.window["Height"] / 2])
            pygame.display.update()

    def eventHandler(self, event):
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
                self.progress.sneks[self.states.activeSnek].eventHandler(event)

    def inGameLoop(self):
        self.loadSneks(self.states.level, True)
        self.loadFood(self.states.level + 1)

        while self.states.inGame:
            for event in pygame.event.get():
                self.eventHandler(event)

            self.drawFrame()
            pygame.display.update()
            self.clock.tick(2)
