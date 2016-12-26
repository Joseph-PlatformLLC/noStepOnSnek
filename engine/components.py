import random

class Dot():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Window():
    def __init__(self):
        self.height = 600
        self.width = 800

class Food():
    def __init__(self, width, height, square_size):
        self.location = Dot(random.randrange(0, self.screen_width, self.square_size), random.randrange(0, self.screen_height, self.square_size))
        self.powerup = False
        self.screen_width = x - square_size
        self.screen_height = y - square_size

class States():
    def __init__(self):
        self.startScreen = "True"
        self.inGame = "True"
        self.paused = "false"
        self.exit = "False"
        self.level = 1
        self.activeSnek = 0ac
