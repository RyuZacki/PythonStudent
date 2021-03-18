import pygame
from setting import *
from player import Player
import math
from map import world_map

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT)) # Создаём окно
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Проверка на выключение
            exit()

    player.movement()
    sc.fill(BLACK) # Делаем чёрный экран

    pygame.draw.circle(sc, GREEN, player.pos, 12)
    pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
                                             player.y + WIDTH * math.sin(player.angle)))
    for x,y in world_map:
        pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), 2)

    pygame.display.flip() # Обновляем экран на каждой этерации
    clock.tick(FPS)