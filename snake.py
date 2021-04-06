import pygame,random

SurfaceWidth = 20
SurfaceHeight = 40
square = 20
SnakeBody = [[SurfaceHeight * 10 - 20, SurfaceWidth * 10],[SurfaceHeight * 10,SurfaceWidth], [SurfaceHeight*10 + 20, SurfaceWidth]]
SnakePos = [SurfaceHeight * 10 - 20, SurfaceWidth * 10]
Enemyx = random.randrange(1, SurfaceWidth)
Enemyy = random.randrange(1, SurfaceHeight)
EnemyPos = [[Enemyx * square],[Enemyy * square]]
Enemyflat = True
direction = 'RIGHT'
changeto = direction
score = 0
red = pygame.Color( 255, 0, 0)
blue = pygame.Color(65, 105, 255)

# LoadImages
Imgbody = pygame.transform.scale(pygame.image.load('body.jpg'),(square,square))
ImgEnemy = pygame.transform.scale(pygame.image.load('enemy.jpg'),(square,square))

# CreateSurface
pygame.init()
surface = pygame.display.set_mode(SurfaceHeight*square,SurfaceWidth*square)
pygame.display.set_caption('Snake!!!')

# GameOver
def gameOver():
    gfont = pygame.font.SysFont('Ariel', 35)
    gsurf = gfont.render('Game Over!', True, red, blue)
    grect = gsurf.get_rect()
    grect.midtop = (SurfaceHeight / 2, SurfaceWidth / 2)
    surface.blit(gsurf, grect)
    show_score(0)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

# ShowScore
def show_score(choice = 1):
    sfont = pygame.font.SysFont('Ariel', 17)
    ssurf = gfont.render('Score: {}'.format(score))
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop(70, 20)
    else:
        srect.midtop(SurfaceHeight / 2, SurfaceWidth / 2)
    surface.blit(ssurf, srect)


# mainloop
while True:
    pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # KeyEvent
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            changeto = 'RIGHT'
        if event.key == pygame.K_LEFT:
            changeto = 'LEFT'
        if event.key == pygame.K_UP:
            changeto = 'UP'
        if event.key == pygame.K_DOWN:
            changeto = 'DOWN'
        if event.key == pygame.K_ESCAPE:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
    
    #Accident event
    if SnakePos[0] >= SurfaceWidth and SnakePos[0] <= 0:
        gameOver()
    if SnakePos[1] >= SurfaceHeight and SnakePos[1] <=0:
        gameOver()
    for body in SnakeBody[1:]:
        if SnakePos[0] == body[0] and SnakePos[1] == body[1]:
            gameOver()
    
    #Direction        
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    
    # Update new position
    if direction == 'RIGHT':
        SnakePos[0] += square
    if direction == 'LEFT':
        SnakePos[0] -= square
    if direction == 'UP':
        SnakePos[1] -= square
    if direction == 'DOWN':
        SnakePos[1] += square

    # Update new body
    SnakeBody.insert(1, SnakePos)
    if SnakePos[0] == EnemyPos[0] and SnakePos[1] == EnemyPos[1]:
        score += 10
        Enemyflat = False
    else:
        SnakeBody.pop()
    
    # Born New Enemy
    if Enemyflat == False:
        Enemyx = random.randrange(1, SurfaceWidth)
        Enemyy = random.randrange(1, SurfaceHeight)
        EnemyPos = [Enemyx * square, Enemyy * square]
        Enemyflat = True
    
    # Update Surface
    for pos in SnakeBody:
        surface.blit(Imgbody, pygame.Rect(pos[0], pos[1], square, square))
    surface.blit(ImgEnemy, pygame.Rect(EnemyPos[0], EnemyPos[1], square, square)
    