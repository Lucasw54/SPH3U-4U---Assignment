import pygame
from sys import exit
import math


def display_ScoreSelect():
    screen.blit(titleshadow_surf, titleshadow_rect)
    screen.blit(title_surf, title_rect)
    screen.blit(chooseScenario_surf, chooseScenario_rect)

    screen.blit(ScenarioOneSelect_surf, ScenarioOneSelect_rect)
    screen.blit(ScenarioOneText_surf, ScenarioOneText_rect)

    screen.blit(ScenarioTwoSelect_surf, ScenarioTwoSelect_rect)

    screen.blit(ScenarioThreeSelect_surf, ScenarioThreeSelect_rect)


def display_Scenario1():
    screen.blit(Scen1_ground_surf, Scen1_ground_rect)
    pygame.draw.rect(screen, '#000000', ((0, 520), (1200, 700)), 1000, 1)
    pygame.draw.rect(screen, '#ffffff', ((0, 520), (1200, 540)), 10, 1)
    pygame.draw.line(screen, '#ffffff', (0, 695), (1200, 695), 10)
    screen.blit(Scen1_BackButton_surf, Scen1_BackButton_rect)
    screen.blit(Scen1_bridge_surf, Scen1_bridge_rect)
    screen.blit(Scen1_PhysicsInfo_surf, Scen1_PhysicsInfo_rect)
    pygame.draw.line(screen, '#ffffff', (25, 570), (290, 570), 4)
    screen.blit(Scen1_DistanceFromGround_surf, Scen1_DistanceFromGround_rect)
    screen.blit(Scen1_MassDropped_surf, Scen1_MassDropped_rect)
    pygame.draw.line(screen, '#ffffff', (722, 102), (722, 396), 4)
    pygame.draw.line(screen, '#ffffff', (682, 396), (762, 396), 4)
    pygame.draw.line(screen, '#ffffff', (682, 102), (762, 102), 4)
    screen.blit(Scen1_StartButton_surf, Scen1_StartButton_rect)
    screen.blit(Scen1_StopButton_surf, Scen1_StopButton_rect)
    pygame.draw.circle(screen, '#ffffff', (600, Scen1_DroppedMassHeight), 30)
    screen.blit(Scen1_InitialVelocity_surf, Scen1_InitialVelocity_rect)
    screen.blit(Scen1_Gravity_surf, Scen1_Gravity_rect)

    pygame.draw.circle(screen, '#000000', (1000, 50), 5)
    pygame.draw.line(screen, '#000000', (1000, 50), (1000, 20), 3)
    pygame.draw.line(screen, '#000000', (1000, 20), (995, 30), 3)
    pygame.draw.line(screen, '#000000', (1000, 20), (1005, 30), 3)

    pygame.draw.line(screen, '#000000', (1000, 50), (1000, 80), 3)
    pygame.draw.line(screen, '#000000', (1000, 80), (995, 70), 3)
    pygame.draw.line(screen, '#000000', (1000, 80), (1005, 70), 3)

    pygame.draw.line(screen, '#000000', (560, 20), (560, 40), 3)
    pygame.draw.line(screen, '#000000', (560, 40), (565, 35), 3)
    pygame.draw.line(screen, '#000000', (560, 40), (555, 35), 3)


