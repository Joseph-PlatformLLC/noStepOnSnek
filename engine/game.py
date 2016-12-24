import pygame
from . import snek

pygame.init()

class GameInstance():
    def __init__(self):
        self.colors = {
            "Red": (255,0,0),
            "White": (255,255,255),
            "Black": (0,0,0)
            }
        self.window = {
            "Width": 800,
            "Height": 600,
            }
        self.gameDisplay = pygame.display.set_mode(( self.window["Width"], self.window["Height"] ))
        self.clock = pygame.time.Clock()
        self.inGame = "True"
        self.exitGame = "False"
        self.directionX = True
        self.font = pygame.font.SysFont(None, 50)
        self.sneks = []
        self.level = 1

    def loadSneks(self, num):
        i = 0
        x = 0
        y = 0
        while (i = num):
            sneks.append(Snek(x, y))

    def endGame(self):
        pygame.quit()
        quit()

    def afterGameScreen(self):
        game_over = self.font.render("Game Over", True, self.colors["Black"])

        while not self.exitGame:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                    gameExit = True

            self.gameDisplay.fill(self.colors["Red"])
            self.gameDisplay.blit(self.game_over, [self.window["Width"] / 2, self.window["Height"] / 2])
            pygame.display.update()

    def inGameLoop(self):
        while self.inGame:

            for event in pygame.event.get():
                self.gameDisplay.fill(self.colors["White"])
                # rect -> x, y, width, height
                pygame.draw.rect(self.gameDisplay, self.colors["Red"], [self.lead["x"], self.lead["y"], self.square_size, self.square_size])
                pygame.display.update()
                self.clock.tick(2)
