import pygame, random, sys
from pygame.locals import *

def collide(x1, x2, y1, y2, w1, w2, h1, h2):
    if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:
        return True
    else:
        return False

def lose(screen, points):
    f=pygame.font.SysFont('Arial', 30)
    t=f.render('Points: '+str(points), True, (0, 0, 0))
    screen.blit(t, (10, 270))
    pygame.display.update()
    pygame.time.wait(2000)
    sys.exit(0)
 
a = [290, 290, 290, 290, 290]
b = [290, 270, 250, 230, 210]
z = 0
points = 0
applepos = (random.randint(0, 590), random.randint(0, 590))
pygame.init()
s=pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')
appleimage = pygame.Surface((10, 10))
appleimage.fill((0, 255, 0))
img = pygame.Surface((20, 20))
img.fill((255, 0, 0))
f = pygame.font.SysFont('Arial', 20)
clock = pygame.time.Clock()

while True:
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit(0)
        elif e.type == KEYDOWN:
            if e.key == K_UP and z != 0:
                   z = 2
            elif e.key == K_DOWN and z != 2:
                   z = 0
            elif e.key == K_LEFT and z != 1:
                   z = 3
            elif e.key == K_RIGHT and z != 3:
                   z = 1
    i = len(a)-1
    while i >= 2:
        if collide(a[0], a[i], b[0], b[i], 20, 20, 20, 20):
              lose(s, points)
        i-= 1
    if collide(a[0], applepos[0], b[0], applepos[1], 20, 10, 20, 10):
        points+=1
        a.append(700)
        b.append(700)
        applepos=(random.randint(0,590),random.randint(0,590))
  
    if a[0] < 0 or a[0] > 580 or b[0] < 0 or b[0] > 580:
         lose(s, points)
    i = len(a)-1
 
    while i >= 1:
        a[i] = a[i-1]
        b[i] = b[i-1]
        i -= 1
    if z==0:
        b[0] += 20
    elif z==1:
        a[0] += 20
    elif z==2:
        b[0] -= 20
    elif z==3:
        a[0] -= 20	
    s.fill((255, 255, 255))	
 
    for i in range(0, len(a)):
        s.blit(img, (a[i], b[i]))
    s.blit(appleimage, applepos)
    t=f.render(str(points), True, (0, 0, 0))
    s.blit(t, (10, 10))
    pygame.display.update()