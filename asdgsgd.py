import pygame
import random
import high_scores

pygame.init()

# Define Variables
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
screen_width = 800
screen_height = 600
player_size = 20
player_speed = 20  # Speed should match the size for grid-like movement
font = pygame.font.Font("freesansbold.ttf", 32)
title_font = pygame.font.Font("freesansbold.ttf", 64)

# Create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fettuccine Snake Game")
pygame.mixer.music.load('bubble.mp3')

def show_text(text, size, x, y, color=white):
    font_obj = pygame.font.Font("freesansbold.ttf", size)
    text_surface = font_obj.render(text, True, color)
    screen.blit(text_surface, (x, y))

def death_screen():
    while True:
        screen.fill(black)
        show_text("Game Over", 64, 250, 200)
        show_text("Press ENTER to Restart", 32, 250, 300)
        show_text("Press ESC to Quit", 32, 250, 350)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Restart game
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

def title_screen():
    while True:
        screen.fill(black)
        show_text("Snake Game", 64, 250, 200)
        show_text("Press ENTER to Start", 32, 250, 300)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

def main_game():
    global high_scores
    score = 0
    highscore = high_scores.Score
    snake = [pygame.Rect(400, 250, player_size, player_size)]
    direction = 'RIGHT'
    dot = pygame.Rect(random.randint(0, (screen_width - player_size) // player_speed) * player_speed,
                      random.randint(0, (screen_height - player_size) // player_speed) * player_speed,
                      player_size, player_size)
    clock = pygame.time.Clock()

    while True:
        screen.fill(black)
        show_text(f"Score: {score}", 32, 10, 10)
        show_text(f"High Score: {highscore}", 32, 550, 10)

        for segment in snake:
            pygame.draw.rect(screen, green, segment)
        pygame.draw.rect(screen, red, dot)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                if event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                if event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'

        # Move the snake
        head = snake[0].copy()
        if direction == 'LEFT':
            head.x -= player_speed
        elif direction == 'RIGHT':
            head.x += player_speed
        elif direction == 'UP':
            head.y -= player_speed
        elif direction == 'DOWN':
            head.y += player_speed

        snake.insert(0, head)

        # Snake Food Logic
        if snake[0].colliderect(dot):
            dot = pygame.Rect(random.randint(0, (screen_width - player_size) // player_speed) * player_speed,
                              random.randint(0, (screen_height - player_size) // player_speed) * player_speed,
                              player_size, player_size)
            score += 1
            pygame.mixer.music.load('bubble.mp3')
            pygame.mixer.music.play(1)

            if score > highscore:
                highscore = score
                with open('high_scores.py', 'w') as file:
                    file.write(f"Score = {highscore}\n")

        else:
            snake.pop()  # Remove last segment if no food eaten

        # Check collision with walls or self
        if (snake[0].left < 0 or snake[0].right > screen_width or
            snake[0].top < 0 or snake[0].bottom > screen_height or
            any(segment.colliderect(snake[0]) for segment in snake[1:])):
            pygame.mixer.music.load('lego.mp3') #REPLACE THIS WITH BETTER SOUND !!!!! <=========================================
            pygame.mixer.music.play(1)
            death_screen()
            return  # Restart game when the function returns

        pygame.display.update()
        clock.tick(10)  # Control game speed

# Show title screen
title_screen()

# Start game loop
while True:
    main_game()
