#Изучение pygame

import pygame

pygame.init()
size = (600, 400)
screen = pygame.display.set_mode(size) # <-- Создание окна
pygame.display.set_caption('Моя программа') # <-- Название окна
'''img = pygame.image.load('Proga.png') # <-- Загружаем в переменную картинку
pygame.display.set_icon(img) # <-- Ставим иконку программы'''

font = pygame.font.SysFont('comicsansms', 32)# <-- Создание шрифта

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

follow = font.render("Ги ги га га ", 1, RED, GREEN) # <-- Создание текста (1 - Текст, 2 - сглаживание, 3 - цвет, 4 - фон)
like = font.render("Ги ги га га 22 ", 1, GREEN, BLUE)
width, height = like.get_size()

FPS = 120
x, y = 0, 300
direct_x = 1
direct_y = 1
clock = pygame.time.Clock()
while True: # <-- Цикл обработки событий
    for even in pygame.event.get(): # <-- В этом цикле мы перехватываем все событий
        if even.type == pygame.QUIT:
            quit()

        clock.tick(FPS)
        screen.fill(BLACK)
        screen.blit(follow, (0, 0)) # <-- Отображение текста
        screen.blit(like, (x, y))

        x += direct_x
        if x + width>= 600 or x < 0:
            direct_x = -direct_x

        y += direct_y
        if y + height >= 400 or y < 0:
            direct_y = -direct_y

        pygame.display.update()