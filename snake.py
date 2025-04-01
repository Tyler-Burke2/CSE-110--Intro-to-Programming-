import pygame
import random
import high_scores

pygame.init()

# Define Variables
white = (255, 255, 255)
black = (0, 0, 0)
screen_width = 800
screen_height = 600
x = random.randint(0, 780)
y = random.randint(0, 590)
player_size = 20
player_speed = 5
dot = pygame.Rect((x, y, 20, 20))
clock = pygame.time.Clock()
score = 0
highscore = high_scores.Score
font = pygame.font.Font("freesansbold.ttf", 32)
title_font = pygame.font.Font("freesansbold.ttf", 64)
direction = "right"

# Create screens, snake, and scores
screen = pygame.display.set_mode((screen_width, screen_height))
player = pygame.Rect((400, 250, player_size, player_size))
pygame.display.set_caption("Fettuccine Snake Game")

def show_score(x, y):
    score_display = font.render("Score: " + str(score), True, white)
    screen.blit(score_display, (x, y))
def show_highscore(x, y):
    score_display = font.render("High Score: " + str(highscore), True, white)
    screen.blit(score_display, (x, y))

def title_screen():
    while True:
        screen.fill(black)
        title_text = title_font.render("     Snake Game", True, white)
        instructions_text = font.render("     Press ENTER", True, white)
        screen.blit(title_text, (100, 200))
        screen.blit(instructions_text, (250, 300))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                return

pygame.mixer.music.load('bubble.mp3')
def main_game():
    global dot, score
    run = True
    while run:
        screen.fill(black)
        show_score(10, 10)
        show_highscore(550, 10)
        
        pygame.draw.rect(screen, (0, 255, 0), player)
        pygame.draw.rect(screen, (255, 0, 0), dot)
        
# Character Movement
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            player.move_ip(-player_speed, 0)
        elif key[pygame.K_d]:
            player.move_ip(player_speed, 0)
        elif key[pygame.K_w]:
            player.move_ip(0, -player_speed)
        elif key[pygame.K_s]:
            player.move_ip(0, player_speed)
        elif key[pygame.K_DOWN]:
            player.move_ip(0, player_speed)
        elif key[pygame.K_UP]:
            player.move_ip(0, -player_speed)
        elif key[pygame.K_RIGHT]:
            player.move_ip(player_speed, 0)
        elif key[pygame.K_LEFT]:
            player.move_ip(-player_speed, 0)

        player.clamp_ip(screen.get_rect())
        
        if score>highscore:
            with open('high_scores.py', 'w') as file:
                file.write(f"Score = {score}\n")

# Snake Food Logic
        if player.colliderect(dot):
            dot = pygame.Rect(random.randint(0, 780), random.randint(0, 590), 20, 20)
            score += 1
            pygame.mixer.music.play(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(60)
    pygame.quit()

title_screen()
main_game()