import random

class Dot():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.square_size = 25

class Window():
    def __init__(self):
        self.height = 600
        self.width = 800

class Food():
    def __init__(self):
        window = Window()
        snek = Snek()
        self.colors = Colors()
        self.color = colors.red
        self.size = snek.square_size
        width = window.width - self.size
        height = window.height - self.size
        dot = Dot(random.randrange(0, width, self.size), random.randrange(0, height, self.size))
        self.x = dot.x
        self.y = dot.y
        self.powerup = False

    def collisionCheck(self, sneks):
        for x in sneks:
            for i in x:
                


class States():
    def __init__(self):
        self.startScreen = True
        self.inGame = True
        self.paused = False
        self.exit = False
        self.level = 1
        self.activeSnek = 0

class Colors():
    def __init__(self):
        self.red = (255,0,0)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.grey = (128, 131, 137)
