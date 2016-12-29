import random
import snek

class Dot():
    def __init__(self, x, y, color, rand=False):
        window = Window()
        self.square_size = 25
        if rand:
            self.x = random.randrange(0, window.width, self.square_size)
            self.y = random.randrange(0, window.height, self.square_size)
        else:
            self.x = x
            self.y = y
        self.color = color

class Window():
    def __init__(self):
        self.height = 600
        self.width = 800

class Food():
    def __init__(self):
        window = Window()
        snekx = snek.Snek(0,0,False)
        self.colors = Colors()
        self.color = self.colors.red
        self.size = snekx.square_size
        width = window.width - self.size
        height = window.height - self.size
        dot = Dot(random.randrange(0, width, self.size), random.randrange(0, height, self.size), self.color)
        self.x = dot.x
        self.y = dot.y
        self.powerup = False

class States():
    def __init__(self):
        self.startScreen = True
        self.inGame = True
        self.paused = False
        self.exit = False
        self.level = 1
        self.activeSnek = 0
        self.nextLevel = 5

class Colors():
    def __init__(self):
        self.red = (255,0,0)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.grey = (128, 131, 137)
