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

    def grow(self):
        x = self.body
        if x:
            dx = x[len(x) - 1].x
            dy = x[len(x) - 1].y
            self.body.append(components.Dot(dx, dy, self.color))

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
                self.grow()
                f = True
                break

        return f

    def bodyFollow(self, oldHead, grow=False):
        flag = True
        temp1 = None
        temp2 = None

        if self.body:
            temp3 = self.body[len(self.body) - 1]
            for d in self.body:

                if flag:
                    temp1 = d
                    d.x = oldHead.x
                    d.y = oldHead.y
                    flag = False

                else:
                    temp1 = d
                    d.x = temp2.x
                    d.y = temp2.y

                temp2 = temp1

            if grow:
                self.body[len(self.body)-1] = temp3

        else:
            if grow:
                print len(self.body)
                self.body.append(oldHead)
