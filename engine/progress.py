import components

class ProgressHandler():
    def __init__(self):
        self.states = components.States()
        self.score = 0
        self.sneks = []
        self.food = []
        self.window = components.Window()

    def score(self):
        self.score += 1

    def update(self):
        if self.score > self.states.nextLevel:
            self.states.level += 1
            self.states.nextLevel += 55
            self.loadSneks(1)

    def activateSnek(self, num):
        a = num - 1
        self.states.activeSnek = a

        for i in self.sneks:
            if i != a:
                i.active = False
            else:
                i.active = True

    def loadFood(self, num):
        for i in range(num):
            self.food.append(components.Food())

    def loadSneks(self, num, first=False):
        a = first
        i = 0
        numx = num + 1
        sectionsX = round(((self.window.width - 25) / numx)/25.0) * 25.0
        y = (self.window.height / 2) - 25

        if first:
            for s in range(num):
                x = sectionsX * i
                self.progress.sneks.append(snek.Snek(x, y, a))
                a = False
                i = i + 1
        else:
            x = components.Dot(0,0,self.colors.black,True)
            self.progress.sneks.append(snek.Snek(x.x, x.y, False))
