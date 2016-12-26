from . import components

class Snek():
    def __init__(self, x, y, active):
        self.velocity = 25
        self.square_size = 25
        self.speed = components.Dot(0,0)
        self.head = components.Dot(x, y)
        self.body = []
        self.active = active
        self.directionX = True
        self.window = components.Window()
        self.directionX = True


    def returnHandler(self, code):
        r = {
            "code": code
            "head": self.head
            "body": self.body
            "active": self.active
            }
        return r

    def eventHandler(self, event):
        code = 'n'
        if event.key == pygame.K_LEFT:
            self.speed.x = -self.velocity
            self.directionX = True
            code = 'l'

        elif event.key == pygame.K_RIGHT:
            self.speed.x = self.velocity
            self.directionX = True
            code = 'r'

        elif event.key == pygame.K_DOWN:
            self.speed.y = self.velocity
            self.directionX = False
            code = 'd'

        elif event.key == pygame.K_UP:
            self.speed.y = -self.velocity
            self.directionX = False
            code = 'u'

        if self.directionX:
            self.head.x += self.speed.x

        else:
            self.head.y += self.speed.y

        if (self.head.x <= 0) or (self.head.x >= self.window.width) or (self.head.y <= 0) or (self.head.y >= self.window.height):
            code = 'q'

        return self.returnHandler(code)

    def grow(self, x, y):
        body.append(components.Dot(x, y))

    def render(self):
        r = [self.head]
        for components.Dot in self.body
