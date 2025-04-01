import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Interactive 3D Game")

# Colors
colors = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255)
]

# Cube vertices
vertices = [
    (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
    (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
]

# Cube faces
faces = [
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (0, 1, 5, 4),
    (2, 3, 7, 6),
    (0, 3, 7, 4),
    (1, 2, 6, 5)
]

# Player position
player_pos = [0, 0, 5]

# Obstacles
obstacles = [[random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(5, 15)] for _ in range(5)]

def project(x, y, z):
    """ Project 3D coordinates to 2D using a simple perspective """
    fov = 500
    distance = 4
    factor = fov / (distance + z)
    x = x * factor + width // 2
    y = -y * factor + height // 2
    return (x, y)

def rotate(x, y, z, angleX, angleY):
    """ Rotate a point around the origin (0, 0, 0) """
    radX = math.radians(angleX)
    radY = math.radians(angleY)
    cosX, sinX = math.cos(radX), math.sin(radX)
    cosY, sinY = math.cos(radY), math.sin(radY)

    # Rotate around Y axis
    x1 = x * cosY - z * sinY
    z1 = z * cosY + x * sinY

    # Rotate around X axis
    y1 = y * cosX - z1 * sinX
    z2 = z1 * cosX + y * sinX

    return x1, y1, z2

def draw_cube(screen, vertices, faces, angleX, angleY, position):
    transformed_vertices = []
    for vertex in vertices:
        rotated_vertex = rotate(*vertex, angleX, angleY)
        x, y, z = rotated_vertex[0] + position[0], rotated_vertex[1] + position[1], rotated_vertex[2] + position[2]
        projected_vertex = project(x, y, z)
        transformed_vertices.append(projected_vertex)

    for i, face in enumerate(faces):
        pointlist = [transformed_vertices[vertex] for vertex in face]
        pygame.draw.polygon(screen, colors[i], pointlist, 1)

def main():
    clock = pygame.time.Clock()
    angleX, angleY = 0, 0
    move_speed = 0.1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_pos[0] -= move_speed
        if keys[pygame.K_RIGHT]:
            player_pos[0] += move_speed
        if keys[pygame.K_UP]:
            player_pos[1] += move_speed
        if keys[pygame.K_DOWN]:
            player_pos[1] -= move_speed

        screen.fill((0, 0, 30))  # Dark blue background

        # Rotate and draw player cube
        draw_cube(screen, vertices, faces, angleX, angleY, player_pos)

        # Draw obstacles
        for obstacle in obstacles:
            draw_cube(screen, vertices, faces, angleX, angleY, obstacle)

        pygame.display.flip()
        clock.tick(60)
        angleX += 1
        angleY += 1

if __name__ == "__main__":
    main()
