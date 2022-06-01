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
    screen.blit(groundScenarioOne_surf, groundScenarioOne_rect)
    pygame.draw.rect(screen, '#000000', ((0, 520), (1200, 700)), 1000, 1)
    pygame.draw.rect(screen, '#ffffff', ((0, 520), (1200, 540)), 10, 1)
    pygame.draw.line(screen, '#ffffff', (0, 695), (1200, 695), 10)
    screen.blit(BackButton_surf, BackButton_rect)
    screen.blit(bridgeScenarioOne_surf, bridgeScenarioOne_rect)
    screen.blit(PhysicsInfo_surf, PhysicsInfo_rect)
    pygame.draw.line(screen, '#ffffff', (25, 570), (290, 570), 4)
    screen.blit(DistanceFromGround_surf, DistanceFromGround_rect)
    screen.blit(MassDropped_surf, MassDropped_rect)
    pygame.draw.line(screen, '#ffffff', (722, 102), (722, 396), 4)
    pygame.draw.line(screen, '#ffffff', (682, 396), (762, 396), 4)
    pygame.draw.line(screen, '#ffffff', (682, 102), (762, 102), 4)
    screen.blit(StartButtonScen1_surf, StartButtonScen1_rect)
    screen.blit(StopButtonScen1_surf, StopButtonScen1_rect)
    pygame.draw.circle(screen, '#ffffff', (600, DroppedMassHeight), 30)
    screen.blit(InitialVelocity_surf, InitialVelocity_rect)
    screen.blit(Gravity_surf, Gravity_rect)

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
    screen.blit(UpArrowDistance_surf, UpArrowDistance_rect)
    screen.blit(DownArrowDistance_surf, DownArrowDistance_rect)
    screen.blit(UpArrowMass_surf, UpArrowMass_rect)
    screen.blit(DownArrowMass_surf, DownArrowMass_rect)
    screen.blit(UpArrowInitialVelocity_surf, UpArrowInitialVelocity_rect)
    screen.blit(DownArrowInitialVelocity_surf, DownArrowInitialVelocity_rect)
    screen.blit(UpArrowGravity_surf, UpArrowGravity_rect)
    screen.blit(DownArrowGravity_surf, DownArrowGravity_rect)

    screen.blit(DistanceFromGroundMeasurementUnits_surf, DistanceFromGroundMeasurementUnits_rect)
    screen.blit(MassDroppedMeasurementUnits_surf, MassDroppedMeasurementUnits_rect)

    DistanceFromGroundNum_surf = Value_font.render(f'{DistanceFromGroundValue}', False, (255, 255, 255))
    DistanceFromGroundNum_rect = DistanceFromGroundNum_surf.get_rect(topleft=(20, 593))
    screen.blit(DistanceFromGroundNum_surf, DistanceFromGroundNum_rect)

    DistanceFromGroundMeasurement_surf = Value_font.render(f'{DistanceFromGroundValue}', False, (0, 0, 0))
    DistanceFromGroundMeasurement_rect = DistanceFromGroundMeasurement_surf.get_rect(topleft=(740, 250))
    screen.blit(DistanceFromGroundMeasurement_surf, DistanceFromGroundMeasurement_rect)

    MassDroppedNum_surf = Value_font.render(f'{MassDroppedValue}', False, (255, 255, 255))
    MassDroppedNum_rect = MassDroppedNum_surf.get_rect(topleft=(20, 643))
    screen.blit(MassDroppedNum_surf, MassDroppedNum_rect)

    MassDroppedMeasurement_surf = Value_font.render(f'{MassDroppedValue}', False, (0, 0, 0))
    MassDroppedMeasurement_rect = MassDroppedMeasurement_surf.get_rect(topleft=(575, 55))
    screen.blit(MassDroppedMeasurement_surf, MassDroppedMeasurement_rect)

    InitialVelocityNum_surf = Value_font.render(f'{SpeedAtBeginningOfFrame}', False, (255, 255, 255))
    InitialVelocityNum_rect = InitialVelocityNum_surf.get_rect(topleft=(200, 593))
    screen.blit(InitialVelocityNum_surf, InitialVelocityNum_rect)

    InitialVelocityMeasurement_surf = Value_font.render(f'{SpeedAtBeginningOfFrame}', False, (0, 0, 0))
    InitialVelocityMeasurement_rect = InitialVelocityMeasurement_surf.get_rect(topleft=(575, 15))
    screen.blit(InitialVelocityMeasurement_surf, InitialVelocityMeasurement_rect)

    screen.blit(InitialVelocityMeasurementUnits_surf, InitialVelocityMeasurementUnits_rect)

    GravityNum_surf = Value_font.render(f'{round(GravityValue, 2)}', False, (255, 255, 255))
    GravityNum_rect = GravityNum_surf.get_rect(topleft=(195, 643))
    screen.blit(GravityNum_surf, GravityNum_rect)

    ElapsedTimeStat_surf = DistanceFromGround_font.render("Time Elapsed: " + f'{round(EndingTime, 1)}' + " s", False, (255, 255, 255))
    ElapsedTimeStat_rect = ElapsedTimeStat_surf.get_rect(topleft=(470, 540))
    screen.blit(ElapsedTimeStat_surf, ElapsedTimeStat_rect)

    DistanceStat_surf = DistanceFromGround_font.render("Distance Travelled: " + f'{round(DistanceTravelledOverall, 1)}' + " m", False, (255, 255, 255))
    DistanceStat_rect = DistanceStat_surf.get_rect(topleft=(470, 570))
    screen.blit(DistanceStat_surf, DistanceStat_rect)

    InitialVelocityStat_surf = DistanceFromGround_font.render("Initial Velocity: " + f'{round(InitialVelocityStat, 1)}' + " m/s", False, (255, 255, 255))
    InitialVelocityStat_rect = InitialVelocityStat_surf.get_rect(topleft=(470, 600))
    screen.blit(InitialVelocityStat_surf, InitialVelocityStat_rect)

    FinalVelocityStat_surf = DistanceFromGround_font.render("Final Velocity: " + f'{round(ExtraVelocity, 1)}' + " m/s",False, (255, 255, 255))
    FinalVelocityStat_rect = FinalVelocityStat_surf.get_rect(topleft=(470, 630))
    screen.blit(FinalVelocityStat_surf, FinalVelocityStat_rect)

    AccelerationStat_surf = DistanceFromGround_font.render("Acceleration: " + f'{round(GravityValue, 1)}' + " m/s^2", False, (255, 255, 255))
    AccelerationStat_rect = AccelerationStat_surf.get_rect(topleft=(470, 660))
    screen.blit(AccelerationStat_surf, AccelerationStat_rect)

    GravityMeasurementUnits_surf = Value_font.render("Fg = " + f'{round((GravityValue * MassDroppedValue), 1)}' + "N", False, (0, 0, 0))
    GravityMeasurementUnits_rect = GravityMeasurementUnits_surf.get_rect(topleft=(1025, 55))
    screen.blit(GravityMeasurementUnits_surf, GravityMeasurementUnits_rect)

    NormalForce_surf = Value_font.render("Fn = " + f'{round((GravityValue * MassDroppedValue), 1)}' + "N", False, (0, 0, 0))
    NormalForce_rect = NormalForce_surf.get_rect(topleft=(1025, 15))
    screen.blit(NormalForce_surf, NormalForce_rect)