def Scenario1ValuesUpdate():
    screen.blit(Scen1_UpArrowDistance_surf, Scen1_UpArrowDistance_rect)
    screen.blit(Scen1_DownArrowDistance_surf, Scen1_DownArrowDistance_rect)
    screen.blit(Scen1_UpArrowMass_surf, Scen1_UpArrowMass_rect)
    screen.blit(Scen1_DownArrowMass_surf, Scen1_DownArrowMass_rect)
    screen.blit(Scen1_UpArrowInitialVelocity_surf, Scen1_UpArrowInitialVelocity_rect)
    screen.blit(Scen1_DownArrowInitialVelocity_surf, Scen1_DownArrowInitialVelocity_rect)
    screen.blit(Scen1_UpArrowGravity_surf, Scen1_UpArrowGravity_rect)
    screen.blit(Scen1_DownArrowGravity_surf, Scen1_DownArrowGravity_rect)

    screen.blit(Scen1_DistanceFromGroundMeasurementUnits_surf, Scen1_DistanceFromGroundMeasurementUnits_rect)
    screen.blit(Scen1_MassDroppedMeasurementUnits_surf, Scen1_MassDroppedMeasurementUnits_rect)

    Scen1_DistanceFromGroundNum_surf = Value_font.render(f'{Scen1_DistanceFromGroundValue}', False, (255, 255, 255))
    Scen1_DistanceFromGroundNum_rect = Scen1_DistanceFromGroundNum_surf.get_rect(topleft=(20, 593))
    screen.blit(Scen1_DistanceFromGroundNum_surf, Scen1_DistanceFromGroundNum_rect)

    Scen1_DistanceFromGroundMeasurement_surf = Value_font.render(f'{Scen1_DistanceFromGroundValue}', False, (0, 0, 0))
    Scen1_DistanceFromGroundMeasurement_rect = Scen1_DistanceFromGroundMeasurement_surf.get_rect(topleft=(740, 250))
    screen.blit(Scen1_DistanceFromGroundMeasurement_surf, Scen1_DistanceFromGroundMeasurement_rect)

    Scen1_MassDroppedNum_surf = Value_font.render(f'{Scen1_MassDroppedValue}', False, (255, 255, 255))
    Scen1_MassDroppedNum_rect = Scen1_MassDroppedNum_surf.get_rect(topleft=(20, 643))
    screen.blit(Scen1_MassDroppedNum_surf, Scen1_MassDroppedNum_rect)

    Scen1_MassDroppedMeasurement_surf = Value_font.render(f'{Scen1_MassDroppedValue}', False, (0, 0, 0))
    Scen1_MassDroppedMeasurement_rect = Scen1_MassDroppedMeasurement_surf.get_rect(topleft=(575, 55))
    screen.blit(Scen1_MassDroppedMeasurement_surf, Scen1_MassDroppedMeasurement_rect)

    Scen1_InitialVelocityNum_surf = Value_font.render(f'{Scen1_SpeedAtBeginningOfFrame}', False, (255, 255, 255))
    Scen1_InitialVelocityNum_rect = Scen1_InitialVelocityNum_surf.get_rect(topleft=(200, 593))
    screen.blit(Scen1_InitialVelocityNum_surf, Scen1_InitialVelocityNum_rect)

    Scen1_InitialVelocityMeasurement_surf = Value_font.render(f'{Scen1_SpeedAtBeginningOfFrame}', False, (0, 0, 0))
    Scen1_InitialVelocityMeasurement_rect = Scen1_InitialVelocityMeasurement_surf.get_rect(topleft=(575, 15))
    screen.blit(Scen1_InitialVelocityMeasurement_surf, Scen1_InitialVelocityMeasurement_rect)

    screen.blit(Scen1_InitialVelocityMeasurementUnits_surf, Scen1_InitialVelocityMeasurementUnits_rect)

    Scen1_GravityNum_surf = Value_font.render(f'{round(Scen1_GravityValue, 2)}', False, (255, 255, 255))
    Scen1_GravityNum_rect = Scen1_GravityNum_surf.get_rect(topleft=(195, 643))
    screen.blit(Scen1_GravityNum_surf, Scen1_GravityNum_rect)

    Scen1_ElapsedTimeStat_surf = DistanceFromGround_font.render("Time Elapsed: " + f'{round(Scen1_EndingTime, 1)}' + " s", False, (255, 255, 255))
    Scen1_ElapsedTimeStat_rect = Scen1_ElapsedTimeStat_surf.get_rect(topleft=(470, 540))
    screen.blit(Scen1_ElapsedTimeStat_surf, Scen1_ElapsedTimeStat_rect)

    Scen1_DistanceStat_surf = DistanceFromGround_font.render("Distance Travelled: " + f'{round(Scen1_DistanceTravelledOverall, 1)}' + " m", False, (255, 255, 255))
    Scen1_DistanceStat_rect = Scen1_DistanceStat_surf.get_rect(topleft=(470, 570))
    screen.blit(Scen1_DistanceStat_surf, Scen1_DistanceStat_rect)

    Scen1_InitialVelocityStat_surf = DistanceFromGround_font.render("Initial Velocity: " + f'{round(Scen1_InitialVelocityStat, 1)}' + " m/s", False, (255, 255, 255))
    Scen1_InitialVelocityStat_rect = Scen1_InitialVelocityStat_surf.get_rect(topleft=(470, 600))
    screen.blit(Scen1_InitialVelocityStat_surf, Scen1_InitialVelocityStat_rect)

    Scen1_FinalVelocityStat_surf = DistanceFromGround_font.render("Final Velocity: " + f'{round(Scen1_ExtraVelocity, 1)}' + " m/s",False, (255, 255, 255))
    Scen1_FinalVelocityStat_rect = Scen1_FinalVelocityStat_surf.get_rect(topleft=(470, 630))
    screen.blit(Scen1_FinalVelocityStat_surf, Scen1_FinalVelocityStat_rect)

    Scen1_AccelerationStat_surf = DistanceFromGround_font.render("Acceleration: " + f'{round(Scen1_GravityValue, 1)}' + " m/s^2", False, (255, 255, 255))
    Scen1_AccelerationStat_rect = Scen1_AccelerationStat_surf.get_rect(topleft=(470, 660))
    screen.blit(Scen1_AccelerationStat_surf, Scen1_AccelerationStat_rect)

    Scen1_GravityMeasurementUnits_surf = Value_font.render("Fg = " + f'{round((Scen1_GravityValue * Scen1_MassDroppedValue), 1)}' + " N", False, (0, 0, 0))
    Scen1_GravityMeasurementUnits_rect = Scen1_GravityMeasurementUnits_surf.get_rect(topleft=(1025, 55))
    screen.blit(Scen1_GravityMeasurementUnits_surf, Scen1_GravityMeasurementUnits_rect)

    Scen1_NormalForce_surf = Value_font.render("Fn = " + f'{round((Scen1_GravityValue * Scen1_MassDroppedValue), 1)}' + " N", False, (0, 0, 0))
    Scen1_NormalForce_rect = Scen1_NormalForce_surf.get_rect(topleft=(1025, 15))
    screen.blit(Scen1_NormalForce_surf, Scen1_NormalForce_rect)


