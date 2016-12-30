import pygame
import components

class RenderEngine():
    def __init__(self):
        self.colors = components.Colors()
        self.font = pygame.font.SysFont(None, 50)
        self.window = components.Window()
        self.gameDisplay = pygame.display.set_mode(( self.window.width, self.window.height ))


    def Text(self, text, color):
        x = self.font.render(text, True, color)
        y = x.get_rect()
        return x, y

    # def updateSneks(self, sneks):

    def renderOverlay(self, progress):
        offset = 15
        score_surface, score_rect = self.Text('Score: '+ str(progress.score), self.colors.grey)
        level_surface, level_rect = self.Text('Level: '+ str(progress.states.level), self.colors.grey)

        sr_width, sr_height = self.font.size('Score: '+str(progress.score))
        ls_width, ls_height = self.font.size('Level: '+str(progress.states.level))

        score_rect.center = ((sr_width / 2) + offset, self.window.height + (-sr_height /2) - offset)
        level_rect.center = ((self.window.width + (-ls_width / 2) - offset), (self.window.height + ((-ls_height / 2) - offset)))

        for i in range(0, len(progress.sneks)):
            if progress.sneks[i].active:
                color = self.colors.black
            else:
                color = self.colors.grey

            snek_display = self.font.render(str(i + 1), True, color)
            self.gameDisplay.blit(snek_display, [xoffset, 10])
            xoffset += 30

        self.gameDisplay.blit(score_surface, score_rect)
        self.gameDisplay.blit(level_surface, level_rect)
