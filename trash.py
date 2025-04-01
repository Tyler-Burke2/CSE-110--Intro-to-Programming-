import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake-like Movement in Pygame")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SNAKE_SIZE = 20
SNAKE_SPEED = 20  # Speed should match the size for grid-like movement
snake_positions = [(100, 50), (80, 50), (60, 50)]  # Initial positions
direction = 'RIGHT'

clock = pygame.time.Clock()

def draw_snake(screen, snake_positions):
    for pos in snake_positions:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))

def update_snake(snake_positions, direction):
    x, y = snake_positions[0]
    if direction == 'UP':
        y -= SNAKE_SPEED
    elif direction == 'DOWN':
        y += SNAKE_SPEED
    elif direction == 'LEFT':
        x -= SNAKE_SPEED
    elif direction == 'RIGHT':
        x += SNAKE_SPEED

    new_head = (x, y)
    snake_positions = [new_head] + snake_positions[:-1]
    return snake_positions

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    snake_positions = update_snake(snake_positions, direction)
    screen.fill((0, 0, 0))
    draw_snake(screen, snake_positions)
    pygame.display.flip()
    clock.tick(10)  # Control the speed of the game

pygame.quit()
