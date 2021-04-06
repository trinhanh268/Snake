import pygame,random

SurfaceWidth = 20
SurfaceHeight = 40
SnakeBody = [[SurfaceHeight * 10 - 20, SurfaceWidth * 10],[SurfaceHeight * 10,SurfaceWidth], [SurfaceHeight*10 + 20, SurfaceWidth]]
SnalePos = [[SurfaceHeight * 10 - 20, SurfaceWidth * 10]]
Enemyx = random.randrange(1, SurfaceWidth)
Enemyy = random.randrange(1, SurfaceHeight)
EnemyPos = [[Enemyx * square],[Enemyy * square]]
direction = 'RIGHT'
changeto = direction
score = 0

# LoadImages
square = 20
Imgbody = pygame.transform.scale(pygame.image.load('body.jpg'),(square,square))
ImgEnemy = pygame.transform.scale(pygame.image.load('enemy.jpg'),(square,square))

# CreateSurface
pygame.init()
surface = pygame.display.set_mode((SurfaceHeight*square,SurfaceWidth*square))
pygame.display.set_caption('Snake!!!')

# GameOver

# mainloop
while True:
    pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # surface.blit(Imgbody, pygame.Rect(SurfaceHeight*10, SurfaceWidth*10, square, square))
    # pygame.display.flip()
