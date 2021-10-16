import pygame
from math import *

yellow = (244, 208, 63)
blue = (52, 152, 219)
red = (203, 67, 53)
purple = (136, 78, 160)
orange = (230, 126, 34)
green = (40, 180, 99)
brown = (102, 51, 0)

white = (236, 240, 241)
black = (23, 32, 42)
beige = (249, 231, 159)
dark_green = (0, 102, 0)
wood_brown = (100, 30, 22)

background = dark_green

RATE = 60

width = 800
height = 450
radius = height/40
margin = 50
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pool")
clock = pygame.time.Clock()

def project_vec(a, b):
    angle = a.angle_to(b) * pi / 180
    c = pygame.Vector2(b.x, b.y)
    c.scale_to_length(a.magnitude() * cos(angle))
    return c
