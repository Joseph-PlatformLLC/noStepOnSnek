import components
import pygame
class Snek():
    def __init__(self, x, y, active):
        self.colors = components.Colors()
        self.velocity = 25
        self.square_size = 25
        self.color = self.colors.black
        self.speed = components.Dot(self.velocity, 0, self.color)
        self.head = components.Dot(x, y, self.color)
        self.body = []
        self.active = True
        self.directionX = True
        self.window = components.Window()
        self.directionX = True

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

    # def grow(self):
    #     x = self.body
    #     if x:
    #         dx = x[len(x) - 1].x
    #         dy = x[len(x) - 1].y
    #         self.body.append(components.Dot(dx, dy, self.color))
    #     else:
    #         self.body.append(components.Dot(self.head.x, self.head.y, self.color))

    def render(self):
        r = [self.head]
        if self.body:
            for dot in self.body:
                r.append(dot)

        return r

    def collisionCheck(self, food):
        f = False
        for x in food:
            if (x.x == self.head.x) and (x.y == self.head.y):
                f = True
                break

        return f

    def bodyFollow(self, oldHead, grow=False):
        flag = True
        for dot in self.body:
            print dot.x, dot.y, dot.color
        if self.body:
            self.body.insert(0, components.Dot(oldHead.x, oldHead.y, oldHead.color))
            if not grow:
                x = self.body.pop()
                print x

        else:
            if grow:
                self.body.append(components.Dot(oldHead.x, oldHead.y, oldHead.color))

    def update(self, code, food):
        if code == 'n':
            c = self.collisionCheck(food)

            if c:
                self.bodyFollow(self.head, True)
            else:
                self.bodyFollow(self.head)

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