def Scenario1Action():
    pygame.draw.circle(screen, '#ffffff', (600, Scen1_DroppedMassHeight), 30)

    Scen1_InitialVelocityMeasurement_surf = Value_font.render(f'{round(Scen1_SpeedAtBeginningOfFrame, 2)}' + " m/s", False, (0, 0, 0))
    Scen1_InitialVelocityMeasurement_rect = Scen1_InitialVelocityMeasurement_surf.get_rect(topleft=(575, 15))
    screen.blit(Scen1_InitialVelocityMeasurement_surf, Scen1_InitialVelocityMeasurement_rect)

    screen.blit(Scen1_DistanceFromGroundMeasurementUnits_surf, Scen1_DistanceFromGroundMeasurementUnits_rect)
    Scen1_DistanceFromGroundMeasurement_surf = Value_font.render(f'{Scen1_DistanceFromGroundValue}', False, (0, 0, 0))
    Scen1_DistanceFromGroundMeasurement_rect = Scen1_DistanceFromGroundMeasurement_surf.get_rect(topleft=(740, 250))
    screen.blit(Scen1_DistanceFromGroundMeasurement_surf, Scen1_DistanceFromGroundMeasurement_rect)

    Scen1_ElapsedTimeStat_surf = DistanceFromGround_font.render("Time Elapsed: " + f'{round(Scen1_EndingTime, 1)}' + " s", False,(255, 255, 255))
    Scen1_ElapsedTimeStat_rect = Scen1_ElapsedTimeStat_surf.get_rect(topleft=(470, 540))
    screen.blit(Scen1_ElapsedTimeStat_surf, Scen1_ElapsedTimeStat_rect)

    Scen1_DistanceStat_surf = DistanceFromGround_font.render("Distance Travelled: " + f'{round(Scen1_DistanceTravelledOverall, 1)}' + " m", False, (255, 255, 255))
    Scen1_DistanceStat_rect = Scen1_DistanceStat_surf.get_rect(topleft=(470, 570))
    screen.blit(Scen1_DistanceStat_surf, Scen1_DistanceStat_rect)

    Scen1_InitialVelocityStat_surf = DistanceFromGround_font.render("Initial Velocity: " + f'{round(Scen1_InitialVelocityStat, 1)}' + " m/s", False, (255, 255, 255))
    Scen1_InitialVelocityStat_rect = Scen1_InitialVelocityStat_surf.get_rect(topleft=(470, 600))
    screen.blit(Scen1_InitialVelocityStat_surf, Scen1_InitialVelocityStat_rect)

    Scen1_FinalVelocityStat_surf = DistanceFromGround_font.render("Final Velocity: " + f'{round(Scen1_ExtraVelocity, 1)}' + " m/s", False, (255, 255, 255))
    Scen1_FinalVelocityStat_rect = Scen1_FinalVelocityStat_surf.get_rect(topleft=(470, 630))
    screen.blit(Scen1_FinalVelocityStat_surf, Scen1_FinalVelocityStat_rect)

    Scen1_AccelerationStat_surf = DistanceFromGround_font.render("Acceleration: " + f'{round(Scen1_GravityValue, 1)}' + " m/s^2", False, (255, 255, 255))
    Scen1_AccelerationStat_rect = Scen1_AccelerationStat_surf.get_rect(topleft=(470, 660))
    screen.blit(Scen1_AccelerationStat_surf, Scen1_AccelerationStat_rect)

    Scen1_GravityMeasurementUnits_surf = Value_font.render("Fg = " + f'{round((Scen1_GravityValue * Scen1_MassDroppedValue), 1)}' + " N", False, (0, 0, 0))
    Scen1_GravityMeasurementUnits_rect = Scen1_GravityMeasurementUnits_surf.get_rect(topleft=(1025, 55))
    screen.blit(Scen1_GravityMeasurementUnits_surf, Scen1_GravityMeasurementUnits_rect)


