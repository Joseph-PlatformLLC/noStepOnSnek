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

    def renderText(self, text, color):
        x = self.font.render(text, True, color)
        y = x.get_rect()
        return x, y

    def renderOverlay(self):
        score_surface, score_rect = self.renderText('Score: '+ str(self.score), self.colors.grey)
        sr_width, sr_height = self.font.size('Score: '+str(self.score))
        level_surface, level_rect = self.renderText('Level: '+ str(self.states.level), self.colors.grey)
        ls_width, ls_height = self.font.size('Level: '+str(self.states.level))
        offset = 15
        score_rect.center = ((sr_width / 2) + offset, self.window.height + (-sr_height /2) - offset)
        level_rect.center = ((self.window.width + (-ls_width / 2) - offset), (self.window.height + ((-ls_height / 2) - offset)))

        for i in range(0, len(self.sneks)):
            if self.sneks[i].active:
                color = self.colors.black
            else:
                color = self.colors.grey

            snek_display = self.font.render(str(i + 1), True, color)
            self.gameDisplay.blit(snek_display, [xoffset, 10])
            xoffset += 30

        self.gameDisplay.blit(score_surface, score_rect)
        self.gameDisplay.blit(level_surface, level_rect)

    def loadSneks(self, num, first=False):
        a = first
        i = 0
        numx = num + 1
        sectionsX = round(((self.window.width - 25) / numx)/25.0) * 25.0
        y = (self.window.height / 2) - 25

        if first:
            for s in range(num):
                x = sectionsX * i
                self.sneks.append(snek.Snek(x, y, a))
                a = False
                i = i + 1
        else:
            x = components.Dot(0,0,self.colors.black,True)
            self.sneks.append(snek.Snek(x.x, x.y, False))

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

    def drawFrame(self):
        i = 0
        self.gameDisplay.fill(self.colors.white)

        for x in self.sneks:
            r = x.update('n', self.food)
            # print r
            if r[0]:
                self.food.pop(r[1])
                self.loadFood(1)
                self.progressHandler('score')

        for x in self.food:
            pygame.draw.rect(self.gameDisplay, x.color, [x.x, x.y, x.size, x.size])

        for i in self.sneks:
            for x in i.render():
                # rect -> x, y, width, height
                pygame.draw.rect(self.gameDisplay, x.color, [x.x, x.y, x.square_size, x.square_size])

        self.renderOverlay()

    def progressHandler(self, code):
        if code == 'score':
            self.score += 1

        if self.score > self.states.nextLevel:
            self.states.level += 1
            self.states.nextLevel += 55
            self.loadSneks(1)

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
                self.sneks[self.states.activeSnek].eventHandler(event)

    def inGameLoop(self):
        self.loadSneks(self.states.level, True)
        self.loadFood(self.states.level + 1)

        while self.states.inGame:
            for event in pygame.event.get():
                self.eventHandler(event)

            self.drawFrame()
            pygame.display.update()
            self.clock.tick(2)
