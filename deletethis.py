import pygame
import random

pygame.init()

####### Define Variables \/\/\/

screen_width = 800
screen_height = 600
x = random.randint(0, 780)
y = random.randint(0, 590)
a = random.randint(0, 780)
b = random.randint(0, 590)
player_size = 20
player_speed = 7
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)

clock = pygame.time.Clock()

######## Create Objects \/\/\/

screen = pygame.display.set_mode((screen_width, screen_height))
player = pygame.Rect((400, 250, player_size, player_size))
dot = pygame.Rect((x, y, 20, 20))
evil = pygame.Rect((a, b, 20, 20))
def show_score(x, y):
    score_display = font.render("Red = Evil             Green = Good                 Score: " + str(score), 
True, (255, 255, 255))
    screen.blit(score_display, (x, y))

run = True
while run:
    
    screen.fill((0,0,0))
    show_score(10, 10)
    
    pygame.draw.rect(screen, (0, 0, 255), player)
    pygame.draw.rect(screen, (0, 255, 0), dot)
    pygame.draw.rect(screen, (255, 0, 0), evil)

######## Character Movement \/\/\/

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-player_speed, 0)
    if key[pygame.K_d] == True:
        player.move_ip(player_speed, 0)
    if key[pygame.K_w] == True:
        player.move_ip(0, -player_speed)
    if key[pygame.K_s] == True:
        player.move_ip(0, player_speed)

    if key[pygame.K_DOWN] == True:
        player.move_ip(0, player_speed)
    if key[pygame.K_UP] == True:
        player.move_ip(0, -player_speed)
    if key[pygame.K_RIGHT] == True:
        player.move_ip(player_speed, 0)
    if key[pygame.K_LEFT] == True:
        player.move_ip(-player_speed, 0)

    player.clamp_ip(screen.get_rect())

######### Snake Food Logic \/\/\/

    if player.collidepoint(evil.x, evil.y): 
        pygame.QUIT
        run = False
    if player.collidepoint(evil.x+20, evil.y+20):
        pygame.QUIT
        run = False
    if player.collidepoint(evil.x, evil.y+20):
        pygame.QUIT
        run = False
    if player.collidepoint(evil.x+20, evil.y):
        pygame.QUIT
        run = False
    
    if player.collidepoint(dot.x, dot.y):
        dot = pygame.Rect((random.randint(0, 780), random.randint(0, 590), 20, 20))
        evil = pygame.Rect((random.randint(0, 780), random.randint(0, 590), 20, 20))
        player.inflate_ip(5, 5)
        score += 1
    if player.collidepoint(dot.x+20, dot.y+20):
        dot = pygame.Rect((random.randint(0, 780), random.randint(0, 590), 20, 20))
        evil = pygame.Rect((random.randint(0, 780), random.randint(0, 590), 20, 20))
        player.inflate_ip(5, 5)
        score += 1
    if player.collidepoint(dot.x, dot.y+20):
        dot = pygame.Rect((random.randint(0, 780), random.randint(0, 590), 20, 20))
        evil = pygame.Rect((random.randint(0, 780), random.randint(0, 590), 20, 20))
        player.inflate_ip(5, 5)
        score += 1
    if player.collidepoint(dot.x+20, dot.y):
        dot = pygame.Rect((random.randint(0, 780), random.randint(0, 590), 20, 20))
        evil = pygame.Rect((random.randint(0, 780), random.randint(0, 590), 20, 20))
        player.inflate_ip(5, 5)
        score += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
    clock.tick(60)
pygame.quit()