def display_Scenario2():
    screen.blit(Scen1_ground_surf, (0, 400))
    pygame.draw.rect(screen, '#000000', ((0, 520), (1200, 700)), 1000, 1)
    pygame.draw.rect(screen, '#ffffff', ((0, 520), (1200, 540)), 10, 1)
    pygame.draw.line(screen, '#ffffff', (0, 695), (1200, 695), 10)
    screen.blit(Scen1_BackButton_surf, Scen1_BackButton_rect)


def display_Scenario3():
    screen.blit(Scen1_ground_surf, (0, 500))
    pygame.draw.rect(screen, '#000000', ((0, 520), (1200, 700)), 1000, 1)
    pygame.draw.rect(screen, '#ffffff', ((0, 520), (1200, 540)), 10, 1)
    pygame.draw.line(screen, '#ffffff', (0, 695), (1200, 695), 10)
    screen.blit(Scen1_BackButton_surf, Scen1_BackButton_rect)


pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('Physics Environment')
clock = pygame.time.Clock()
titleshadow_font = pygame.font.Font('Fonts/OpenSans-Bold.ttf', 71)
title_font = pygame.font.Font('Fonts/OpenSans-Bold.ttf', 70)
scenarioSelect_font = pygame.font.Font('Fonts/OpenSans-Bold.ttf', 50)
scenarios_font = pygame.font.Font('Fonts/AovelSansRounded-rdDL.ttf', 30)
PhysicsInfo_font = pygame.font.Font('Fonts/AovelSansRounded-rdDL.ttf', 34)
DistanceFromGround_font = pygame.font.Font('Fonts/AovelSansRounded-rdDL.ttf', 25)
Value_font = pygame.font.Font('Fonts/AovelSansRounded-rdDL.ttf', 20)

