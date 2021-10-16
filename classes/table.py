from classes.utils import *

class Walls:
    def __init__(self, color=wood_brown):
        self.color = color
        self.top = pygame.Rect(0, 0, width, margin)
        self.left = pygame.Rect(0, 0, margin, height)
        self.right = pygame.Rect(width-margin, 0, margin, height)
        self.bottom = pygame.Rect(0, height-margin, width, margin)
    
    def draw(self):
        pygame.draw.rect(display, self.color, self.top)
        pygame.draw.rect(display, self.color, self.left)
        pygame.draw.rect(display, self.color, self.right)
        pygame.draw.rect(display, self.color, self.bottom)

    def collision(self, ball):
        if self.top.collidepoint(ball.pos.x, ball.pos.y - ball.r):
            ball.pos.y += abs(ball.pos.y - ball.r - margin)
            ball.vel.y *= -1
        if self.left.collidepoint(ball.pos.x - ball.r, ball.pos.y):
            ball.pos.x += abs(ball.pos.x - ball.r - margin)
            ball.vel.x *= -1
        if self.right.collidepoint(ball.pos.x + ball.r, ball.pos.y):
            ball.pos.x -= abs(ball.pos.x + ball.r + margin - width)
            ball.vel.x *= -1
        if self.bottom.collidepoint(ball.pos.x, ball.pos.y + ball.r):
            ball.pos.y -= abs(ball.pos.y + ball.r + margin - height)
            ball.vel.y *= -1

class Pocket:
    def __init__(self, x, y, color=black):
        self.pos = pygame.Vector2(x, y)
        self.r = radius*1.5
        self.margin = self.r/2
        self.color = color

    def draw(self):
        pygame.draw.circle(display, self.color, self.pos, self.r)

    def collision(self, ball):
        if ball.swappable:  
            if self.pos.distance_to(ball.pos) < ball.r + self.margin:
                ball.on = False