def Scenario1Action():
    pygame.draw.circle(screen, '#ffffff', (600, DroppedMassHeight), 30)

    InitialVelocityMeasurement_surf = Value_font.render(f'{round(SpeedAtBeginningOfFrame, 2)}' + " m/s", False, (0, 0, 0))
    InitialVelocityMeasurement_rect = InitialVelocityMeasurement_surf.get_rect(topleft=(575, 15))
    screen.blit(InitialVelocityMeasurement_surf, InitialVelocityMeasurement_rect)

    screen.blit(DistanceFromGroundMeasurementUnits_surf, DistanceFromGroundMeasurementUnits_rect)
    DistanceFromGroundMeasurement_surf = Value_font.render(f'{DistanceFromGroundValue}', False, (0, 0, 0))
    DistanceFromGroundMeasurement_rect = DistanceFromGroundMeasurement_surf.get_rect(topleft=(740, 250))
    screen.blit(DistanceFromGroundMeasurement_surf, DistanceFromGroundMeasurement_rect)

    ElapsedTimeStat_surf = DistanceFromGround_font.render("Time Elapsed: " + f'{round(EndingTime, 1)}' + " s", False,(255, 255, 255))
    ElapsedTimeStat_rect = ElapsedTimeStat_surf.get_rect(topleft=(470, 540))
    screen.blit(ElapsedTimeStat_surf, ElapsedTimeStat_rect)

    DistanceStat_surf = DistanceFromGround_font.render("Distance Travelled: " + f'{round(DistanceTravelledOverall, 1)}' + " m", False, (255, 255, 255))
    DistanceStat_rect = DistanceStat_surf.get_rect(topleft=(470, 570))
    screen.blit(DistanceStat_surf, DistanceStat_rect)

    InitialVelocityStat_surf = DistanceFromGround_font.render("Initial Velocity: " + f'{round(InitialVelocityStat, 1)}' + " m/s", False, (255, 255, 255))
    InitialVelocityStat_rect = InitialVelocityStat_surf.get_rect(topleft=(470, 600))
    screen.blit(InitialVelocityStat_surf, InitialVelocityStat_rect)

    FinalVelocityStat_surf = DistanceFromGround_font.render("Final Velocity: " + f'{round(ExtraVelocity, 1)}' + " m/s", False, (255, 255, 255))
    FinalVelocityStat_rect = FinalVelocityStat_surf.get_rect(topleft=(470, 630))
    screen.blit(FinalVelocityStat_surf, FinalVelocityStat_rect)

    AccelerationStat_surf = DistanceFromGround_font.render("Acceleration: " + f'{round(GravityValue, 1)}' + " m/s^2", False, (255, 255, 255))
    AccelerationStat_rect = AccelerationStat_surf.get_rect(topleft=(470, 660))
    screen.blit(AccelerationStat_surf, AccelerationStat_rect)

    GravityMeasurementUnits_surf = Value_font.render("Fg = " + f'{round((GravityValue * MassDroppedValue), 1)}' + "N", False, (0, 0, 0))
    GravityMeasurementUnits_rect = GravityMeasurementUnits_surf.get_rect(topleft=(1025, 55))
    screen.blit(GravityMeasurementUnits_surf, GravityMeasurementUnits_rect)


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
PhysicsInfo_font = pygame.font.Font('Fonts/AovelSansRounded-rdDL.ttf', 34)
DistanceFromGround_font = pygame.font.Font('Fonts/AovelSansRounded-rdDL.ttf', 25)
Value_font = pygame.font.Font('Fonts/AovelSansRounded-rdDL.ttf', 20)