ScenarioOne_active = False
ScenarioOneAction = False
ScenarioTwo_active = False
ScenarioThree_active = False
ScenarioSelect_active = True
start_time = 0
Scen1_InitialDistanceFromGroundValue = 40
Scen1_DistanceFromGroundValue = 40
Scen1_MassDroppedValue = 10
Scen1_DroppedMassHeight = 70
Scen1_HeightOfFloor = 366
Scen1_DistanceTravelledDuringFrame = 0
Scen1_SpeedAtBeginningOfFrame = 0
Scen1_SpeedAtEndOfFrame = 0
Scen1_CurrentDistanceFromGround = 40
Scen1_TimeAtBeginningOfFrame = 0
Scen1_GravityValue = 9.8
Scen1_ExtraDistance = 0
Scen1_ExtraTime = 0
Scen1_ExtraVelocity = 0
Scen1_FinalTime = 0
Scen1_EndingTime = 0
Scen1_DistanceTravelledOverall = 0
Scen1_InitialVelocityStat = 0

# Intro Screen
title_surf = title_font.render("Simulated Physics Environment", False, (255, 255, 255))
title_rect = title_surf.get_rect(topleft=(10, 0))

titleshadow_surf = titleshadow_font.render("Simulated Physics Environment", False, (0, 0, 0))
titleshadow_rect = titleshadow_surf.get_rect(topleft=(10, 5))

chooseScenario_surf = scenarioSelect_font.render("Choose a Scenario", False, (255, 255, 255))
chooseScenario_rect = chooseScenario_surf.get_rect(center=(400, 150))

ScenarioOneSelect_surf = pygame.image.load('Graphics/Buttons/SelectGrey.png').convert_alpha()
ScenarioOneSelect_surf = pygame.transform.scale(ScenarioOneSelect_surf, (200, 75))
ScenarioOneSelect_rect = ScenarioOneSelect_surf.get_rect(topleft=(200, 190))

ScenarioOneText_surf = scenarios_font.render("An object dropping of a bridge", False, (255, 255, 255))
ScenarioOneText_rect = ScenarioOneText_surf.get_rect(topleft=(400, 210))

ScenarioTwoSelect_surf = pygame.image.load('Graphics/Buttons/SelectGrey.png').convert_alpha()
ScenarioTwoSelect_surf = pygame.transform.scale(ScenarioTwoSelect_surf, (200, 75))
ScenarioTwoSelect_rect = ScenarioTwoSelect_surf.get_rect(topleft=(200, 320))

ScenarioThreeSelect_surf = pygame.image.load('Graphics/Buttons/SelectGrey.png').convert_alpha()
ScenarioThreeSelect_surf = pygame.transform.scale(ScenarioThreeSelect_surf, (200, 75))
ScenarioThreeSelect_rect = ScenarioThreeSelect_surf.get_rect(topleft=(200, 450))

#  Scenario 1
Scen1_ground_surf = pygame.image.load('Graphics/Ground.png').convert_alpha()
Scen1_ground_surf = pygame.transform.scale(Scen1_ground_surf, (1200, 300))
Scen1_ground_rect = Scen1_ground_surf.get_rect(topleft=(0, 300))

Scen1_bridge_surf = pygame.image.load('Graphics/Scenario1/Bridge.png').convert_alpha()
Scen1_bridge_surf = pygame.transform.scale(Scen1_bridge_surf, (1200, 300))
Scen1_bridge_rect = Scen1_bridge_surf.get_rect(topleft=(0, 100))

Scen1_BackButton_surf = pygame.image.load('Graphics/Buttons/Back.png').convert_alpha()
Scen1_BackButton_surf = pygame.transform.scale(Scen1_BackButton_surf, (150, 70))
Scen1_BackButton_rect = Scen1_BackButton_surf.get_rect(topleft=(0, 0))

