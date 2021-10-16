from classes.utils import *
import numpy as np
import random

class Ball:

    radius = radius

    def __init__(self, pos, color, striped, swappable=True):
        self.color = color
        self.striped = striped

        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(0, 0)
        self.swappable = swappable

        self.r = self.radius
        self.on = True
        
    def swap(self, b2):
        if self.swappable and b2.swappable:
            self.pos, b2.pos = b2.pos, self.pos

    def update(self):
        if self.vel.magnitude() < .1:
            self.vel *= 0
        self.pos += self.vel
        
    def draw(self):
        pygame.draw.circle(display, self.color, self.pos, self.r)
        if self.striped:
            pygame.draw.circle(display, white, self.pos, self.r/2)
    
    def collision(self, s2):
        if self == s2:
            return
        if self.vel.magnitude() < s2.vel.magnitude():
            b1, b2 = s2, self
        else:
            b1, b2 = self, s2

        diff = b1.pos - b2.pos 
        if diff.magnitude() != 0 and diff.magnitude() <= b1.r + b2.r:

            offset = pygame.Vector2(diff.x, diff.y)
            offset.scale_to_length(b1.r + b2.r)
            b1.pos += offset - diff

            diff.scale_to_length(1)

            dtan = offset.rotate(90)
            dtan.scale_to_length(1)
            
            v1_rad = project_vec(b1.vel, diff)
            v1_tan = project_vec(b1.vel, dtan)
            v2_rad = project_vec(b2.vel, -diff)
            v2_tan = project_vec(b2.vel, dtan)
            
            b1.vel = v2_rad + v1_tan
            b2.vel = v1_rad + v2_tan

class Rack():
    
    def __init__(self):

        self.cueBall = Ball([width * .75 - margin, height/2], white, False, False)
        self.ball_array = [self.cueBall]

        color_iter = iter(self.get_color_iter())
        pos_iter = iter(self.get_pos_iter())

        for _ in range(15):
            pos, isEight = next(pos_iter)
            if isEight:
                color = black
                isStriped = True
            else:
                color, isStriped = next(color_iter)
            b = Ball(pos, color, isStriped, not isEight)
            self.ball_array.append(b)

        for b1 in self.ball_array:
            for b2 in self.ball_array:
                if random.randint(0,1):
                    b1.swap(b2)
    
    def get_pos_iter(self):

        class Pos_Iter:

            x_front = (width/2 + margin)/2
            y_center = height/2
            num_rows = 5

            def __iter__(self):
                self.i = 0
                self.ball_pos = self.rack_pos(self.x_front, self.y_center, self.num_rows, Ball.radius)
                return self

            def __next__(self):
                isEight = self.i == 4
                if self.i == len(self.ball_pos):
                    self.i = self.i % len(self.ball_pos)
                p = self.ball_pos[self.i]
                self.i += 1
                return p, isEight

            def rack_pos(self, x_front, y_center, num_rows, obj_radius):
                def xPos(row_n):
                    return x_front + sqrt(3)*row_n*obj_radius

                def yPos(num_obj):
                    uncentered_y_vals = [2 * i * obj_radius for i in range(1, num_obj + 1)]
                    return np.array(uncentered_y_vals) + (y_center - np.mean(uncentered_y_vals))

                result = []
                for i in range(1, num_rows + 1):
                    result += [[xPos(-i), y] for y in yPos(i)]
                return result
        
        return Pos_Iter()
    
    def get_color_iter(self):

        class Color_Iter:

            colors = [yellow, blue, red, purple, orange, green, brown]
            
            def __iter__(self):
                self.i = 0
                self.striped = True
                return self

            def __next__(self):
                if self.i == len(self.colors):
                    self.striped = not self.striped
                    self.i = self.i % len(self.colors)
                c = self.colors[self.i]
                self.i += 1
                return c, self.striped
        
        return Color_Iter()