ScenarioOne_active = False
ScenarioOneAction = False
ScenarioTwo_active = False
ScenarioThree_active = False
ScenarioSelect_active = True
start_time = 0
InitialDistanceFromGroundValue = 40
DistanceFromGroundValue = 40
MassDroppedValue = 10
DroppedMassHeight = 70
HeightOfFloor = 366
DistanceTravelledDuringFrame = 0
SpeedAtBeginningOfFrame = 0
SpeedAtEndOfFrame = 0
CurrentDistanceFromGround = 40
TimeAtBeginningOfFrame = 0
GravityValue = 9.8
ExtraDistance = 0
ExtraTime = 0
ExtraVelocity = 0
FinalTime = 0
EndingTime = 0
DistanceTravelledOverall = 0
InitialVelocityStat = 0

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
groundScenarioOne_surf = pygame.image.load('Graphics/Ground.png').convert_alpha()
groundScenarioOne_surf = pygame.transform.scale(groundScenarioOne_surf, (1200, 300))
groundScenarioOne_rect = groundScenarioOne_surf.get_rect(topleft=(0, 300))

bridgeScenarioOne_surf = pygame.image.load('Graphics/Scenario1/Bridge.png').convert_alpha()
bridgeScenarioOne_surf = pygame.transform.scale(bridgeScenarioOne_surf, (1200, 300))
bridgeScenarioOne_rect = bridgeScenarioOne_surf.get_rect(topleft=(0, 100))

BackButton_surf = pygame.image.load('Graphics/Back.png').convert_alpha()
BackButton_surf = pygame.transform.scale(BackButton_surf, (150, 70))
BackButton_rect = BackButton_surf.get_rect(topleft=(0, 0))

PhysicsInfo_surf = PhysicsInfo_font.render("Physics Information", False, (255, 255, 255))
PhysicsInfo_rect = PhysicsInfo_surf.get_rect(topleft=(30, 535))

DistanceFromGround_surf = DistanceFromGround_font.render("Distance (m)", False, (255, 255, 255))
DistanceFromGround_rect = DistanceFromGround_surf.get_rect(topleft=(50, 593))