Scen1_PhysicsInfo_surf = PhysicsInfo_font.render("Physics Information", False, (255, 255, 255))
Scen1_PhysicsInfo_rect = Scen1_PhysicsInfo_surf.get_rect(topleft=(30, 535))

Scen1_DistanceFromGround_surf = DistanceFromGround_font.render("Distance (m)", False, (255, 255, 255))
Scen1_DistanceFromGround_rect = Scen1_DistanceFromGround_surf.get_rect(topleft=(50, 593))

Scen1_UpArrowDistance_surf = pygame.image.load('Graphics/UpAndDownArrows/UpArrow.png').convert_alpha()
Scen1_UpArrowDistance_surf = pygame.transform.scale(Scen1_UpArrowDistance_surf, (80, 30))
Scen1_UpArrowDistance_rect = Scen1_UpArrowDistance_surf.get_rect(topleft=(0, 575))

Scen1_DownArrowDistance_surf = pygame.image.load('Graphics/UpAndDownArrows/DownArrow.png').convert_alpha()
Scen1_DownArrowDistance_surf = pygame.transform.scale(Scen1_DownArrowDistance_surf, (80, 30))
Scen1_DownArrowDistance_rect = Scen1_DownArrowDistance_surf.get_rect(topleft=(-18, 605))

Scen1_MassDropped_surf = DistanceFromGround_font.render("Mass (Kg)", False, (255, 255, 255))
Scen1_MassDropped_rect = Scen1_MassDropped_surf.get_rect(topleft=(50, 643))

Scen1_MassDroppedMeasurementUnits_surf = Value_font.render("Kg", False, (0, 0, 0))
Scen1_MassDroppedMeasurementUnits_rect = Scen1_MassDroppedMeasurementUnits_surf.get_rect(topleft=(605, 55))

Scen1_UpArrowMass_surf = pygame.image.load('Graphics/UpAndDownArrows/UpArrow.png').convert_alpha()
Scen1_UpArrowMass_surf = pygame.transform.scale(Scen1_UpArrowMass_surf, (80, 30))
Scen1_UpArrowMass_rect = Scen1_UpArrowMass_surf.get_rect(topleft=(0, 625))

Scen1_DownArrowMass_surf = pygame.image.load('Graphics/UpAndDownArrows/DownArrow.png').convert_alpha()
Scen1_DownArrowMass_surf = pygame.transform.scale(Scen1_DownArrowMass_surf, (80, 30))
Scen1_DownArrowMass_rect = Scen1_DownArrowMass_surf.get_rect(topleft=(-18, 655))

Scen1_DistanceFromGroundMeasurementUnits_surf = Value_font.render("m", False, (0, 0, 0))
Scen1_DistanceFromGroundMeasurementUnits_rect = Scen1_DistanceFromGroundMeasurementUnits_surf.get_rect(topleft=(770, 250))

Scen1_StartButton_surf = pygame.image.load('Graphics/Buttons/Start.png').convert_alpha()
Scen1_StartButton_surf = pygame.transform.scale(Scen1_StartButton_surf, (150, 70))
Scen1_StartButton_rect = Scen1_StartButton_surf.get_rect(topleft=(800, 570))

Scen1_StopButton_surf = pygame.image.load('Graphics/Buttons/Stop.png').convert_alpha()
Scen1_StopButton_surf = pygame.transform.scale(Scen1_StopButton_surf, (180, 90))
Scen1_StopButton_rect = Scen1_StopButton_surf.get_rect(topleft=(1000, 560))

Scen1_InitialVelocity_surf = DistanceFromGround_font.render("Initial Velocity (m/s)", False, (255, 255, 255))
Scen1_InitialVelocity_rect = Scen1_InitialVelocity_surf.get_rect(topleft=(230, 593))

