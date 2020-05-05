import pygame
import random

pygame.init()

display_width = 500
display_height = 500

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Collision check')

clock = pygame.time.Clock()

colorBlue = (18, 45, 166)
colorGreen = (30, 166, 18)
colorRed = (245, 81, 66)

font_type = pygame.font.Font(pygame.font.get_default_font(), 32)

class Rect:
    def __init__(self, x, y, w, h, color, name):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.name = name


def create_rect(color, name):
    x = random.randrange(0, display_width - 10)
    y = random.randrange(0, display_height - 10)
    w = random.randrange(0, display_width - x)
    h = random.randrange(0, display_height - y)

    return Rect(x, y, w, h, color, name)


rect1 = create_rect(colorRed, 'R')
rect2 = create_rect(colorGreen, 'G')
rect3 = create_rect(colorBlue, 'B')

rects = [rect1, rect2, rect3]


def collision(a: Rect, b: Rect):
    xa1 = a.x
    xa2 = a.x + a.w
    ya1 = a.y
    ya2 = a.y + a.h

    xb1 = b.x
    xb2 = b.x + b.w
    yb1 = b.y
    yb2 = b.y + b.h

    res = xa2 >= xb1 and xa1 <= xb2 and ya2 >= yb1 and ya1 <= yb2

    print(a.name + ' AND ' + b.name + ' = ' + str(res))


for i in rects:
     for j in rects:
         if i.name != j.name:
            collision(i, j)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    for i in rects:
        pygame.draw.rect(display, i.color, (i.x, i.y, i.w, i.h), 4)
        display.blit(font_type.render(i.name, True, (0, 0, 0)), (i.x + 5, i.y + 5))

    pygame.display.update()

    clock.tick(80)