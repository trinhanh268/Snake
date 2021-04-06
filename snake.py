import pygame,random, time

SurfaceWidth = 20
SurfaceHeight = 30
square = 20
SnakePos = [SurfaceWidth * 10 - 20, SurfaceHeight * 10]
SnakeBody = [[SnakePos[0],SnakePos[1]], [SnakePos[0] - 20,SnakePos[1] - 20]]
Enemyx = random.randrange(2, SurfaceWidth - 1)
Enemyy = random.randrange(2, SurfaceHeight - 1)
EnemyPos = [Enemyx * square,Enemyy * square]
Enemyflat = True
direction = 'UP'
changeto = direction
score = 0
red = pygame.Color( 255, 0, 0)
blue = pygame.Color(65, 105, 255)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
# LoadImages
Imgbody = pygame.transform.scale(pygame.image.load('body.jpg'),(square,square))
ImgEnemy = pygame.transform.scale(pygame.image.load('enemy.jpg'),(square,square))

# CreateSurface
pygame.init()
surface = pygame.display.set_mode((SurfaceWidth*square,SurfaceHeight*square))
pygame.display.set_caption('Snake!!!')

# GameOver
def gameOver():
    surface.fill(black)
    gfont = pygame.font.SysFont('Ariel', 35)
    gsurf = gfont.render('Game Over!', True, red, blue)
    grect = gsurf.get_rect()
    grect.midtop = (SurfaceWidth / 2 * square, SurfaceHeight / 2 * square)
    surface.blit(gsurf, grect)
    show_score(0)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

# ShowScore
def show_score(choice = 1):
    sfont = pygame.font.SysFont('Ariel', 17)
    ssurf = sfont.render('Score: {}'.format(score), True, blue)
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop = (70, 20)
    else:
        srect.midtop = (SurfaceWidth / 2 * square, SurfaceHeight / 2 * square + 40)
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
    
    # Accident 
    if SnakePos[0] >= (SurfaceWidth - 1) * square or SnakePos[0] < square:
        gameOver()
    if SnakePos[1] >= (SurfaceHeight - 1)* square or SnakePos[1] < square:
        gameOver()
    for body in SnakeBody[2:]:
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
    SnakeBody.insert(0, list(SnakePos))
    if SnakePos[0] == EnemyPos[0] and SnakePos[1] == EnemyPos[1]:
        score += 10
        Enemyflat = False
    else:
        SnakeBody.pop()
    
    # Born New Enemy
    if Enemyflat == False:
        Enemyx = random.randrange(2, SurfaceWidth - 1)
        Enemyy = random.randrange(2, SurfaceHeight - 1)
        EnemyPos = [Enemyx * square, Enemyy * square]
        Enemyflat = True
    
    # Update Surface
    surface.fill(white)
    for pos in SnakeBody:
        surface.blit(Imgbody, pygame.Rect(pos[0], pos[1], square, square))
    surface.blit(ImgEnemy, pygame.Rect(EnemyPos[0], EnemyPos[1], square, square))

    show_score(1)
    pygame.display.flip()
    