Scen1_InitialVelocityMeasurementUnits_surf = Value_font.render("m/s", False, (0, 0, 0))
Scen1_InitialVelocityMeasurementUnits_rect = Scen1_InitialVelocityMeasurementUnits_surf.get_rect(topleft=(605, 15))

Scen1_UpArrowInitialVelocity_surf = pygame.image.load('Graphics/UpAndDownArrows/UpArrow.png').convert_alpha()
Scen1_UpArrowInitialVelocity_surf = pygame.transform.scale(Scen1_UpArrowInitialVelocity_surf, (80, 30))
Scen1_UpArrowInitialVelocity_rect = Scen1_UpArrowInitialVelocity_surf.get_rect(topleft=(180, 575))

Scen1_DownArrowInitialVelocity_surf = pygame.image.load('Graphics/UpAndDownArrows/DownArrow.png').convert_alpha()
Scen1_DownArrowInitialVelocity_surf = pygame.transform.scale(Scen1_DownArrowInitialVelocity_surf, (80, 30))
Scen1_DownArrowInitialVelocity_rect = Scen1_DownArrowInitialVelocity_surf.get_rect(topleft=(162, 605))

Scen1_Gravity_surf = DistanceFromGround_font.render("Gravity (m/s^2)", False, (255, 255, 255))
Scen1_Gravity_rect = Scen1_Gravity_surf.get_rect(topleft=(230, 643))

Scen1_UpArrowGravity_surf = pygame.image.load('Graphics/UpAndDownArrows/UpArrow.png').convert_alpha()
Scen1_UpArrowGravity_surf = pygame.transform.scale(Scen1_UpArrowGravity_surf, (80, 30))
Scen1_UpArrowGravity_rect = Scen1_UpArrowGravity_surf.get_rect(topleft=(180, 625))

