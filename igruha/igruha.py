#ИГРА
import pygame

pygame.init()
win = pygame.display.set_mode((1000, 800))

pygame.display.set_caption('igruha')

class map():
    pass

class player():
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

player1 = player(400, 725, 50, 60, 5)

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and player1.x > 5:
        player1.x -= player1.speed
    if keys[pygame.K_d] and player1.x < 1000 - player1.width - 5:
        player1.x += player1.speed
    if not(isJump):
        if keys[pygame.K_w]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                player1.y += (jumpCount ** 2) / 2
            else:
                player1.y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (player1.x, player1.y, player1.width, player1.height))
    pygame.display.update()

pygame.quit()