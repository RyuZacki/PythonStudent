
import pygame
from Player import Player
from Platforms1 import GameObject

SIZE = (640, 480)

pygame.display.set_caption('Cubes Game')

playerStand = pygame.image.load('anim/idle.png')

walkRight = [pygame.image.load('anim/right_1.png'),
pygame.image.load('anim/right_2.png'), pygame.image.load('anim/right_3.png'),
pygame.image.load('anim/right_4.png'), pygame.image.load('anim/right_5.png'),
pygame.image.load('anim/right_6.png')]

walkLeft = [pygame.image.load('anim/left_1.png'),
pygame.image.load('anim/left_2.png'), pygame.image.load('anim/left_3.png'),
pygame.image.load('anim/left_4.png'), pygame.image.load('anim/left_5.png'),
pygame.image.load('anim/left_6.png')]

window = pygame.display.set_mode(SIZE)
screen = pygame.Surface(SIZE)

x1 = 55
y1 = 430

hero = Player(x1, y1, playerStand)

left = False
right = False
up = False

level = [
 '000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
 '0                                                                                              0',
 '0                                                                                              0',
 '0                                                                                        -------',
 '0                                                                                   -----=======',
 '0                                                                                  -============',
 '0                                                                                  =============',
 '0                                                                                 -=============',
 '0                                                                              ---==============',
 '0                                                                             -=================',
 '0                                                                             ==================',
 '0                                                                            -==================',
 '0                                                                         ---===================',
 '0                                                                   ------======================',
 '0                                    ---------                  ----============================',
 '0                        ------------=========--              --================================',
 '-------------------------=======================--------------==================================',
 '================================================================================================',
    ]

sprite_group = pygame.sprite.Group()
sprite_group.add(hero)
objects = []

x = 0
y = 0
for row in level:
    for col in row:
        if col == '-':
            obj = GameObject(x, y, 'objects/Trava.png')
            sprite_group.add(obj)
            objects.append(obj)
        elif col == '=':
            obj = GameObject(x, y, 'objects/Graz.png')
            sprite_group.add(obj)
            objects.append(obj)
        elif col == '0':
            obj = GameObject(x, y, 'objects/Nebo.png')
            sprite_group.add(obj)
            objects.append(obj)
        x += 40
    y += 40
    x = 0

class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_func(camera, target_rect):
    l = -target_rect.x + SIZE[0]/2
    t = -target_rect.y + SIZE[1]/2
    w, h = camera.width, camera.height

    l = min(0, l)
    l = max(-(camera.width-SIZE[0]), l)
    t = max(-(camera.height-SIZE[1]), t)
    t = min(0, t)

    return pygame.Rect(l, t, w, h)

#hero = Player(55, 430, playerStand)
total_level_width = len(level[0]) * 40
total_level_height = len(level) * 40

camera = Camera(camera_func, total_level_width, total_level_height)

done = True
timer = pygame.time.Clock()
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                left = True
            if e.key == pygame.K_RIGHT:
                right = True
            if e.key == pygame.K_UP:
                up = True


        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                left = False
            if e.key == pygame.K_RIGHT:
                right = False
            if e.key == pygame.K_UP:
                up = False

    screen.fill((0, 255, 255))

    hero.update(left, right, up, objects)
    camera.update(hero)
    for e in sprite_group:
        screen.blit(e.image, camera.apply(e))

    pygame.display.flip()
    timer.tick(60)

    window.blit(screen, (0, 0))
