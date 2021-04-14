import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))


rect(screen, (0, 255, 255), (0, 0, 600, 400)) #небо

rect(screen, (0, 128, 0), (0, 401, 600, 400)) #трава

rect(screen, (128, 128, 0), (0, 200, 600, 300))#забор (доски)

x1 = 0; y1 = 200 #штриховка забора (12-21)
x2 = 600; y2 = 500
N = 10
color = (255, 255, 255)
rect(screen, color, (x1, y1, x2 - x1, y2 - y1), 2)
h = (x2 - x1) // (N + 1)
x = x1 + h
for i in range(N):
    line(screen, color, (x, y1), (x, y2))
    x += h

#будка + цепь
polygon(screen, (235, 191, 0), [[350, 450], [350, 650], [500, 700], [550, 650], [550, 450], [450, 300], [400, 350]])
aalines(screen, (0, 0, 0), False, [[350, 450], [350, 650], [500, 700], [550, 650], [550, 450], [450, 300], [400, 350], [500, 500], [500, 700]])
aalines(screen, (0, 0, 0), False, [[400, 350], [350, 450], [500, 500], [550, 450]])
ellipse(screen, (0, 0, 0), (375, 500, 100, 150))
pi = 3.14
arc(screen, (255, 255, 0), (355, 610, 15, 30), 0, pi, 4)
arc(screen, (255, 255, 0), (355, 610, 15, 30), pi, 2*pi, 4)
arc(screen, (255, 255, 0), (357, 630, 15, 30), 0, pi, 4)
arc(screen, (255, 255, 0), (357, 630, 15, 30), pi, 2*pi, 4)
arc(screen, (255, 255, 0), (355, 650, 15, 30), 0, pi, 4)
arc(screen, (255, 255, 0), (355, 650, 15, 30), pi, 2*pi, 4)
arc(screen, (255, 255, 0), (345, 665, 30, 15), 0, pi, 4)
arc(screen, (255, 255, 0), (345, 665, 30, 15), pi, 2*pi, 4)
arc(screen, (255, 255, 0), (325, 663, 30, 15), 0, pi, 4)
arc(screen, (255, 255, 0), (325, 663, 30, 15), pi, 2*pi, 4)
arc(screen, (255, 255, 0), (305, 665, 30, 15), 0, pi, 4)
arc(screen, (255, 255, 0), (305, 665, 30, 15), pi, 2*pi, 4)
arc(screen, (255, 255, 0), (285, 663, 30, 15), 0, pi, 4)
arc(screen, (255, 255, 0), (285, 663, 30, 15), pi, 2*pi, 4)
arc(screen, (255, 255, 0), (265, 665, 30, 15), 0, pi, 4)
arc(screen, (255, 255, 0), (265, 665, 30, 15), pi, 2*pi, 4)


#собака-кусака
ellipse(screen, (153, 102, 0), (50, 580, 120, 70))
ellipse(screen, (153, 102, 0), (150, 590, 90, 45))
ellipse(screen, (153, 102, 0), (200, 600, 50, 50))
ellipse(screen, (153, 102, 0), (150, 580, 50, 50))
ellipse(screen, (153, 102, 0), (235, 620, 20, 50))
ellipse(screen, (153, 102, 0), (180, 600, 20, 50))
ellipse(screen, (153, 102, 0), (220, 665, 30, 10))
ellipse(screen, (153, 102, 0), (165, 645, 30, 10))
ellipse(screen, (153, 102, 0), (115, 625, 35, 70))
ellipse(screen, (153, 102, 0), (40, 600, 35, 70))
ellipse(screen, (153, 102, 0), (25, 665, 35, 15))
ellipse(screen, (153, 102, 0), (100, 690, 35, 15))
rect(screen, (153, 102, 0), (45, 545, 80, 80))
aalines(screen, (0, 0, 0), True, [[45, 545], [125, 545], [125, 625], [45, 625]])
ellipse(screen, (153, 102, 0), (30, 545, 20, 30))
arc(screen, (0, 0, 0), (30, 545, 20, 30), pi, 2*pi, 1)
arc(screen, (0, 0, 0), (30, 545, 20, 30), 0, pi, 1)
ellipse(screen, (153, 102, 0), (120, 545, 20, 30))
arc(screen, (0, 0, 0), (120, 545, 20, 30), pi, 2*pi, 1)
arc(screen, (0, 0, 0), (120, 545, 20, 30), 0, pi, 1)
ellipse(screen, (255, 255, 255), (100, 570, 20, 15))
arc(screen, (0, 0, 0), (100, 570, 20, 15), pi, 2*pi, 2)
arc(screen, (0, 0, 0), (100, 570, 20, 15), 0, pi, 2)
ellipse(screen, (255, 255, 255), (50, 570, 20, 15))
arc(screen, (0, 0, 0), (50, 570, 20, 15), pi, 2*pi, 2)
arc(screen, (0, 0, 0), (50, 570, 20, 15), 0, pi, 2)
ellipse(screen, (0, 0, 0), (55, 575, 5, 5))
ellipse(screen, (0, 0, 0), (110, 575, 5, 5))
arc(screen, (0, 0, 0), (65, 590, 40, 20), pi, 2*pi, 2)
polygon(screen, (255, 255, 255),  [[70,605], [70,615], [75, 610]])
polygon(screen, (255, 255, 255),  [[100,605], [100,615], [95, 610]])
aalines(screen, (0, 0, 0), True, [[70,605], [70,615], [75, 610]])
aalines(screen, (0, 0, 0), True, [[100,605], [100,615], [95, 610]])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True