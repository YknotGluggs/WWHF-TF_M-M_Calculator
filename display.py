import pygame
import game
import math


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

def draw_hexagon(surface, color, center, radius):
    points = []
    for i in range(6):
        # Calculate angle for each vertex (60 degrees apart)
        angle_deg = 60 * i + 30
        angle_rad = math.radians(angle_deg)
        
        # Calculate x and y coordinates
        x = center[0] + radius * math.cos(angle_rad)
        y = center[1] + radius * math.sin(angle_rad)
        points.append((x, y))
    
    # Draw the polygon using the calculated points
    pygame.draw.polygon(surface, color, points, width=10)


def coordinate_convert(coordinates):
    #print(coordinates)
    ret = [0,0]
    if coordinates[0] == 0:
        ret[1] = coordinates[1] * 150 + 125
        if coordinates[1] == 1:
            ret[0] = coordinates[2] * 100 + 150
        else:
            ret[0] = coordinates[2] * 100 + 250
    else:
        ret[1] = coordinates[1] * 150 + 50
        if coordinates[1] == 0 or coordinates[1] == 3:
            ret[0] = coordinates[2] * 100 + 300
        else:
            ret[0] = coordinates[2] * 100 + 200
        
    return ret

while running:
    coordinates_tile, coordinates_pillar = game.game_loop()
    #print(coordinates_tile)
    #print(coordinates_pillar)
    screen.fill("white")
    for x in range(3):
        for y in range(3+x):
            draw_hexagon(screen, 'black', (200 + 50*(2-x) + 100*y, 50 + 75*x), 50)
    for y in range(6):
        draw_hexagon(screen, 'black', (150 + 100*y, 275), 50)
    for x in range(3):
        for y in range(5-x):
            draw_hexagon(screen, 'black', (200 + 50*x + 100*y, 350 + 75*x), 50)
    for x in coordinates_tile:
        pygame.draw.circle(screen, 'blue', coordinate_convert(x), 40)
    for x in coordinates_pillar:
        pygame.draw.circle(screen, 'red', coordinate_convert(x), 20)
    pygame.display.flip()
    input()
pygame.quit()