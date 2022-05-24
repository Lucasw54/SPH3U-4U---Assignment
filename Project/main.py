import pygame
from sys import exit


def display_ScoreSelect():
    screen.blit(titleshadow_surf, titleshadow_rect)
    screen.blit(title_surf, title_rect)
    screen.blit(chooseScenario_surf, chooseScenario_rect)

    screen.blit(ScenarioOneSelect_surf, ScenarioOneSelect_rect)
    screen.blit(ScenarioOneText_surf, ScenarioOneText_rect)

    screen.blit(ScenarioTwoSelect_surf, ScenarioTwoSelect_rect)

    screen.blit(ScenarioThreeSelect_surf, ScenarioThreeSelect_rect)


def display_Scenario1():
    screen.blit(groundScenarioOne_surf, groundScenarioOne_rect)
    pygame.draw.rect(screen, '#000000', ((0, 520), (1200, 700)), 1000, 1)
    pygame.draw.rect(screen, '#ffffff', ((0, 520), (1200, 540)), 10, 1)
    pygame.draw.line(screen, '#ffffff', (0, 695), (1200, 695), 10)
    screen.blit(BackButton_surf, BackButton_rect)


def display_Scenario2():
    screen.blit(groundScenarioOne_surf, (0, 400))
    pygame.draw.rect(screen, '#000000', ((0, 520), (1200, 700)), 1000, 1)
    pygame.draw.rect(screen, '#ffffff', ((0, 520), (1200, 540)), 10, 1)
    pygame.draw.line(screen, '#ffffff', (0, 695), (1200, 695), 10)
    screen.blit(BackButton_surf, BackButton_rect)


def display_Scenario3():
    screen.blit(groundScenarioOne_surf, (0, 500))
    pygame.draw.rect(screen, '#000000', ((0, 520), (1200, 700)), 1000, 1)
    pygame.draw.rect(screen, '#ffffff', ((0, 520), (1200, 540)), 10, 1)
    pygame.draw.line(screen, '#ffffff', (0, 695), (1200, 695), 10)
    screen.blit(BackButton_surf, BackButton_rect)


pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('Physics Environment')
clock = pygame.time.Clock()
titleshadow_font = pygame.font.Font('Fonts/OpenSans-Bold.ttf', 71)
title_font = pygame.font.Font('Fonts/OpenSans-Bold.ttf', 70)
scenarioSelect_font = pygame.font.Font('Fonts/OpenSans-Bold.ttf', 50)
scenarios_font = pygame.font.Font('Fonts/AovelSansRounded-rdDL.ttf', 30)
ScenarioOne_active = False
ScenarioTwo_active = False
ScenarioThree_active = False
ScenarioSelect_active = True
start_time = 0

#Intro Screen
title_surf = title_font.render("Simulated Physics Environment", False, (255, 255, 255))
title_rect = title_surf.get_rect(topleft=(10, 0))

titleshadow_surf = titleshadow_font.render("Simulated Physics Environment", False, (0, 0, 0))
titleshadow_rect = titleshadow_surf.get_rect(topleft=(10, 5))

chooseScenario_surf = scenarioSelect_font.render("Choose a Scenario", False, (255, 255, 255))
chooseScenario_rect = chooseScenario_surf.get_rect(center=(400, 150))

ScenarioOneSelect_surf = pygame.image.load('Graphics/SelectButtons/SelectGrey.png').convert_alpha()
ScenarioOneSelect_surf = pygame.transform.scale(ScenarioOneSelect_surf, (200, 75))
ScenarioOneSelect_rect = ScenarioOneSelect_surf.get_rect(topleft=(200, 190))

ScenarioOneText_surf = scenarios_font.render("An object dropping of a bridge", False, (255, 255, 255))
ScenarioOneText_rect = ScenarioOneText_surf.get_rect(topleft=(400, 210))

ScenarioTwoSelect_surf = pygame.image.load('Graphics/SelectButtons/SelectGrey.png').convert_alpha()
ScenarioTwoSelect_surf = pygame.transform.scale(ScenarioTwoSelect_surf, (200, 75))
ScenarioTwoSelect_rect = ScenarioTwoSelect_surf.get_rect(topleft=(200, 320))

ScenarioThreeSelect_surf = pygame.image.load('Graphics/SelectButtons/SelectGrey.png').convert_alpha()
ScenarioThreeSelect_surf = pygame.transform.scale(ScenarioThreeSelect_surf, (200, 75))
ScenarioThreeSelect_rect = ScenarioThreeSelect_surf.get_rect(topleft=(200, 450))

#  Scenario 1
groundScenarioOne_surf = pygame.image.load('Graphics/Ground.png').convert_alpha()
groundScenarioOne_surf = pygame.transform.scale(groundScenarioOne_surf, (1200, 300))
groundScenarioOne_rect = groundScenarioOne_surf.get_rect(topleft=(0, 300))

BackButton_surf = pygame.image.load('Graphics/Back.png').convert_alpha()
BackButton_surf = pygame.transform.scale(BackButton_surf, (150, 70))
BackButton_rect = BackButton_surf.get_rect(topleft=(0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if ScenarioSelect_active:
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and ScenarioOneSelect_rect.collidepoint(mouse_pos):
                ScenarioSelect_active = False
                pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
                ScenarioOne_active = True

            if event.type == pygame.MOUSEBUTTONDOWN and ScenarioTwoSelect_rect.collidepoint(mouse_pos):
                ScenarioSelect_active = False
                pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
                ScenarioTwo_active = True

            if event.type == pygame.MOUSEBUTTONDOWN and ScenarioThreeSelect_rect.collidepoint(mouse_pos):
                ScenarioSelect_active = False
                pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
                ScenarioThree_active = True

        if ScenarioOne_active:
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and BackButton_rect.collidepoint(mouse_pos):
                ScenarioOne_active = False
                pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
                ScenarioSelect_active = True

        if ScenarioTwo_active:
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and BackButton_rect.collidepoint(mouse_pos):
                ScenarioTwo_active = False
                pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
                ScenarioSelect_active = True

        if ScenarioThree_active:
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and BackButton_rect.collidepoint(mouse_pos):
                ScenarioThree_active = False
                pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
                ScenarioSelect_active = True

    if ScenarioSelect_active:
        pygame.draw.rect(screen, '#000000', ((0, 0), (1200, 700)), 0, 1)
        pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 110, 1)
        display_ScoreSelect()

    else:
        if ScenarioOne_active:
            display_Scenario1()

        if ScenarioTwo_active:
            display_Scenario2()

        if ScenarioThree_active:
            display_Scenario3()

    pygame.display.update()
    clock.tick(60)
