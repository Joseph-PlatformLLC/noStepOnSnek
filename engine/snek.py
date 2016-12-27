from . import components

class Snek():
    def __init__(self, x, y, active):
        self.colors = components.Colors()
        self.velocity = 25
        self.square_size = 25
        self.color = self.colors.black
        self.speed = components.Dot(0,0)
        self.head = components.Dot(x, y, self.color)
        self.body = []
        self.active = True
        self.directionX = True
        self.window = components.Window()
        self.directionX = True

    def update(self, code):
        if code == 'l' or code == 'r':
            self.head.x += self.speed.x

        elif code =='u' or code == 'd':
            self.head.y += self.speed.y

        elif code == 'n'
            if self.directionX:
                self.head.x += self.speed.x
            else:
                self.head.y += self.speed.y

        if self.active:
            self.color = self.colors.black
        else:
            self.color = self.colors.grey

        if code == 'none':
            print('Unassigned Key')

    def eventHandler(self, event):
        code = 'none'
        if event.key == pygame.K_LEFT:
            self.speed.x = -self.velocity
            self.directionX = True

        elif event.key == pygame.K_RIGHT:
            self.speed.x = self.velocity
            self.directionX = True

        elif event.key == pygame.K_DOWN:
            self.speed.y = self.velocity
            self.directionX = False

        elif event.key == pygame.K_UP:
            self.speed.y = -self.velocity
            self.directionX = False

    def grow(self, x, y):
        body.append(components.Dot(x, y))

    def render(self, display):
        r = [self.head]
        for dot in self.body:
            r.append((dot.x, dot.y))
        return r

    def collisionCheck(self)