UpArrowDistance_surf = pygame.image.load('Graphics/UpAndDownArrows/UpArrow.png').convert_alpha()
UpArrowDistance_surf = pygame.transform.scale(UpArrowDistance_surf, (80, 30))
UpArrowDistance_rect = UpArrowDistance_surf.get_rect(topleft=(0, 575))

DownArrowDistance_surf = pygame.image.load('Graphics/UpAndDownArrows/DownArrow.png').convert_alpha()
DownArrowDistance_surf = pygame.transform.scale(DownArrowDistance_surf, (80, 30))
DownArrowDistance_rect = DownArrowDistance_surf.get_rect(topleft=(-18, 605))

MassDropped_surf = DistanceFromGround_font.render("Mass (Kg)", False, (255, 255, 255))
MassDropped_rect = MassDropped_surf.get_rect(topleft=(50, 643))

MassDroppedMeasurementUnits_surf = Value_font.render("Kg", False, (0, 0, 0))
MassDroppedMeasurementUnits_rect = MassDroppedMeasurementUnits_surf.get_rect(topleft=(605, 55))

UpArrowMass_surf = pygame.image.load('Graphics/UpAndDownArrows/UpArrow.png').convert_alpha()
UpArrowMass_surf = pygame.transform.scale(UpArrowMass_surf, (80, 30))
UpArrowMass_rect = UpArrowMass_surf.get_rect(topleft=(0, 625))

DownArrowMass_surf = pygame.image.load('Graphics/UpAndDownArrows/DownArrow.png').convert_alpha()
DownArrowMass_surf = pygame.transform.scale(DownArrowMass_surf, (80, 30))
DownArrowMass_rect = DownArrowMass_surf.get_rect(topleft=(-18, 655))

DistanceFromGroundMeasurementUnits_surf = Value_font.render("m", False, (0, 0, 0))
DistanceFromGroundMeasurementUnits_rect = DistanceFromGroundMeasurementUnits_surf.get_rect(topleft=(770, 250))

StartButtonScen1_surf = pygame.image.load('Graphics/Start.png').convert_alpha()
StartButtonScen1_surf = pygame.transform.scale(StartButtonScen1_surf, (150, 70))
StartButtonScen1_rect = StartButtonScen1_surf.get_rect(topleft=(800, 570))

StopButtonScen1_surf = pygame.image.load('Graphics/Stop.png').convert_alpha()
StopButtonScen1_surf = pygame.transform.scale(StopButtonScen1_surf, (180, 90))
StopButtonScen1_rect = StopButtonScen1_surf.get_rect(topleft=(1000, 560))

InitialVelocity_surf = DistanceFromGround_font.render("Initial Velocity (m/s)", False, (255, 255, 255))
InitialVelocity_rect = InitialVelocity_surf.get_rect(topleft=(230, 593))

InitialVelocityMeasurementUnits_surf = Value_font.render("m/s", False, (0, 0, 0))
InitialVelocityMeasurementUnits_rect = MassDroppedMeasurementUnits_surf.get_rect(topleft=(605, 15))

UpArrowInitialVelocity_surf = pygame.image.load('Graphics/UpAndDownArrows/UpArrow.png').convert_alpha()
UpArrowInitialVelocity_surf = pygame.transform.scale(UpArrowInitialVelocity_surf, (80, 30))
UpArrowInitialVelocity_rect = UpArrowInitialVelocity_surf.get_rect(topleft=(180, 575))

DownArrowInitialVelocity_surf = pygame.image.load('Graphics/UpAndDownArrows/DownArrow.png').convert_alpha()
DownArrowInitialVelocity_surf = pygame.transform.scale(DownArrowInitialVelocity_surf, (80, 30))
DownArrowInitialVelocity_rect = DownArrowInitialVelocity_surf.get_rect(topleft=(162, 605))

Gravity_surf = DistanceFromGround_font.render("Gravity (m/s^2)", False, (255, 255, 255))
Gravity_rect = Gravity_surf.get_rect(topleft=(230, 643))

UpArrowGravity_surf = pygame.image.load('Graphics/UpAndDownArrows/UpArrow.png').convert_alpha()
UpArrowGravity_surf = pygame.transform.scale(UpArrowGravity_surf, (80, 30))
UpArrowGravity_rect = UpArrowGravity_surf.get_rect(topleft=(180, 625))