Scen1_DownArrowGravity_surf = pygame.image.load('Graphics/UpAndDownArrows/DownArrow.png').convert_alpha()
Scen1_DownArrowGravity_surf = pygame.transform.scale(Scen1_DownArrowGravity_surf, (80, 30))
Scen1_DownArrowGravity_rect = Scen1_DownArrowGravity_surf.get_rect(topleft=(162, 655))

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
            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_BackButton_rect.collidepoint(mouse_pos):
                ScenarioOne_active = False
                pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
                ScenarioSelect_active = True

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_StartButton_rect.collidepoint(mouse_pos):
                ScenarioOneAction = True

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_StopButton_rect.collidepoint(mouse_pos):
                if Scen1_DroppedMassHeight < Scen1_DistanceTravelledDuringFrame:
                    ScenarioOneAction = False
                else:
                    ScenarioOneAction = False
                    Scen1_DroppedMassHeight = 70
                    Scen1_DistanceTravelledDuringFrame = 0
                    Scen1_SpeedAtBeginningOfFrame = 0
                    Scen1_SpeedAtEndOfFrame = 0
                    Scen1_CurrentDistanceFromGround = Scen1_DistanceFromGroundValue
                    Scen1_TimeAtBeginningOfFrame = 0
                    Scen1_DistanceTravelledOverall = 0
                    Scen1_InitialVelocityStat = 0

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_UpArrowDistance_rect.collidepoint(mouse_pos):
                Scen1_DistanceFromGroundValue += 1
                Scen1_CurrentDistanceFromGround += 1
                Scen1_InitialDistanceFromGroundValue += 1

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_DownArrowDistance_rect.collidepoint(mouse_pos) and Scen1_DistanceFromGroundValue > 1:
                Scen1_DistanceFromGroundValue -= 1
                Scen1_CurrentDistanceFromGround -= 1
                Scen1_InitialDistanceFromGroundValue -= 1

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_UpArrowMass_rect.collidepoint(mouse_pos):
                Scen1_MassDroppedValue += 1

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_DownArrowMass_rect.collidepoint(mouse_pos) and Scen1_MassDroppedValue > 1:
                Scen1_MassDroppedValue -= 1

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_UpArrowInitialVelocity_rect.collidepoint(mouse_pos):
                Scen1_SpeedAtBeginningOfFrame += 1
                Scen1_InitialVelocityStat += 1

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_DownArrowInitialVelocity_rect.collidepoint(mouse_pos):
                Scen1_SpeedAtBeginningOfFrame -= 1
                Scen1_InitialVelocityStat -= 1

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_UpArrowGravity_rect.collidepoint(mouse_pos):
                Scen1_GravityValue += 0.1

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_DownArrowGravity_rect.collidepoint(mouse_pos) and Scen1_GravityValue > 0.2:
                Scen1_GravityValue -= 0.1

        if ScenarioTwo_active:
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_BackButton_rect.collidepoint(mouse_pos):
                ScenarioTwo_active = False
                pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
                ScenarioSelect_active = True

        if ScenarioThree_active:
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_BackButton_rect.collidepoint(mouse_pos):
                ScenarioThree_active = False
                pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
                ScenarioSelect_active = True

    if ScenarioSelect_active:
        pygame.draw.rect(screen, '#000000', ((0, 0), (1200, 700)), 0, 1)
        pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 110, 1)
        display_ScoreSelect()

    if ScenarioOne_active:
        if ScenarioOneAction:
            pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
            display_Scenario1()
            Scenario1Action()
            Scen1_current_time = pygame.time.get_ticks() - start_time

            if Scen1_DroppedMassHeight < 366 and Scen1_CurrentDistanceFromGround > Scen1_DistanceTravelledDuringFrame:
                Scen1_DistanceTravelledDuringFrame = (Scen1_SpeedAtBeginningOfFrame * 0.05) + (0.5 * Scen1_GravityValue * (0.05 * 0.05))
                Scen1_SpeedAtEndOfFrame = ((2 * Scen1_DistanceTravelledDuringFrame) / 0.05) - Scen1_SpeedAtBeginningOfFrame
                Scen1_DistanceTravelledToPx = Scen1_DistanceTravelledDuringFrame / (Scen1_DistanceFromGroundValue / 294)
                Scen1_DroppedMassHeight += Scen1_DistanceTravelledToPx

                Scen1_current_time = pygame.time.get_ticks() - start_time
                Scen1_DifferenceInTime = Scen1_current_time - Scen1_TimeAtBeginningOfFrame
                Scen1_FinalTime = Scen1_current_time - Scen1_DifferenceInTime

                Scen1_SpeedAtBeginningOfFrame = Scen1_SpeedAtEndOfFrame
                Scen1_TimeAtBeginningOfFrame = Scen1_current_time
                Scen1_CurrentDistanceFromGround -= Scen1_DistanceTravelledDuringFrame
                Scen1_EndingTime = Scen1_FinalTime / 1000
                Scen1_DistanceTravelledOverall = Scen1_InitialDistanceFromGroundValue - Scen1_CurrentDistanceFromGround

            else:
                Scen1_ExtraDistance = Scen1_HeightOfFloor - Scen1_DroppedMassHeight
                Scen1_ExtraTime = 0.05 * Scen1_ExtraDistance
                Scen1_CurrentDistanceFromGround -= Scen1_CurrentDistanceFromGround
                Scen1_DroppedMassHeight += Scen1_ExtraDistance
                Scen1_FinalTime += Scen1_ExtraTime*100
                Scen1_EndingTime = Scen1_FinalTime/1000
                Scen1_DistanceTravelledOverall = Scen1_InitialDistanceFromGroundValue - Scen1_CurrentDistanceFromGround
                Scen1_ExtraVelocity = Scen1_SpeedAtBeginningOfFrame + (Scen1_GravityValue*Scen1_ExtraTime)

        else:
            pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
            display_Scenario1()
            Scenario1ValuesUpdate()
            start_time = pygame.time.get_ticks()

    if ScenarioTwo_active:
        pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
        display_Scenario2()

    if ScenarioThree_active:
        pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
        display_Scenario3()

    pygame.display.update()
    clock.tick(20)
