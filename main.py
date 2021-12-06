import pygame
import random
pygame.init()

W = 1500
H = 1000
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Eat Game')
pygame.display.set_icon(pygame.image.load('Images/hstand.png'))

hdown = pygame.image.load('Images/hdown.png')
hdownleft = pygame.image.load('Images/hdownleft.png')
hdownright = pygame.image.load('Images/hdownright.png')
hleft = pygame.image.load('Images/hleft.png')
hleftup = pygame.image.load('Images/hleftup.png')
hright = pygame.image.load('Images/hright.png')
hup = pygame.image.load('Images/hup.png')
hupright = pygame.image.load('Images/hupright.png')
hstand = pygame.image.load('Images/hstand.png')
food = pygame.image.load('Images/Apple.png')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
hx = W//2
hy = H//2


def cordgen():
    x = random.randint(100, W-100), random.randint(200, H-100)
    return x


FPS = 90
clock = pygame.time.Clock()

appcord = cordgen()
mleft = 0
mright = 0
mup = 0
mdown = 0
speed = 1.5
score = 0
apple = 0
scmult = 10

apple = pygame.Surface((40, 40))
hero = pygame.Surface((75, 75))
hero.blit(hstand, (0, 0))
apple.blit(food, (0, 0))
hrect = hero.get_rect(center=(W//2, H//2))
arect = hero.get_rect(center=appcord)

while True:
    keys = pygame.key.get_pressed()
    hrect = hero.get_rect(center=(hx, hy))
    hrectdownlx, hrectdownly = hrect.bottomleft
    hrectuprx, hrectupry = hrect.topright
    arect = apple.get_rect(center=appcord)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if keys[pygame.K_LEFT]:
        mleft = True
        mup = mdown = mright = False
    if keys[pygame.K_RIGHT]:
        mright = True
        mup = mdown = mleft = False
    if keys[pygame.K_UP]:
        mup = True
        mleft = mdown = mright = False
    if keys[pygame.K_DOWN]:
        mdown = True
        mup = mright = mleft = False

    if mleft:
        hx -= speed
    if mright:
        hx += speed
    if mup:
        hy -= speed
    if mdown:
        hy += speed

    if hrectdownlx <= 0 or hrectuprx >= W or hrectdownly >= H or hrectupry <= 100:
        exit()

    if (hrect.x+250 > arect.x) and (hrect.x+50 < arect.x) \
            and (hrect.y+200 >= arect.y) and (hrect.y-200 <= arect.y):
        if (hrect.y+250 >= arect.y) and (hrect.y-50 < arect.y):
            hero.blit(hdownright, (0, 0))
        if (hrect.y-250 <= arect.y) and (hrect.y+50 > arect.y):
            hero.blit(hupright, (0, 0))
        if (hrect.y <= arect.y+50) and (hrect.y >= arect.y-50):
            hero.blit(hright, (0, 0))
    elif (hrect.x-250 < arect.x) and (hrect.x-50 > arect.x) \
            and (hrect.y+200 >= arect.y) and (hrect.y-200 <= arect.y):
        if (hrect.y+250 >= arect.y) and (hrect.y-50 < arect.y):
            hero.blit(hdownleft, (0, 0))
        if (hrect.y-250 <= arect.y) and (hrect.y+50 > arect.y):
            hero.blit(hleftup, (0, 0))
        if (hrect.y <= arect.y+50) and (hrect.y >= arect.y-50):
            hero.blit(hleft, (0, 0))
    elif (hrect.x+50 >= arect.x) and (hrect.x-50 <= arect.x):
        if (hrect.y+200 >= arect.y) and (hrect.y < arect.y):
            hero.blit(hdown, (0, 0))
        if (hrect.y-200 <= arect.y) and (hrect.y > arect.y):
            hero.blit(hup, (0, 0))
    else:
        hero.blit(hstand, (0, 0))

    sc.fill(BLACK)
    sc.blit(apple, arect)
    sc.blit(hero, hrect)
    pygame.draw.rect(sc, BLUE, (0, 100, W, H-100), 10)

    if hrect.colliderect(arect):
        score += scmult
        appcord = cordgen()
        scmult += 5
        speed += 0.25
        apple += 1
        print(score)

    pygame.display.update()

    clock.tick(FPS)
