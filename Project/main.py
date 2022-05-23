import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1400, 800))
pygame.display.set_caption('Physics Environment')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Fonts/OpenSans-Bold.ttf', 50)
game_active = True
start_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
