import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('Physics Environment')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Fonts/OpenSans-Bold.ttf', 50)
ScenarioOne_active = False
ScenarioTwo_active = False
ScenarioThree_active = False
ScenarioSelect_active = True
start_time = 0

groundScenarioOne_surf = pygame.image.load('Graphics/Ground.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if ScenarioSelect_active:
        print("Scenario Select")
    else:
        if ScenarioOne_active:
            screen.blit(groundScenarioOne_surf, (0, 300))
            print("Scenario 1")

        if ScenarioTwo_active:
            screen.blit(groundScenarioOne_surf, (0, 400))  # change to Scenario two ground
            print("Scenario 2")

        if ScenarioThree_active:
            screen.blit(groundScenarioOne_surf, (0, 500))  # change to Scenario three ground
            print("Scenario 3")

    pygame.display.update()
    clock.tick(60)
