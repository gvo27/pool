from classes.utils import *

class CueStick:
    def __init__(self, color=beige):
        self.force = 0
        self.color = color
        self.on = True

    def update(self, focus):
        self.focus = focus
        self.mousepos = pygame.mouse.get_pos()

    def draw(self):
        if not self.on:
            return

        focus = self.focus.pos
        if focus == self.mousepos:
            focus *= .999

        stick = focus - self.mousepos
        stick.scale_to_length(100)

        offset = pygame.Vector2(stick.x, stick.y)
        offset.scale_to_length(radius + self.force * 6)

        pygame.draw.line(display, self.color, focus - offset, focus - stick - offset, width=10)

    def hit(self):
        if not self.on:
            return
        diff = self.focus.pos - self.mousepos
        diff.scale_to_length(1)
        self.focus.vel += self.force * diff
        self.force = 0

    def update_force(self, n):
        if not self.on:
            return
        self.force = min(self.force + n, 15)