DownArrowGravity_surf = pygame.image.load('Graphics/UpAndDownArrows/DownArrow.png').convert_alpha()
DownArrowGravity_surf = pygame.transform.scale(DownArrowGravity_surf, (80, 30))
DownArrowGravity_rect = DownArrowInitialVelocity_surf.get_rect(topleft=(162, 655))

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

            if event.type == pygame.MOUSEBUTTONDOWN and StartButtonScen1_rect.collidepoint(mouse_pos):
                ScenarioOneAction = True

            if event.type == pygame.MOUSEBUTTONDOWN and StopButtonScen1_rect.collidepoint(mouse_pos):
                if DroppedMassHeight < DistanceTravelledDuringFrame:
                    ScenarioOneAction = False
                else:
                    ScenarioOneAction = False
                    DroppedMassHeight = 70
                    DistanceTravelledDuringFrame = 0
                    SpeedAtBeginningOfFrame = 0
                    SpeedAtEndOfFrame = 0
                    CurrentDistanceFromGround = DistanceFromGroundValue
                    TimeAtBeginningOfFrame = 0
                    DistanceTravelledOverall = 0
                    InitialVelocityStat = 0

            if event.type == pygame.MOUSEBUTTONDOWN and UpArrowDistance_rect.collidepoint(mouse_pos):
                DistanceFromGroundValue += 1
                CurrentDistanceFromGround += 1
                InitialDistanceFromGroundValue += 1

            if event.type == pygame.MOUSEBUTTONDOWN and DownArrowDistance_rect.collidepoint(mouse_pos):
                DistanceFromGroundValue -= 1
                CurrentDistanceFromGround -= 1
                InitialDistanceFromGroundValue -= 1

            if event.type == pygame.MOUSEBUTTONDOWN and UpArrowMass_rect.collidepoint(mouse_pos):
                MassDroppedValue += 1

            if event.type == pygame.MOUSEBUTTONDOWN and DownArrowMass_rect.collidepoint(mouse_pos):
                MassDroppedValue -= 1

            if event.type == pygame.MOUSEBUTTONDOWN and UpArrowInitialVelocity_rect.collidepoint(mouse_pos):
                SpeedAtBeginningOfFrame += 1
                InitialVelocityStat += 1

            if event.type == pygame.MOUSEBUTTONDOWN and DownArrowInitialVelocity_rect.collidepoint(mouse_pos):
                SpeedAtBeginningOfFrame -= 1
                InitialVelocityStat -= 1

            if event.type == pygame.MOUSEBUTTONDOWN and UpArrowGravity_rect.collidepoint(mouse_pos):
                GravityValue += 0.1

            if event.type == pygame.MOUSEBUTTONDOWN and DownArrowGravity_rect.collidepoint(mouse_pos):
                GravityValue -= 0.1

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

    if ScenarioOne_active:
        if ScenarioOneAction:
            pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
            display_Scenario1()
            Scenario1Action()
            current_time = pygame.time.get_ticks() - start_time

            if DroppedMassHeight < 366 and CurrentDistanceFromGround > DistanceTravelledDuringFrame:
                DistanceTravelledDuringFrame = (SpeedAtBeginningOfFrame * 0.05) + (0.5 * GravityValue * (0.05 * 0.05))
                SpeedAtEndOfFrame = ((2 * DistanceTravelledDuringFrame) / 0.05) - SpeedAtBeginningOfFrame
                DistanceTravelledToPx = DistanceTravelledDuringFrame / (DistanceFromGroundValue / 294)
                DroppedMassHeight += DistanceTravelledToPx

                current_time = pygame.time.get_ticks() - start_time
                DifferenceInTime = current_time - TimeAtBeginningOfFrame
                FinalTime = current_time - DifferenceInTime

                SpeedAtBeginningOfFrame = SpeedAtEndOfFrame
                TimeAtBeginningOfFrame = current_time
                CurrentDistanceFromGround -= DistanceTravelledDuringFrame
                EndingTime = FinalTime / 1000
                DistanceTravelledOverall = InitialDistanceFromGroundValue - CurrentDistanceFromGround

            else:
                ExtraDistance = HeightOfFloor - DroppedMassHeight
                ExtraTime = 0.05 * ExtraDistance
                CurrentDistanceFromGround -= CurrentDistanceFromGround
                DroppedMassHeight += ExtraDistance
                FinalTime += ExtraTime*100
                EndingTime = FinalTime/1000
                DistanceTravelledOverall = InitialDistanceFromGroundValue - CurrentDistanceFromGround
                ExtraVelocity = SpeedAtBeginningOfFrame + (GravityValue*ExtraTime)

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
