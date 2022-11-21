import pygame
from sys import exit
import math
#  https://phet.colorado.edu/sims/html/projectile-motion/latest/projectile-motion_en.html
#  https://www.whitman.edu/Documents/Academics/Mathematics/2016/Henelsmith.pdf
#  Explain Power Dilema (0.001s) 1 ms

def display_ScoreSelect():
    screen.blit(titleshadow_surf, titleshadow_rect)
    screen.blit(title_surf, title_rect)
    screen.blit(chooseScenario_surf, chooseScenario_rect)

    screen.blit(ScenarioOneSelect_surf, ScenarioOneSelect_rect)
    screen.blit(ScenarioOneText_surf, ScenarioOneText_rect)

    screen.blit(ScenarioTwoText_surf, ScenarioTwoText_rect)
    screen.blit(ScenarioTwoSelect_surf, ScenarioTwoSelect_rect)

    screen.blit(ScenarioThreeSelect_surf, ScenarioThreeSelect_rect)
    screen.blit(ScenarioThreeText_surf, ScenarioThreeText_rect)


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

    Scen1_InitialVelocityStat_surf = DistanceFromGround_font.render("Initial Velocity: " + f'{round(Scen1_InitialVelocityStat, 1)}' + " m/s [Down]", False, (255, 255, 255))
    Scen1_InitialVelocityStat_rect = Scen1_InitialVelocityStat_surf.get_rect(topleft=(470, 600))
    screen.blit(Scen1_InitialVelocityStat_surf, Scen1_InitialVelocityStat_rect)

    Scen1_FinalVelocityStat_surf = DistanceFromGround_font.render("Final Velocity: " + f'{round(Scen1_ExtraVelocity, 1)}' + " m/s [Down]",False, (255, 255, 255))
    Scen1_FinalVelocityStat_rect = Scen1_FinalVelocityStat_surf.get_rect(topleft=(470, 630))
    screen.blit(Scen1_FinalVelocityStat_surf, Scen1_FinalVelocityStat_rect)

    Scen1_AccelerationStat_surf = DistanceFromGround_font.render("Acceleration: " + f'{round(Scen1_GravityValue, 1)}' + " m/s^2 [Down]", False, (255, 255, 255))
    Scen1_AccelerationStat_rect = Scen1_AccelerationStat_surf.get_rect(topleft=(470, 660))
    screen.blit(Scen1_AccelerationStat_surf, Scen1_AccelerationStat_rect)

    Scen1_GravityMeasurementUnits_surf = Value_font.render("Fg = " + f'{round((Scen1_GravityValue * Scen1_MassDroppedValue), 1)}' + " N", False, (0, 0, 0))
    Scen1_GravityMeasurementUnits_rect = Scen1_GravityMeasurementUnits_surf.get_rect(topleft=(1025, 55))
    screen.blit(Scen1_GravityMeasurementUnits_surf, Scen1_GravityMeasurementUnits_rect)

    Scen1_NormalForce_surf = Value_font.render("Fn = " + f'{round((Scen1_GravityValue * Scen1_MassDroppedValue), 1)}' + " N", False, (0, 0, 0))
    Scen1_NormalForce_rect = Scen1_NormalForce_surf.get_rect(topleft=(1025, 15))
    screen.blit(Scen1_NormalForce_surf, Scen1_NormalForce_rect)

    pygame.draw.line(screen, '#000000', (1000, 50), (1000, 20), 3)
    pygame.draw.line(screen, '#000000', (1000, 20), (995, 30), 3)
    pygame.draw.line(screen, '#000000', (1000, 20), (1005, 30), 3)


def Scenario1Action():
    pygame.draw.circle(screen, '#ffffff', (600, Scen1_DroppedMassHeight), 30)
    pygame.draw.rect(screen, '#000000', ((840, 550), (170, 100)))

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

    Scen1_InitialVelocityStat_surf = DistanceFromGround_font.render("Initial Velocity: " + f'{round(Scen1_InitialVelocityStat, 1)}' + " m/s [Down]", False, (255, 255, 255))
    Scen1_InitialVelocityStat_rect = Scen1_InitialVelocityStat_surf.get_rect(topleft=(470, 600))
    screen.blit(Scen1_InitialVelocityStat_surf, Scen1_InitialVelocityStat_rect)

    Scen1_FinalVelocityStat_surf = DistanceFromGround_font.render("Final Velocity: " + f'{round(Scen1_ExtraVelocity, 1)}' + " m/s [Down]", False, (255, 255, 255))
    Scen1_FinalVelocityStat_rect = Scen1_FinalVelocityStat_surf.get_rect(topleft=(470, 630))
    screen.blit(Scen1_FinalVelocityStat_surf, Scen1_FinalVelocityStat_rect)

    Scen1_AccelerationStat_surf = DistanceFromGround_font.render("Acceleration: " + f'{round(Scen1_GravityValue, 1)}' + " m/s^2 [Down]", False, (255, 255, 255))
    Scen1_AccelerationStat_rect = Scen1_AccelerationStat_surf.get_rect(topleft=(470, 660))
    screen.blit(Scen1_AccelerationStat_surf, Scen1_AccelerationStat_rect)

    Scen1_GravityMeasurementUnits_surf = Value_font.render("Fg = " + f'{round((Scen1_GravityValue * Scen1_MassDroppedValue), 1)}' + " N", False, (0, 0, 0))
    Scen1_GravityMeasurementUnits_rect = Scen1_GravityMeasurementUnits_surf.get_rect(topleft=(1025, 55))
    screen.blit(Scen1_GravityMeasurementUnits_surf, Scen1_GravityMeasurementUnits_rect)


def display_Scenario2():
    screen.blit(Scen1_ground_surf, Scen1_ground_rect)
    screen.blit(Scen2_Cliff_surf, Scen2_Cliff_rect)
    screen.blit(Scen2_Compass_surf, Scen2_Compass_rect)
    pygame.draw.rect(screen, '#000000', ((0, 520), (1200, 700)), 1000, 1)
    pygame.draw.rect(screen, '#ffffff', ((0, 520), (1200, 540)), 10, 1)
    pygame.draw.line(screen, '#ffffff', (0, 695), (1200, 695), 10)
    screen.blit(Scen1_BackButton_surf, Scen1_BackButton_rect)
    screen.blit(Scen1_PhysicsInfo_surf, Scen1_PhysicsInfo_rect)
    pygame.draw.line(screen, '#ffffff', (25, 570), (290, 570), 4)
    screen.blit(Scen2_Angle_surf, Scen2_Angle_rect)

    #  Distance measurement lines
    pygame.draw.line(screen, '#ffffff', (900, 170), (900, 432), 4)
    pygame.draw.line(screen, '#ffffff', (850, 432), (950, 432), 4)
    pygame.draw.line(screen, '#ffffff', (850, 170), (950, 170), 4)

    screen.blit(Scen2_StartButton_surf, Scen2_StartButton_rect)
    screen.blit(Scen2_StopButton_surf, Scen2_StopButton_rect)

    pygame.draw.circle(screen, '#ffffff', (Scen2_CurrentDistanceFromLeft, Scen2_MassHeight), 15)
    screen.blit(Scen2_InitialVelocity_surf, Scen2_InitialVelocity_rect)
    screen.blit(Scen2_Gravity_surf, Scen2_Gravity_rect)

    #Direction Indication
    pygame.draw.line(screen, '#000000', (240, 20), (260, 20), 2)
    pygame.draw.line(screen, '#000000', (250, 30), (250, 10), 2)

    pygame.draw.line(screen, '#000000', (210, 85), (230, 85), 2)
    pygame.draw.line(screen, '#000000', (220, 75), (220, 95), 2)

    #  Cannon
    pygame.draw.circle(screen, '#000000', (980, 180), 10)
    pygame.draw.circle(screen, '#000000', (1060, 180), 10)
    pygame.draw.circle(screen, '#ffffff', (980, 180), 8)
    pygame.draw.circle(screen, '#ffffff', (1060, 180), 8)
    pygame.draw.line(screen, '#000000', (980, 180), (1060, 180), 3)
    pygame.draw.line(screen, '#000000', (1000, 180), (1000, 155), 3)
    pygame.draw.line(screen, '#000000', (1040, 180), (1040, 155), 3)
    pygame.draw.line(screen, '#000000', (1000, 155), (1040, 155), 3)


def Scenario2ValuesUpdate():
    #  Cannon
    pygame.draw.line(screen, '#808080', (1020, 170), (Scen2_CannonEndx, Scen2_CannonEndy), 10)

    screen.blit(Scen2_UpArrowAngle_surf, Scen2_UpArrowAngle_rect)
    screen.blit(Scen2_DownArrowAngle_surf, Scen2_DownArrowAngle_rect)
    screen.blit(Scen2_UpArrowInitialVelocity_surf, Scen2_UpArrowInitialVelocity_rect)
    screen.blit(Scen2_DownArrowInitialVelocity_surf, Scen2_DownArrowInitialVelocity_rect)
    screen.blit(Scen2_UpArrowGravity_surf, Scen2_UpArrowGravity_rect)
    screen.blit(Scen2_DownArrowGravity_surf, Scen2_DownArrowGravity_rect)

    Scen2_DistanceFromGroundMeasurement_surf = Value_font.render(f'{Scen2_DistanceFromGroundValue}' + " m", False, (0, 0, 0))
    Scen2_DistanceFromGroundMeasurement_rect = Scen2_DistanceFromGroundMeasurement_surf.get_rect(topleft=(920, 280))
    screen.blit(Scen2_DistanceFromGroundMeasurement_surf, Scen2_DistanceFromGroundMeasurement_rect)

    Scen2_AngleNum_surf = Value_font.render(f'{Scen2_AngleLaunched}', False, (255, 255, 255))
    Scen2_AngleNum_rect = Scen2_AngleNum_surf.get_rect(topleft=(20, 614))
    screen.blit(Scen2_AngleNum_surf, Scen2_AngleNum_rect)

    Scen2_MassDroppedMeasurement_surf = Small_font.render(f'{Scen2_MassDroppedValue}' + " Kg", False, (0, 0, 0))
    Scen2_MassDroppedMeasurement_rect = Scen2_MassDroppedMeasurement_surf.get_rect(topleft=(Scen2_CurrentDistanceFromLeft-10, Scen2_MassHeight-5))
    screen.blit(Scen2_MassDroppedMeasurement_surf, Scen2_MassDroppedMeasurement_rect)

    Scen2_InitialVelocityNum_surf = Value_font.render(f'{abs(Scen2_InitialVelocityStat)}', False, (255, 255, 255))
    Scen2_InitialVelocityNum_rect = Scen2_InitialVelocityNum_surf.get_rect(topleft=(150, 593))
    screen.blit(Scen2_InitialVelocityNum_surf, Scen2_InitialVelocityNum_rect)

    Scen2_GravityNum_surf = Value_font.render(f'{round(Scen2_GravityValue, 2)}', False, (255, 255, 255))
    Scen2_GravityNum_rect = Scen2_GravityNum_surf.get_rect(topleft=(145, 643))
    screen.blit(Scen2_GravityNum_surf, Scen2_GravityNum_rect)

    Scen2_ElapsedTimeStat_surf = DistanceFromGround_font.render("Time Elapsed: " + f'{round(Scen2_EndingTime, 1)}' + " s", False, (255, 255, 255))
    Scen2_ElapsedTimeStat_rect = Scen2_ElapsedTimeStat_surf.get_rect(topleft=(380, 540))
    screen.blit(Scen2_ElapsedTimeStat_surf, Scen2_ElapsedTimeStat_rect)

    Scen2_ResultantDisplacementStat_surf = DistanceFromGround_font.render("Resultant Displacement: " + f'{round(Scen2_ResultantDisplacementAmplitudeStat, 1)}' + " m [ S " + f'{round(Scen2_ResultantDisplacementAngleStat, 1)}' + "° W]", False, (255, 255, 255))
    Scen2_ResultantDisplacementStat_rect = Scen2_ResultantDisplacementStat_surf.get_rect(topleft=(380, 660))
    screen.blit(Scen2_ResultantDisplacementStat_surf, Scen2_ResultantDisplacementStat_rect)

    Scen2_DistancexStat_surf = DistanceFromGround_font.render("Distance (x): " + f'{round(abs(Scen2_DistanceTravelledx), 1)}' + " m", False, (255, 255, 255))
    Scen2_DistancexStat_rect = Scen2_DistancexStat_surf.get_rect(topleft=(730, 570))
    screen.blit(Scen2_DistancexStat_surf, Scen2_DistancexStat_rect)

    Scen2_MaxHeight_surf = DistanceFromGround_font.render("Max Height: " + f'{round(Scen2_MaxHeight, 1)}' + " m", False, (255, 255, 255))
    Scen2_MaxHeight_rect = Scen2_MaxHeight_surf.get_rect(topleft=(730, 600))
    screen.blit(Scen2_MaxHeight_surf, Scen2_MaxHeight_rect)

    Scen2_TotalEnergy_surf = DistanceFromGround_font.render("Total Energy: " + f'{round(Scen2_TotalEnergy, 1)}' + " J", False, (0, 0, 0))
    Scen2_TotalEnergy_rect = Scen2_TotalEnergy_surf.get_rect(topleft=(10, 100))
    screen.blit(Scen2_TotalEnergy_surf, Scen2_TotalEnergy_rect)

    Scen2_KineticEnergy_surf = DistanceFromGround_font.render("Kinetic " + f'{round(Scen2_KineticEnergy, 1)}' + " J", False, (0, 0, 0))
    Scen2_KineticEnergy_rect = Scen2_KineticEnergy_surf.get_rect(topleft=(10, 130))
    screen.blit(Scen2_KineticEnergy_surf, Scen2_KineticEnergy_rect)

    Scen2_GravitationalPotentialEnergy_surf = DistanceFromGround_font.render("Gravitational: " + f'{round(Scen2_GravitationalEnergy, 1)}' + " J", False, (0, 0, 0))
    Scen2_GravitationalPotentialEnergy_rect = Scen2_GravitationalPotentialEnergy_surf.get_rect(topleft=(10, 160))
    screen.blit(Scen2_GravitationalPotentialEnergy_surf, Scen2_GravitationalPotentialEnergy_rect)

    Scen2_InitialVelocityStat_surf = DistanceFromGround_font.render("Initial Velocity: " + f'{round(abs(Scen2_InitialVelocityStat), 1)}' + " m/s [U]", False, (255, 255, 255))
    Scen2_InitialVelocityStat_rect = Scen2_InitialVelocityStat_surf.get_rect(topleft=(380, 600))
    screen.blit(Scen2_InitialVelocityStat_surf, Scen2_InitialVelocityStat_rect)

    Scen2_FinalVelocityStat_surf = DistanceFromGround_font.render("Final Velocity: " + f'{round(Scen2_FinalVelocity, 1)}' + " m/s [D]", False, (255, 255, 255))
    Scen2_FinalVelocityStat_rect = Scen2_FinalVelocityStat_surf.get_rect(topleft=(380, 630))
    screen.blit(Scen2_FinalVelocityStat_surf, Scen2_FinalVelocityStat_rect)

    Scen2_AccelerationStat_surf = DistanceFromGround_font.render("Acceleration: " + f'{round(-Scen2_GravityValue, 1)}' + " m/s^2", False, (255, 255, 255))
    Scen2_AccelerationStat_rect = Scen2_AccelerationStat_surf.get_rect(topleft=(730, 540))
    screen.blit(Scen2_AccelerationStat_surf, Scen2_AccelerationStat_rect)

    Scen2_PowerStat_surf = DistanceFromGround_font.render("Cannon Power: " + f'{round(Scen2_PowerValue)}' + " W", False,(255, 255, 255))
    Scen2_PowerStat_rect = Scen2_PowerStat_surf.get_rect(topleft=(380, 570))
    screen.blit(Scen2_PowerStat_surf, Scen2_PowerStat_rect)


def Scenario2Action():
    pygame.draw.circle(screen, '#ffffff', (Scen2_CurrentDistanceFromLeft, Scen2_MassHeight), 15)
    pygame.draw.rect(screen, '#000000', ((1000, 530), (170, 80)))

    Scen2_MassDroppedMeasurement_surf = Small_font.render(f'{Scen2_MassDroppedValue}' + " Kg", False, (0, 0, 0))
    Scen2_MassDroppedMeasurement_rect = Scen2_MassDroppedMeasurement_surf.get_rect(topleft=(Scen2_CurrentDistanceFromLeft-10, Scen2_MassHeight-5))
    screen.blit(Scen2_MassDroppedMeasurement_surf, Scen2_MassDroppedMeasurement_rect)

    Scen2_DistanceFromGroundMeasurement_surf = Value_font.render(f'{Scen2_DistanceFromGroundValue}' + " m", False, (0, 0, 0))
    Scen2_DistanceFromGroundMeasurement_rect = Scen2_DistanceFromGroundMeasurement_surf.get_rect(topleft=(920, 280))
    screen.blit(Scen2_DistanceFromGroundMeasurement_surf, Scen2_DistanceFromGroundMeasurement_rect)

    Scen2_ElapsedTimeStat_surf = DistanceFromGround_font.render("Time Elapsed: " + f'{round(Scen2_EndingTime, 1)}' + " s", False, (255, 255, 255))
    Scen2_ElapsedTimeStat_rect = Scen2_ElapsedTimeStat_surf.get_rect(topleft=(380, 540))
    screen.blit(Scen2_ElapsedTimeStat_surf, Scen2_ElapsedTimeStat_rect)

    Scen2_ResultantDisplacementStat_surf = DistanceFromGround_font.render("Resultant Displacement: " + f'{round(Scen2_ResultantDisplacementAmplitudeStat, 1)}' + " m [ S " + f'{round(Scen2_ResultantDisplacementAngleStat, 1)}' + "° W]",False, (255, 255, 255))
    Scen2_ResultantDisplacementStat_rect = Scen2_ResultantDisplacementStat_surf.get_rect(topleft=(380, 660))
    screen.blit(Scen2_ResultantDisplacementStat_surf, Scen2_ResultantDisplacementStat_rect)

    Scen2_DistancexStat_surf = DistanceFromGround_font.render("Distance (x): " + f'{round(abs(Scen2_DistanceTravelledx), 1)}' + " m", False, (255, 255, 255))
    Scen2_DistancexStat_rect = Scen2_DistancexStat_surf.get_rect(topleft=(730, 570))
    screen.blit(Scen2_DistancexStat_surf, Scen2_DistancexStat_rect)

    Scen2_MaxHeight_surf = DistanceFromGround_font.render("Max Height: " + f'{round(Scen2_MaxHeight, 1)}' + " m", False,(255, 255, 255))
    Scen2_MaxHeight_rect = Scen2_MaxHeight_surf.get_rect(topleft=(730, 600))
    screen.blit(Scen2_MaxHeight_surf, Scen2_MaxHeight_rect)

    Scen2_TotalEnergy_surf = DistanceFromGround_font.render("Total Energy: " + f'{round(Scen2_TotalEnergy, 1)}' + " J", False, (0, 0, 0))
    Scen2_TotalEnergy_rect = Scen2_TotalEnergy_surf.get_rect(topleft=(10, 100))
    screen.blit(Scen2_TotalEnergy_surf, Scen2_TotalEnergy_rect)

    Scen2_KineticEnergy_surf = DistanceFromGround_font.render("Kinetic " + f'{round(Scen2_KineticEnergy, 1)}' + " J", False, (0, 0, 0))
    Scen2_KineticEnergy_rect = Scen2_KineticEnergy_surf.get_rect(topleft=(10, 130))
    screen.blit(Scen2_KineticEnergy_surf, Scen2_KineticEnergy_rect)

    Scen2_GravitationalPotentialEnergy_surf = DistanceFromGround_font.render("Gravitational: " + f'{round(Scen2_GravitationalEnergy, 1)}' + " J", False, (0, 0, 0))
    Scen2_GravitationalPotentialEnergy_rect = Scen2_GravitationalPotentialEnergy_surf.get_rect(topleft=(10, 160))
    screen.blit(Scen2_GravitationalPotentialEnergy_surf, Scen2_GravitationalPotentialEnergy_rect)

    Scen2_InitialVelocityStat_surf = DistanceFromGround_font.render("Initial Velocity: " + f'{round(abs(Scen2_InitialVelocityStat), 1)}' + " m/s [U]", False, (255, 255, 255))
    Scen2_InitialVelocityStat_rect = Scen2_InitialVelocityStat_surf.get_rect(topleft=(380, 600))
    screen.blit(Scen2_InitialVelocityStat_surf, Scen2_InitialVelocityStat_rect)

    Scen2_FinalVelocityStat_surf = DistanceFromGround_font.render("Final Velocity: " + f'{round(Scen2_FinalVelocity, 1)}' + " m/s [D]", False, (255, 255, 255))
    Scen2_FinalVelocityStat_rect = Scen2_FinalVelocityStat_surf.get_rect(topleft=(380, 630))
    screen.blit(Scen2_FinalVelocityStat_surf, Scen2_FinalVelocityStat_rect)

    Scen2_AccelerationStat_surf = DistanceFromGround_font.render("Acceleration: " + f'{round(-Scen2_GravityValue, 1)}' + " m/s^2", False, (255, 255, 255))
    Scen2_AccelerationStat_rect = Scen2_AccelerationStat_surf.get_rect(topleft=(730, 540))
    screen.blit(Scen2_AccelerationStat_surf, Scen2_AccelerationStat_rect)

    Scen2_PowerStat_surf = DistanceFromGround_font.render("Cannon Power: " + f'{round(Scen2_PowerValue)}' + " W", False,(255, 255, 255))
    Scen2_PowerStat_rect = Scen2_PowerStat_surf.get_rect(topleft=(380, 570))
    screen.blit(Scen2_PowerStat_surf, Scen2_PowerStat_rect)


def display_Scenario3():
    screen.blit(Scen3_Water_surf, Scen3_Water_rect)
    screen.blit(Scen3_LucentWater_surf, Scen3_LucentWater_rect)
    screen.blit(Scen3_RockBottom_surf, Scen3_RockBottom_rect)
    screen.blit(Scen3_Cliff_surf, Scen3_Cliff_rect)
    pygame.draw.rect(screen, '#000000', ((0, 520), (1200, 700)), 1000, 1)
    pygame.draw.rect(screen, '#ffffff', ((0, 520), (1200, 540)), 10, 1)
    pygame.draw.line(screen, '#ffffff', (0, 695), (1200, 695), 10)
    screen.blit(Scen1_BackButton_surf, Scen1_BackButton_rect)
    screen.blit(Scen1_PhysicsInfo_surf, Scen1_PhysicsInfo_rect)
    pygame.draw.line(screen, '#ffffff', (25, 570), (290, 570), 4)

    screen.blit(Scen3_StartButton_surf, Scen3_StartButton_rect)
    screen.blit(Scen3_StopButton_surf, Scen3_StopButton_rect)

def Scenario3ValuesUpdate():
    screen.blit(Scen2_UpArrowAngle_surf, Scen2_UpArrowAngle_rect)
    screen.blit(Scen2_DownArrowAngle_surf, Scen2_DownArrowAngle_rect)
    screen.blit(Scen2_UpArrowInitialVelocity_surf, Scen2_UpArrowInitialVelocity_rect)
    screen.blit(Scen2_DownArrowInitialVelocity_surf, Scen2_DownArrowInitialVelocity_rect)
    screen.blit(Scen2_UpArrowGravity_surf, Scen2_UpArrowGravity_rect)
    screen.blit(Scen2_DownArrowGravity_surf, Scen2_DownArrowGravity_rect)

    Scen3_AngleNum_surf = Value_font.render(f'{Scen3_AngleLaunched}', False, (255, 255, 255))
    Scen3_AngleNum_rect = Scen3_AngleNum_surf.get_rect(topleft=(20, 614))
    screen.blit(Scen3_AngleNum_surf, Scen3_AngleNum_rect)

    Scen3_InitialVelocityNum_surf = Value_font.render(f'{abs(Scen3_InitialVelocityStat)}', False, (255, 255, 255))
    Scen3_InitialVelocityNum_rect = Scen3_InitialVelocityNum_surf.get_rect(topleft=(150, 593))
    screen.blit(Scen3_InitialVelocityNum_surf, Scen3_InitialVelocityNum_rect)

    Scen3_GravityNum_surf = Value_font.render(f'{round(Scen3_GravityValue, 2)}', False, (255, 255, 255))
    Scen3_GravityNum_rect = Scen3_GravityNum_surf.get_rect(topleft=(145, 643))
    screen.blit(Scen3_GravityNum_surf, Scen3_GravityNum_rect)

    Scen3_ElapsedTimeStat_surf = DistanceFromGround_font.render("Time Elapsed: " + f'{round(Scen3_EndingTime, 1)}' + " s", False, (255, 255, 255))
    Scen3_ElapsedTimeStat_rect = Scen3_ElapsedTimeStat_surf.get_rect(topleft=(380, 540))
    screen.blit(Scen3_ElapsedTimeStat_surf, Scen3_ElapsedTimeStat_rect)

    Scen3_ResultantDisplacementStat_surf = DistanceFromGround_font.render("Resultant Displacement: " + f'{round(Scen3_ResultantDisplacementAmplitudeStat, 1)}' + " m [ S " + f'{round(Scen3_ResultantDisplacementAngleStat, 1)}' + "° W]",False, (255, 255, 255))
    Scen3_ResultantDisplacementStat_rect = Scen3_ResultantDisplacementStat_surf.get_rect(topleft=(380, 660))
    screen.blit(Scen3_ResultantDisplacementStat_surf, Scen3_ResultantDisplacementStat_rect)

    Scen3_DistancexStat_surf = DistanceFromGround_font.render("Distance (x): " + f'{round(abs(Scen3_DistanceTravelledx), 1)}' + " m", False, (255, 255, 255))
    Scen3_DistancexStat_rect = Scen3_DistancexStat_surf.get_rect(topleft=(730, 570))
    screen.blit(Scen3_DistancexStat_surf, Scen3_DistancexStat_rect)

    Scen3_MaxHeight_surf = DistanceFromGround_font.render("Max Height: " + f'{round(Scen3_MaxHeight, 1)}' + " m", False,(255, 255, 255))
    Scen3_MaxHeight_rect = Scen3_MaxHeight_surf.get_rect(topleft=(730, 600))
    screen.blit(Scen3_MaxHeight_surf, Scen3_MaxHeight_rect)

    Scen3_TotalEnergy_surf = DistanceFromGround_font.render("Total Energy: " + f'{round(Scen3_TotalEnergy, 1)}' + " J",False, (0, 0, 0))
    Scen3_TotalEnergy_rect = Scen3_TotalEnergy_surf.get_rect(topleft=(10, 100))
    screen.blit(Scen3_TotalEnergy_surf, Scen3_TotalEnergy_rect)

    Scen3_KineticEnergy_surf = DistanceFromGround_font.render("Kinetic " + f'{round(Scen3_KineticEnergy, 1)}' + " J",False, (0, 0, 0))
    Scen3_KineticEnergy_rect = Scen3_KineticEnergy_surf.get_rect(topleft=(10, 130))
    screen.blit(Scen3_KineticEnergy_surf, Scen3_KineticEnergy_rect)

    Scen3_GravitationalPotentialEnergy_surf = DistanceFromGround_font.render("Gravitational: " + f'{round(Scen3_GravitationalEnergy, 1)}' + " J", False, (0, 0, 0))
    Scen3_GravitationalPotentialEnergy_rect = Scen3_GravitationalPotentialEnergy_surf.get_rect(topleft=(10, 160))
    screen.blit(Scen3_GravitationalPotentialEnergy_surf, Scen3_GravitationalPotentialEnergy_rect)

    Scen3_InitialVelocityStat_surf = DistanceFromGround_font.render("Initial Velocity: " + f'{round(abs(Scen3_InitialVelocityStat), 1)}' + " m/s [U]", False, (255, 255, 255))
    Scen3_InitialVelocityStat_rect = Scen3_InitialVelocityStat_surf.get_rect(topleft=(380, 600))
    screen.blit(Scen3_InitialVelocityStat_surf, Scen3_InitialVelocityStat_rect)

    Scen3_FinalVelocityStat_surf = DistanceFromGround_font.render("Final Velocity: " + f'{round(Scen3_FinalVelocity, 1)}' + " m/s [D]", False, (255, 255, 255))
    Scen3_FinalVelocityStat_rect = Scen3_FinalVelocityStat_surf.get_rect(topleft=(380, 630))
    screen.blit(Scen3_FinalVelocityStat_surf, Scen3_FinalVelocityStat_rect)

    Scen3_AccelerationStat_surf = DistanceFromGround_font.render("Acceleration: " + f'{round(-Scen3_GravityValue, 1)}' + " m/s^2", False, (255, 255, 255))
    Scen3_AccelerationStat_rect = Scen3_AccelerationStat_surf.get_rect(topleft=(730, 540))
    screen.blit(Scen3_AccelerationStat_surf, Scen3_AccelerationStat_rect)

    Scen3_PowerStat_surf = DistanceFromGround_font.render("Cannon Power: " + f'{round(Scen3_PowerValue)}' + " W", False,(255, 255, 255))
    Scen3_PowerStat_rect = Scen3_PowerStat_surf.get_rect(topleft=(380, 570))
    screen.blit(Scen3_PowerStat_surf, Scen3_PowerStat_rect)


def Scenario3Action():
    print("HI")
    pygame.draw.circle(screen, '#ffffff', (Scen3_CurrentDistanceFromLeft, Scen3_MassHeight), 15)
    pygame.draw.rect(screen, '#000000', ((1000, 530), (170, 80)))

    Scen3_MassDroppedMeasurement_surf = Small_font.render(f'{Scen3_MassDroppedValue}' + " Kg", False, (0, 0, 0))
    Scen3_MassDroppedMeasurement_rect = Scen3_MassDroppedMeasurement_surf.get_rect(topleft=(Scen3_CurrentDistanceFromLeft - 10, Scen3_MassHeight - 5))
    screen.blit(Scen3_MassDroppedMeasurement_surf, Scen3_MassDroppedMeasurement_rect)

    Scen3_DistanceFromGroundMeasurement_surf = Value_font.render(f'{Scen3_DistanceFromGroundValue}' + " m", False, (0, 0, 0))
    Scen3_DistanceFromGroundMeasurement_rect = Scen3_DistanceFromGroundMeasurement_surf.get_rect(topleft=(920, 280))
    screen.blit(Scen3_DistanceFromGroundMeasurement_surf, Scen3_DistanceFromGroundMeasurement_rect)

    Scen3_ElapsedTimeStat_surf = DistanceFromGround_font.render("Time Elapsed: " + f'{round(Scen3_EndingTime, 1)}' + " s", False, (255, 255, 255))
    Scen3_ElapsedTimeStat_rect = Scen3_ElapsedTimeStat_surf.get_rect(topleft=(380, 540))
    screen.blit(Scen3_ElapsedTimeStat_surf, Scen3_ElapsedTimeStat_rect)

    Scen3_ResultantDisplacementStat_surf = DistanceFromGround_font.render("Resultant Displacement: " + f'{round(Scen3_ResultantDisplacementAmplitudeStat, 1)}' + " m [ S " + f'{round(Scen3_ResultantDisplacementAngleStat, 1)}' + "° W]", False, (255, 255, 255))
    Scen3_ResultantDisplacementStat_rect = Scen3_ResultantDisplacementStat_surf.get_rect(topleft=(380, 660))
    screen.blit(Scen3_ResultantDisplacementStat_surf, Scen3_ResultantDisplacementStat_rect)

    Scen3_DistancexStat_surf = DistanceFromGround_font.render("Distance (x): " + f'{round(abs(Scen3_DistanceTravelledx), 1)}' + " m", False, (255, 255, 255))
    Scen3_DistancexStat_rect = Scen3_DistancexStat_surf.get_rect(topleft=(730, 570))
    screen.blit(Scen3_DistancexStat_surf, Scen3_DistancexStat_rect)

    Scen3_MaxHeight_surf = DistanceFromGround_font.render("Max Height: " + f'{round(Scen3_MaxHeight, 1)}' + " m", False, (255, 255, 255))
    Scen3_MaxHeight_rect = Scen3_MaxHeight_surf.get_rect(topleft=(730, 600))
    screen.blit(Scen3_MaxHeight_surf, Scen3_MaxHeight_rect)

    Scen3_TotalEnergy_surf = DistanceFromGround_font.render("Total Energy: " + f'{round(Scen3_TotalEnergy, 1)}' + " J", False, (0, 0, 0))
    Scen3_TotalEnergy_rect = Scen3_TotalEnergy_surf.get_rect(topleft=(10, 100))
    screen.blit(Scen3_TotalEnergy_surf, Scen3_TotalEnergy_rect)

    Scen3_KineticEnergy_surf = DistanceFromGround_font.render("Kinetic " + f'{round(Scen3_KineticEnergy, 1)}' + " J", False, (0, 0, 0))
    Scen3_KineticEnergy_rect = Scen3_KineticEnergy_surf.get_rect(topleft=(10, 130))
    screen.blit(Scen3_KineticEnergy_surf, Scen3_KineticEnergy_rect)

    Scen3_GravitationalPotentialEnergy_surf = DistanceFromGround_font.render("Gravitational: " + f'{round(Scen3_GravitationalEnergy, 1)}' + " J", False, (0, 0, 0))
    Scen3_GravitationalPotentialEnergy_rect = Scen3_GravitationalPotentialEnergy_surf.get_rect(topleft=(10, 160))
    screen.blit(Scen3_GravitationalPotentialEnergy_surf, Scen3_GravitationalPotentialEnergy_rect)

    Scen3_InitialVelocityStat_surf = DistanceFromGround_font.render("Initial Velocity: " + f'{round(abs(Scen3_InitialVelocityStat), 1)}' + " m/s [U]", False, (255, 255, 255))
    Scen3_InitialVelocityStat_rect = Scen3_InitialVelocityStat_surf.get_rect(topleft=(380, 600))
    screen.blit(Scen3_InitialVelocityStat_surf, Scen3_InitialVelocityStat_rect)

    Scen3_FinalVelocityStat_surf = DistanceFromGround_font.render("Final Velocity: " + f'{round(Scen3_FinalVelocity, 1)}' + " m/s [D]", False, (255, 255, 255))
    Scen3_FinalVelocityStat_rect = Scen3_FinalVelocityStat_surf.get_rect(topleft=(380, 630))
    screen.blit(Scen3_FinalVelocityStat_surf, Scen3_FinalVelocityStat_rect)

    Scen3_AccelerationStat_surf = DistanceFromGround_font.render("Acceleration: " + f'{round(-Scen3_GravityValue, 1)}' + " m/s^2", False, (255, 255, 255))
    Scen3_AccelerationStat_rect = Scen3_AccelerationStat_surf.get_rect(topleft=(730, 540))
    screen.blit(Scen3_AccelerationStat_surf, Scen3_AccelerationStat_rect)

    Scen3_PowerStat_surf = DistanceFromGround_font.render("Cannon Power: " + f'{round(Scen3_PowerValue)}' + " W", False, (255, 255, 255))
    Scen3_PowerStat_rect = Scen3_PowerStat_surf.get_rect(topleft=(380, 570))
    screen.blit(Scen3_PowerStat_surf, Scen3_PowerStat_rect)


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
DistanceFromGround_font = pygame.font.Font('Fonts/AovelSansRounded-rdDL.ttf', 25,)
Value_font = pygame.font.Font('Fonts/AovelSansRounded-rdDL.ttf', 20)
Small_font = pygame.font.Font('Fonts/AovelSansRounded-rdDL.ttf', 9)

ScenarioOne_active = False
ScenarioOneAction = False
ScenarioTwo_active = False
ScenarioTwoAction = False
ScenarioThree_active = False
ScenarioThreeAction = False
ScenarioSelect_active = True
start_time = 0

#  Scenario One Variables
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

#  Scenario Two Variables
Scen2_MassHeight = 170
Scen2_CurrentDistanceFromLeft = 1020
Scen2_InitialDistanceFromGroundValue = 20
Scen2_DistanceFromGroundValue = 20
Scen2_MassDroppedValue = 10
Scen2_HeightOfFloor = 417
Scen2_DistanceTravelledVERTDuringFrame = 0
Scen2_DistanceTravelledHORIZDuringFrame = 0
Scen2_SpeedAtEndOfFrame = 0
Scen2_CurrentDistanceFromGround = 20
Scen2_TimeAtBeginningOfFrame = 0
Scen2_GravityValue = 9.8
Scen2_ExtraDistance = 0
Scen2_ExtraTime = 0
Scen2_ExtraVelocity = 0
Scen2_FinalTime = 0
Scen2_EndingTime = 0
Scen2_DistanceTravelledOverall = 0
Scen2_AngleLaunched = 45
Scen2_InitialVelocityStat = -15
Scen2_HorizontalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat*(math.cos(Scen2_AngleLaunched * (math.pi / 180)))
Scen2_VerticalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat*(math.sin(Scen2_AngleLaunched) * (math.pi / 180))
Scen2_InitialVerticalVelocityStat = Scen2_InitialVelocityStat*(math.sin(Scen2_AngleLaunched * (math.pi / 180)))
Scen2_FinalVerticalVelocityStat = math.sqrt((Scen2_InitialVerticalVelocityStat * Scen2_InitialVerticalVelocityStat) + (2 * Scen2_GravityValue * Scen2_InitialDistanceFromGroundValue))
Scen2_EstimatedAirTime = (Scen2_FinalVerticalVelocityStat - Scen2_InitialVerticalVelocityStat)/Scen2_GravityValue
Scen2_EstimatedDistance = Scen2_EstimatedAirTime * Scen2_HorizontalVelocityAtBeginningOfFrame
Scen2_MaxHeight = 0
Scen2_DistanceTravelledx = 0
Scen2_FinalVelocity = 0

Scen2_DisplacementxStat = 0
Scen2_DisplacementyStat = 0
Scen2_PowerValue = 0
Scen2_ResultantDisplacementAmplitudeStat = 0
Scen2_ResultantDisplacementAngleStat = 0
Scen2_TotalEnergy = 0
Scen2_KineticEnergy = 0
Scen2_GravitationalEnergy = 0

# Scenario Three Variables
Scen3_MassHeight = 170
Scen3_CurrentDistanceFromLeft = 1020
Scen3_InitialDistanceFromGroundValue = 20
Scen3_DistanceFromGroundValue = 20
Scen3_MassDroppedValue = 10
Scen3_HeightOfFloor = 417
Scen3_DistanceTravelledVERTDuringFrame = 0
Scen3_DistanceTravelledHORIZDuringFrame = 0
Scen3_SpeedAtEndOfFrame = 0
Scen3_CurrentDistanceFromGround = 20
Scen3_TimeAtBeginningOfFrame = 0
Scen3_GravityValue = 9.8
Scen3_ExtraDistance = 0
Scen3_ExtraTime = 0
Scen3_ExtraVelocity = 0
Scen3_FinalTime = 0
Scen3_EndingTime = 0
Scen3_DistanceTravelledOverall = 0
Scen3_AngleLaunched = 45
Scen3_InitialVelocityStat = -15
Scen3_HorizontalVelocityAtBeginningOfFrame = Scen3_InitialVelocityStat*(math.cos(Scen3_AngleLaunched * (math.pi / 180)))
Scen3_VerticalVelocityAtBeginningOfFrame = Scen3_InitialVelocityStat*(math.sin(Scen3_AngleLaunched) * (math.pi / 180))
Scen3_InitialVerticalVelocityStat = Scen3_InitialVelocityStat*(math.sin(Scen3_AngleLaunched * (math.pi / 180)))
Scen3_FinalVerticalVelocityStat = math.sqrt((Scen3_InitialVerticalVelocityStat * Scen3_InitialVerticalVelocityStat) + (2 * Scen3_GravityValue * Scen3_InitialDistanceFromGroundValue))
Scen3_EstimatedAirTime = (Scen3_FinalVerticalVelocityStat - Scen3_InitialVerticalVelocityStat)/Scen3_GravityValue
Scen3_EstimatedDistance = Scen3_EstimatedAirTime * Scen2_HorizontalVelocityAtBeginningOfFrame
Scen3_MaxHeight = 0
Scen3_DistanceTravelledx = 0
Scen3_FinalVelocity = 0

Scen3_DisplacementxStat = 0
Scen3_DisplacementyStat = 0
Scen3_PowerValue = 0
Scen3_ResultantDisplacementAmplitudeStat = 0
Scen3_ResultantDisplacementAngleStat = 0
Scen3_TotalEnergy = 0
Scen3_KineticEnergy = 0
Scen3_GravitationalEnergy = 0

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

ScenarioTwoText_surf = scenarios_font.render("An object being launched off a cliff", False, (255, 255, 255))
ScenarioTwoText_rect = ScenarioTwoText_surf.get_rect(topleft=(400, 340))

ScenarioThreeText_surf = scenarios_font.render("A bungee jumper jumping off a cliff", False, (255, 255, 255))
ScenarioThreeText_rect = ScenarioThreeText_surf.get_rect(topleft=(400, 470))

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
Scen1_StartButton_rect = Scen1_StartButton_surf.get_rect(topleft=(850, 570))

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

#  Scenario 2
Scen2_Compass_surf = pygame.image.load('Graphics/Scenario2/Compass.png').convert_alpha()
Scen2_Compass_surf = pygame.transform.scale(Scen2_Compass_surf, (120, 104))
Scen2_Compass_rect = Scen2_Compass_surf.get_rect(topleft=(220, 10))

Scen2_Cliff_surf = pygame.image.load('Graphics/Scenario2/Cliff.png').convert_alpha()
Scen2_Cliff_surf = pygame.transform.scale(Scen2_Cliff_surf, (500, 357))
Scen2_Cliff_rect = Scen2_Cliff_surf.get_rect(topleft=(700, 75))

Scen2_ground_surf = pygame.image.load('Graphics/Ground.png').convert_alpha()
Scen2_ground_surf = pygame.transform.scale(Scen2_ground_surf, (1200, 300))
Scen2_ground_rect = Scen2_ground_surf.get_rect(topleft=(0, 300))

Scen2_BackButton_surf = pygame.image.load('Graphics/Buttons/Back.png').convert_alpha()
Scen2_BackButton_surf = pygame.transform.scale(Scen2_BackButton_surf, (150, 70))
Scen2_BackButton_rect = Scen2_BackButton_surf.get_rect(topleft=(0, 0))

Scen2_PhysicsInfo_surf = PhysicsInfo_font.render("Physics Information", False, (255, 255, 255))
Scen2_PhysicsInfo_rect = Scen2_PhysicsInfo_surf.get_rect(topleft=(30, 535))

Scen2_DistanceFromGround_surf = DistanceFromGround_font.render("Distance (m)", False, (255, 255, 255))
Scen2_DistanceFromGround_rect = Scen2_DistanceFromGround_surf.get_rect(topleft=(50, 593))

Scen2_UpArrowDistance_surf = pygame.image.load('Graphics/UpAndDownArrows/UpArrow.png').convert_alpha()
Scen2_UpArrowDistance_surf = pygame.transform.scale(Scen2_UpArrowDistance_surf, (80, 30))
Scen2_UpArrowDistance_rect = Scen2_UpArrowDistance_surf.get_rect(topleft=(0, 575))

Scen2_DownArrowDistance_surf = pygame.image.load('Graphics/UpAndDownArrows/DownArrow.png').convert_alpha()
Scen2_DownArrowDistance_surf = pygame.transform.scale(Scen2_DownArrowDistance_surf, (80, 30))
Scen2_DownArrowDistance_rect = Scen2_DownArrowDistance_surf.get_rect(topleft=(-18, 605))

Scen2_Angle_surf = DistanceFromGround_font.render("Angle (°)", False, (255, 255, 255))
Scen2_Angle_rect = Scen2_Angle_surf.get_rect(topleft=(50, 615))

Scen2_UpArrowAngle_surf = pygame.image.load('Graphics/UpAndDownArrows/UpArrow.png').convert_alpha()
Scen2_UpArrowAngle_surf = pygame.transform.scale(Scen2_UpArrowAngle_surf, (80, 30))
Scen2_UpArrowAngle_rect = Scen2_UpArrowAngle_surf.get_rect(topleft=(0, 595))

Scen2_DownArrowAngle_surf = pygame.image.load('Graphics/UpAndDownArrows/DownArrow.png').convert_alpha()
Scen2_DownArrowAngle_surf = pygame.transform.scale(Scen2_DownArrowAngle_surf, (80, 30))
Scen2_DownArrowAngle_rect = Scen2_DownArrowAngle_surf.get_rect(topleft=(-18, 625))

Scen2_StartButton_surf = pygame.image.load('Graphics/Buttons/Start.png').convert_alpha()
Scen2_StartButton_surf = pygame.transform.scale(Scen2_StartButton_surf, (150, 70))
Scen2_StartButton_rect = Scen2_StartButton_surf.get_rect(topleft=(1012, 540))

Scen2_StopButton_surf = pygame.image.load('Graphics/Buttons/Stop.png').convert_alpha()
Scen2_StopButton_surf = pygame.transform.scale(Scen2_StopButton_surf, (180, 90))
Scen2_StopButton_rect = Scen2_StopButton_surf.get_rect(topleft=(1000, 600))

Scen2_InitialVelocity_surf = DistanceFromGround_font.render("Initial Velocity (m/s)", False, (255, 255, 255))
Scen2_InitialVelocity_rect = Scen2_InitialVelocity_surf.get_rect(topleft=(180, 593))

Scen2_InitialVelocityMeasurementUnits_surf = Value_font.render("m/s", False, (0, 0, 0))
Scen2_InitialVelocityMeasurementUnits_rect = Scen2_InitialVelocityMeasurementUnits_surf.get_rect(topleft=(605, 15))

Scen2_UpArrowInitialVelocity_surf = pygame.image.load('Graphics/UpAndDownArrows/UpArrow.png').convert_alpha()
Scen2_UpArrowInitialVelocity_surf = pygame.transform.scale(Scen2_UpArrowInitialVelocity_surf, (80, 30))
Scen2_UpArrowInitialVelocity_rect = Scen2_UpArrowInitialVelocity_surf.get_rect(topleft=(130, 575))

Scen2_DownArrowInitialVelocity_surf = pygame.image.load('Graphics/UpAndDownArrows/DownArrow.png').convert_alpha()
Scen2_DownArrowInitialVelocity_surf = pygame.transform.scale(Scen2_DownArrowInitialVelocity_surf, (80, 30))
Scen2_DownArrowInitialVelocity_rect = Scen2_DownArrowInitialVelocity_surf.get_rect(topleft=(112, 605))

Scen2_Gravity_surf = DistanceFromGround_font.render("Gravity (m/s^2)", False, (255, 255, 255))
Scen2_Gravity_rect = Scen2_Gravity_surf.get_rect(topleft=(180, 643))

Scen2_UpArrowGravity_surf = pygame.image.load('Graphics/UpAndDownArrows/UpArrow.png').convert_alpha()
Scen2_UpArrowGravity_surf = pygame.transform.scale(Scen2_UpArrowGravity_surf, (80, 30))
Scen2_UpArrowGravity_rect = Scen2_UpArrowGravity_surf.get_rect(topleft=(130, 625))

Scen2_DownArrowGravity_surf = pygame.image.load('Graphics/UpAndDownArrows/DownArrow.png').convert_alpha()
Scen2_DownArrowGravity_surf = pygame.transform.scale(Scen2_DownArrowGravity_surf, (80, 30))
Scen2_DownArrowGravity_rect = Scen2_DownArrowGravity_surf.get_rect(topleft=(112, 655))

# Scenario 3
Scen3_Water_surf = pygame.image.load('Graphics/Scenario3/Water2.png').convert_alpha()
Scen3_Water_surf = pygame.transform.scale(Scen3_Water_surf, (1400, 100))
Scen3_Water_rect = Scen3_Water_surf.get_rect(topleft=(-100, 350))

Scen3_LucentWater_surf = pygame.image.load('Graphics/Scenario3/SeeThroughWater.png').convert_alpha()
Scen3_LucentWater_surf = pygame.transform.scale(Scen3_LucentWater_surf, (1400, 100))
Scen3_LucentWater_rect = Scen3_LucentWater_surf.get_rect(topleft=(-100, 450))

Scen3_RockBottom_surf = pygame.image.load('Graphics/Scenario3/RockBottom.png').convert_alpha()
Scen3_RockBottom_surf = pygame.transform.scale(Scen3_RockBottom_surf, (1400, 120))
Scen3_RockBottom_rect = Scen3_RockBottom_surf.get_rect(topleft=(-100, 450))

Scen3_Cliff_surf = pygame.image.load('Graphics/Scenario3/Cliff3.png').convert_alpha()
Scen3_Cliff_surf = pygame.transform.scale(Scen3_Cliff_surf, (1400, 370))
Scen3_Cliff_rect = Scen3_Cliff_surf.get_rect(topleft=(-100, 60))

Scen3_StartButton_surf = pygame.image.load('Graphics/Buttons/Start.png').convert_alpha()
Scen3_StartButton_surf = pygame.transform.scale(Scen3_StartButton_surf, (150, 70))
Scen3_StartButton_rect = Scen3_StartButton_surf.get_rect(topleft=(1012, 540))

Scen3_StopButton_surf = pygame.image.load('Graphics/Buttons/Stop.png').convert_alpha()
Scen3_StopButton_surf = pygame.transform.scale(Scen3_StopButton_surf, (180, 90))
Scen3_StopButton_rect = Scen3_StopButton_surf.get_rect(topleft=(1000, 600))


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

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_StartButton_rect.collidepoint(mouse_pos) and ScenarioOneAction == False:
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

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_UpArrowDistance_rect.collidepoint(mouse_pos) and ScenarioOneAction == False:
                Scen1_DistanceFromGroundValue += 1
                Scen1_CurrentDistanceFromGround += 1
                Scen1_InitialDistanceFromGroundValue += 1

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_DownArrowDistance_rect.collidepoint(mouse_pos) and Scen1_DistanceFromGroundValue > 1 and ScenarioOneAction == False:
                Scen1_DistanceFromGroundValue -= 1
                Scen1_CurrentDistanceFromGround -= 1
                Scen1_InitialDistanceFromGroundValue -= 1

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_UpArrowMass_rect.collidepoint(mouse_pos) and ScenarioOneAction == False:
                Scen1_MassDroppedValue += 1

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_DownArrowMass_rect.collidepoint(mouse_pos) and Scen1_MassDroppedValue > 1 and ScenarioOneAction == False:
                Scen1_MassDroppedValue -= 1

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_UpArrowInitialVelocity_rect.collidepoint(mouse_pos) and ScenarioOneAction == False:
                Scen1_SpeedAtBeginningOfFrame += 1
                Scen1_InitialVelocityStat += 1

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_DownArrowInitialVelocity_rect.collidepoint(mouse_pos) and Scen1_InitialVelocityStat > 0 and ScenarioOneAction == False:
                Scen1_SpeedAtBeginningOfFrame -= 1
                Scen1_InitialVelocityStat -= 1

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_UpArrowGravity_rect.collidepoint(mouse_pos) and ScenarioOneAction == False:
                Scen1_GravityValue += 0.1

            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_DownArrowGravity_rect.collidepoint(mouse_pos) and Scen1_GravityValue > 0.2 and ScenarioOneAction == False:
                Scen1_GravityValue -= 0.1

        if ScenarioTwo_active:
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_BackButton_rect.collidepoint(mouse_pos):
                ScenarioTwo_active = False
                pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
                ScenarioSelect_active = True

            if event.type == pygame.MOUSEBUTTONDOWN and Scen2_StartButton_rect.collidepoint(mouse_pos) and ScenarioTwoAction == False:
                ScenarioTwoAction = True
                Scen2_MassHeight = 170
                Scen2_CurrentDistanceFromLeft = 1020
                Scen2_DistanceTravelledVERTDuringFrame = 0
                Scen2_DistanceTravelledHORIZDuringFrame = 0
                Scen2_HorizontalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat * (math.cos(Scen2_AngleLaunched * (math.pi / 180)))
                Scen2_VerticalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat * (math.sin(Scen2_AngleLaunched * (math.pi / 180)))

                Scen2_SpeedAtEndOfFrame = 0
                Scen2_CurrentDistanceFromGround = Scen2_DistanceFromGroundValue
                Scen2_TimeAtBeginningOfFrame = 0
                Scen2_DistanceTravelledOverall = 0
                Scen2_DisplacementxStat = 0
                Scen2_DisplacementyStat = 0

            if event.type == pygame.MOUSEBUTTONDOWN and Scen2_StopButton_rect.collidepoint(mouse_pos):
                if Scen2_MassHeight < Scen2_DistanceTravelledVERTDuringFrame:
                    ScenarioTwoAction = False
                else:
                    ScenarioTwoAction = False
                    Scen2_MassHeight = 170
                    Scen2_CurrentDistanceFromLeft = 1020
                    Scen2_DistanceTravelledVERTDuringFrame = 0
                    Scen2_DistanceTravelledHORIZDuringFrame = 0
                    Scen2_HorizontalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat * (math.cos(Scen2_AngleLaunched * (math.pi / 180)))
                    Scen2_VerticalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat * (math.sin(Scen2_AngleLaunched * (math.pi / 180)))

                    Scen2_SpeedAtEndOfFrame = 0
                    Scen2_CurrentDistanceFromGround = Scen2_DistanceFromGroundValue
                    Scen2_TimeAtBeginningOfFrame = 0
                    Scen2_DistanceTravelledOverall = 0
                    Scen2_DisplacementxStat = 0
                    Scen2_DisplacementyStat = 0

            if event.type == pygame.MOUSEBUTTONDOWN and Scen2_UpArrowAngle_rect.collidepoint(mouse_pos) and Scen2_AngleLaunched < 90 and ScenarioTwoAction == False:
                Scen2_AngleLaunched += 1
                Scen2_HorizontalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat * (math.cos(Scen2_AngleLaunched * (math.pi / 180)))
                Scen2_VerticalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat * (math.sin(Scen2_AngleLaunched * (math.pi / 180)))

                Scen2_HorizontalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat * (math.cos(Scen2_AngleLaunched * (math.pi / 180)))
                Scen2_VerticalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat * (math.sin(Scen2_AngleLaunched) * (math.pi / 180))
                Scen2_InitialVerticalVelocityStat = Scen2_InitialVelocityStat * (math.sin(Scen2_AngleLaunched * (math.pi / 180)))
                Scen2_FinalVerticalVelocityStat = math.sqrt((Scen2_InitialVerticalVelocityStat * Scen2_InitialVerticalVelocityStat) + (2 * Scen2_GravityValue * Scen2_InitialDistanceFromGroundValue))
                Scen2_EstimatedAirTime = (Scen2_FinalVerticalVelocityStat - Scen2_InitialVerticalVelocityStat) / Scen2_GravityValue
                Scen2_EstimatedDistance = Scen2_EstimatedAirTime * Scen2_HorizontalVelocityAtBeginningOfFrame


            if event.type == pygame.MOUSEBUTTONDOWN and Scen2_DownArrowAngle_rect.collidepoint(mouse_pos) and Scen2_AngleLaunched > 0 and ScenarioTwoAction == False:
                Scen2_AngleLaunched -= 1
                Scen2_HorizontalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat * (math.cos(Scen2_AngleLaunched * (math.pi / 180)))
                Scen2_VerticalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat * (math.sin(Scen2_AngleLaunched * (math.pi / 180)))

                Scen2_HorizontalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat * (math.cos(Scen2_AngleLaunched * (math.pi / 180)))
                Scen2_VerticalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat * (math.sin(Scen2_AngleLaunched) * (math.pi / 180))
                Scen2_InitialVerticalVelocityStat = Scen2_InitialVelocityStat * (math.sin(Scen2_AngleLaunched * (math.pi / 180)))
                Scen2_FinalVerticalVelocityStat = math.sqrt((Scen2_InitialVerticalVelocityStat * Scen2_InitialVerticalVelocityStat) + (2 * Scen2_GravityValue * Scen2_InitialDistanceFromGroundValue))
                Scen2_EstimatedAirTime = (Scen2_FinalVerticalVelocityStat - Scen2_InitialVerticalVelocityStat) / Scen2_GravityValue
                Scen2_EstimatedDistance = Scen2_EstimatedAirTime * Scen2_HorizontalVelocityAtBeginningOfFrame

            if event.type == pygame.MOUSEBUTTONDOWN and Scen2_UpArrowInitialVelocity_rect.collidepoint(mouse_pos) and ScenarioTwoAction == False:
                Scen2_InitialVelocityStat -= 1
                Scen2_VerticalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat*(math.sin(Scen2_AngleLaunched * (math.pi / 180)))
                Scen2_HorizontalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat * (math.cos(Scen2_AngleLaunched) * (math.pi / 180))

            if event.type == pygame.MOUSEBUTTONDOWN and Scen2_DownArrowInitialVelocity_rect.collidepoint(mouse_pos) and abs(Scen2_InitialVelocityStat) > 0 and ScenarioTwoAction == False:
                Scen2_InitialVelocityStat += 1
                Scen2_VerticalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat*(math.sin(Scen2_AngleLaunched * (math.pi / 180)))
                Scen2_HorizontalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat * (math.cos(Scen2_AngleLaunched * (math.pi / 180)))

            if event.type == pygame.MOUSEBUTTONDOWN and Scen2_UpArrowGravity_rect.collidepoint(mouse_pos) and ScenarioTwoAction == False:
                Scen2_GravityValue += 0.1

            if event.type == pygame.MOUSEBUTTONDOWN and Scen2_DownArrowGravity_rect.collidepoint(mouse_pos) and Scen2_GravityValue > 0.2 and ScenarioTwoAction == False:
                Scen2_GravityValue -= 0.1

        if ScenarioThree_active:
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and Scen1_BackButton_rect.collidepoint(mouse_pos):
                ScenarioThree_active = False
                pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
                ScenarioSelect_active = True

            if event.type == pygame.MOUSEBUTTONDOWN and Scen3_StartButton_rect.collidepoint(mouse_pos) and ScenarioTwoAction == False:
                Scenario3Action = True

                Scen3_MassHeight = 170
                Scen3_CurrentDistanceFromLeft = 1020
                Scen3_DistanceTravelledVERTDuringFrame = 0
                Scen3_DistanceTravelledHORIZDuringFrame = 0
                Scen3_HorizontalVelocityAtBeginningOfFrame = Scen3_InitialVelocityStat * (math.cos(Scen3_AngleLaunched * (math.pi / 180)))
                Scen2_VerticalVelocityAtBeginningOfFrame = Scen3_InitialVelocityStat * (math.sin(Scen3_AngleLaunched * (math.pi / 180)))

                Scen3_SpeedAtEndOfFrame = 0
                Scen3_CurrentDistanceFromGround = Scen3_DistanceFromGroundValue
                Scen3_TimeAtBeginningOfFrame = 0
                Scen3_DistanceTravelledOverall = 0
                Scen3_DisplacementxStat = 0
                Scen3_DisplacementyStat = 0

            if event.type == pygame.MOUSEBUTTONDOWN and Scen3_StopButton_rect.collidepoint(mouse_pos):
                if Scen3_MassHeight < Scen3_DistanceTravelledVERTDuringFrame:
                    Scenario3Action = False
                else:
                    Scenario3Action = False
                    Scen3_MassHeight = 170
                    Scen3_CurrentDistanceFromLeft = 1020
                    Scen3_DistanceTravelledVERTDuringFrame = 0
                    Scen3_DistanceTravelledHORIZDuringFrame = 0
                    Scen3_HorizontalVelocityAtBeginningOfFrame = Scen3_InitialVelocityStat * (math.cos(Scen3_AngleLaunched * (math.pi / 180)))
                    Scen3_VerticalVelocityAtBeginningOfFrame = Scen3_InitialVelocityStat * (math.sin(Scen3_AngleLaunched * (math.pi / 180)))

                    Scen3_SpeedAtEndOfFrame = 0
                    Scen3_CurrentDistanceFromGround = Scen3_DistanceFromGroundValue
                    Scen3_TimeAtBeginningOfFrame = 0
                    Scen3_DistanceTravelledOverall = 0
                    Scen3_DisplacementxStat = 0
                    Scen3_DisplacementyStat = 0

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
                Scen1_DistanceTravelledToPx = Scen1_DistanceTravelledDuringFrame / (Scen1_DistanceFromGroundValue / 296)
                Scen1_DroppedMassHeight += Scen1_DistanceTravelledToPx

                Scen1_current_time = pygame.time.get_ticks() - start_time
                Scen1_DifferenceInTime = Scen1_current_time - Scen1_TimeAtBeginningOfFrame
                Scen1_FinalTime = Scen1_current_time - Scen1_DifferenceInTime

                Scen1_SpeedAtBeginningOfFrame = Scen1_SpeedAtEndOfFrame
                Scen1_TimeAtBeginningOfFrame = Scen1_current_time
                Scen1_CurrentDistanceFromGround -= Scen1_DistanceTravelledDuringFrame
                Scen1_EndingTime = Scen1_FinalTime / 1000
                Scen1_DistanceTravelledOverall = Scen1_InitialDistanceFromGroundValue - Scen1_CurrentDistanceFromGround
                print(Scen1_SpeedAtBeginningOfFrame)
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
        Scen2_Cannon_a = 70 * (math.sin(Scen2_AngleLaunched * (math.pi / 180)))
        Scen2_Cannon_b = 70 * (math.cos(Scen2_AngleLaunched * (math.pi / 180)))
        Scen2_CannonEndx = 1020 - Scen2_Cannon_b
        Scen2_CannonEndy = 170 - Scen2_Cannon_a

        if ScenarioTwoAction:
            pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
            display_Scenario2()
            Scenario2Action()
            Scen2_current_time = pygame.time.get_ticks() - start_time


            if Scen2_MassHeight < Scen2_HeightOfFloor and Scen2_CurrentDistanceFromGround > Scen2_DistanceTravelledVERTDuringFrame:
                #  VERT
                Scen2_DistanceTravelledVERTDuringFrame = (Scen2_VerticalVelocityAtBeginningOfFrame * 0.05) + (0.5 * Scen2_GravityValue * (0.05 * 0.05))
                Scen2_SpeedAtEndOfFrame = ((2 * Scen2_DistanceTravelledVERTDuringFrame) / 0.05) - Scen2_VerticalVelocityAtBeginningOfFrame
                Scen2_DistanceTravelledToPx = Scen2_DistanceTravelledVERTDuringFrame / (Scen2_DistanceFromGroundValue / 247)
                Scen2_MassHeight += Scen2_DistanceTravelledToPx

                Scen2_current_time = pygame.time.get_ticks() - start_time
                Scen2_DifferenceInTime = Scen2_current_time - Scen2_TimeAtBeginningOfFrame
                Scen2_FinalTime = Scen2_current_time - Scen2_DifferenceInTime

                Scen2_VerticalVelocityAtBeginningOfFrame = Scen2_SpeedAtEndOfFrame
                Scen2_TimeAtBeginningOfFrame = Scen2_current_time
                Scen2_CurrentDistanceFromGround -= Scen2_DistanceTravelledVERTDuringFrame
                Scen2_EndingTime = Scen2_FinalTime / 1000
                Scen2_DistanceTravelledOverall = Scen2_InitialDistanceFromGroundValue - Scen2_CurrentDistanceFromGround
                Scen2_DisplacementyStat += abs(Scen2_DistanceTravelledVERTDuringFrame)

                #  HORIZ
                Scen2_HorizontalVelocityAtBeginningOfFrame = Scen2_InitialVelocityStat * (math.cos(Scen2_AngleLaunched * (math.pi / 180)))
                Scen2_InitialVerticalVelocityStat = Scen2_InitialVelocityStat * (math.sin(Scen2_AngleLaunched * (math.pi / 180)))
                Scen2_FinalVerticalVelocityStat = math.sqrt((Scen2_InitialVerticalVelocityStat * Scen2_InitialVerticalVelocityStat) + (2 * Scen2_GravityValue * Scen2_InitialDistanceFromGroundValue))
                Scen2_EstimatedAirTime = (Scen2_FinalVerticalVelocityStat - Scen2_InitialVerticalVelocityStat) / Scen2_GravityValue
                Scen2_TotalDisplacementx = Scen2_HorizontalVelocityAtBeginningOfFrame*Scen2_EstimatedAirTime
                Scen2_HorizontalNumberOfFrames = Scen2_EstimatedAirTime / (1/20)
                Scen2_DistanceTravelledHORIZDuringFrame = Scen2_TotalDisplacementx / Scen2_HorizontalNumberOfFrames
                Scen2_DistanceTravelledHORIZToPx = Scen2_DistanceTravelledHORIZDuringFrame / 0.08
                Scen2_CurrentDistanceFromLeft -= abs(Scen2_DistanceTravelledHORIZToPx)
                Scen2_DisplacementxStat += abs(Scen2_DistanceTravelledHORIZDuringFrame)
                Scen2_EstimatedDistance = Scen2_EstimatedAirTime * Scen2_HorizontalVelocityAtBeginningOfFrame
                Scen2_EstimatedDistanceToPx = Scen2_EstimatedDistance / 0.136

                #  Random
                Scen2_Cannon_a = Scen2_AngleLaunched
                Scen2_Cannon_b = 0
                Scen2_FinalVelocity = math.sqrt((Scen2_FinalVerticalVelocityStat*Scen2_FinalVerticalVelocityStat)+(abs(Scen2_HorizontalVelocityAtBeginningOfFrame)*abs(Scen2_HorizontalVelocityAtBeginningOfFrame)))
                Scen2_PowerValue = (0.5*Scen2_MassDroppedValue*(Scen2_InitialVelocityStat*Scen2_InitialVelocityStat))/1
                Scen2_MaxHeight = ((-(Scen2_InitialVerticalVelocityStat*Scen2_InitialVerticalVelocityStat))/-(Scen2_GravityValue*2))+Scen2_DistanceFromGroundValue
                Scen2_DistanceTravelledx = Scen2_EstimatedAirTime*Scen2_HorizontalVelocityAtBeginningOfFrame
                Scen2_ResultantDisplacementAmplitudeStat = math.sqrt((Scen2_DistanceFromGroundValue*Scen2_DistanceFromGroundValue)+(Scen2_DistanceTravelledx*Scen2_DistanceTravelledx))
                Scen2_ResultantDisplacementAngleStat = (math.atan(abs(Scen2_DistanceTravelledx)/Scen2_DistanceFromGroundValue)*180/math.pi)
                Scen2_TotalEnergy = (10*Scen2_GravityValue*Scen2_DistanceFromGroundValue) + (0.5*10*(Scen2_InitialVelocityStat*Scen2_InitialVelocityStat))
                Scen2_KineticEnergy = Scen2_TotalEnergy - (10*Scen2_GravityValue*Scen2_CurrentDistanceFromGround)
                Scen2_GravitationalEnergy = Scen2_TotalEnergy - Scen2_KineticEnergy
            else:
                Scen2_ExtraDistance = Scen2_HeightOfFloor - Scen2_MassHeight
                Scen2_ExtraTime = 0.05 * Scen2_ExtraDistance
                Scen2_CurrentDistanceFromGround -= Scen2_CurrentDistanceFromGround
                Scen2_MassHeight += Scen2_ExtraDistance
                Scen2_FinalTime += Scen2_ExtraTime * 100
                Scen2_EndingTime = Scen2_FinalTime / 1000
                Scen2_DistanceTravelledOverall = Scen2_InitialDistanceFromGroundValue - Scen2_CurrentDistanceFromGround
                Scen2_ExtraVelocity = Scen2_VerticalVelocityAtBeginningOfFrame + (Scen2_GravityValue * Scen2_ExtraTime)

                Scen2_DisplacementxStat -= abs(Scen2_EstimatedDistanceToPx - Scen2_DisplacementxStat)

                Scen2_KineticEnergy = Scen2_TotalEnergy
                Scen2_GravitationalEnergy = 0
        else:
            pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
            display_Scenario2()
            Scenario2ValuesUpdate()
            start_time = pygame.time.get_ticks()

    if ScenarioThree_active:
        Scen2_Cannon_a = 70 * (math.sin(Scen2_AngleLaunched * (math.pi / 180)))
        Scen2_Cannon_b = 70 * (math.cos(Scen2_AngleLaunched * (math.pi / 180)))
        Scen2_CannonEndx = 1020 - Scen2_Cannon_b
        Scen2_CannonEndy = 170 - Scen2_Cannon_a

        if ScenarioThreeAction:
            pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
            display_Scenario3()
            Scenario3Action()
            Scen3_current_time = pygame.time.get_ticks() - start_time

            if Scen3_MassHeight < Scen3_HeightOfFloor and Scen3_CurrentDistanceFromGround > Scen3_DistanceTravelledVERTDuringFrame:
                #  VERT
                Scen3_DistanceTravelledVERTDuringFrame = (Scen3_VerticalVelocityAtBeginningOfFrame * 0.05) + (0.5 * Scen3_GravityValue * (0.05 * 0.05))
                Scen3_SpeedAtEndOfFrame = ((2 * Scen3_DistanceTravelledVERTDuringFrame) / 0.05) - Scen3_VerticalVelocityAtBeginningOfFrame
                Scen3_DistanceTravelledToPx = Scen3_DistanceTravelledVERTDuringFrame / (Scen3_DistanceFromGroundValue / 247)
                Scen3_MassHeight += Scen3_DistanceTravelledToPx

                Scen3_current_time = pygame.time.get_ticks() - start_time
                Scen3_DifferenceInTime = Scen3_current_time - Scen3_TimeAtBeginningOfFrame
                Scen3_FinalTime = Scen3_current_time - Scen3_DifferenceInTime

                Scen3_VerticalVelocityAtBeginningOfFrame = Scen3_SpeedAtEndOfFrame
                Scen3_TimeAtBeginningOfFrame = Scen3_current_time
                Scen3_CurrentDistanceFromGround -= Scen3_DistanceTravelledVERTDuringFrame
                Scen3_EndingTime = Scen2_FinalTime / 1000
                Scen3_DistanceTravelledOverall = Scen3_InitialDistanceFromGroundValue - Scen3_CurrentDistanceFromGround
                Scen3_DisplacementyStat += abs(Scen3_DistanceTravelledVERTDuringFrame)

                #  HORIZ
                Scen3_HorizontalVelocityAtBeginningOfFrame = Scen3_InitialVelocityStat * (math.cos(Scen3_AngleLaunched * (math.pi / 180)))
                Scen3_InitialVerticalVelocityStat = Scen3_InitialVelocityStat * (math.sin(Scen3_AngleLaunched * (math.pi / 180)))
                Scen3_FinalVerticalVelocityStat = math.sqrt((Scen2_InitialVerticalVelocityStat * Scen3_InitialVerticalVelocityStat) + (2 * Scen3_GravityValue * Scen3_InitialDistanceFromGroundValue))
                Scen3_EstimatedAirTime = (Scen3_FinalVerticalVelocityStat - Scen3_InitialVerticalVelocityStat) / Scen3_GravityValue
                Scen3_TotalDisplacementx = Scen3_HorizontalVelocityAtBeginningOfFrame*Scen3_EstimatedAirTime
                Scen3_HorizontalNumberOfFrames = Scen3_EstimatedAirTime / (1/20)
                Scen3_DistanceTravelledHORIZDuringFrame = Scen3_TotalDisplacementx / Scen3_HorizontalNumberOfFrames
                Scen3_DistanceTravelledHORIZToPx = Scen3_DistanceTravelledHORIZDuringFrame / 0.08
                Scen3_CurrentDistanceFromLeft -= abs(Scen3_DistanceTravelledHORIZToPx)
                Scen3_DisplacementxStat += abs(Scen3_DistanceTravelledHORIZDuringFrame)
                Scen3_EstimatedDistance = Scen3_EstimatedAirTime * Scen3_HorizontalVelocityAtBeginningOfFrame
                Scen3_EstimatedDistanceToPx = Scen3_EstimatedDistance / 0.136

                #  Random
                Scen3_Cannon_a = Scen3_AngleLaunched
                Scen3_Cannon_b = 0
                Scen3_FinalVelocity = math.sqrt((Scen3_FinalVerticalVelocityStat*Scen3_FinalVerticalVelocityStat)+(abs(Scen3_HorizontalVelocityAtBeginningOfFrame)*abs(Scen3_HorizontalVelocityAtBeginningOfFrame)))
                Scen3_PowerValue = (0.5*Scen3_MassDroppedValue*(Scen3_InitialVelocityStat*Scen3_InitialVelocityStat))/1
                Scen3_MaxHeight = ((-(Scen3_InitialVerticalVelocityStat*Scen3_InitialVerticalVelocityStat))/-(Scen3_GravityValue*2))+Scen3_DistanceFromGroundValue
                Scen3_DistanceTravelledx = Scen3_EstimatedAirTime*Scen3_HorizontalVelocityAtBeginningOfFrame
                Scen3_ResultantDisplacementAmplitudeStat = math.sqrt((Scen3_DistanceFromGroundValue*Scen3_DistanceFromGroundValue)+(Scen3_DistanceTravelledx*Scen3_DistanceTravelledx))
                Scen3_ResultantDisplacementAngleStat = (math.atan(abs(Scen3_DistanceTravelledx)/Scen3_DistanceFromGroundValue)*180/math.pi)
                Scen3_TotalEnergy = (10*Scen3_GravityValue*Scen3_DistanceFromGroundValue) + (0.5*10*(Scen3_InitialVelocityStat*Scen3_InitialVelocityStat))
                Scen3_KineticEnergy = Scen3_TotalEnergy - (10*Scen3_GravityValue*Scen3_CurrentDistanceFromGround)
                Scen3_GravitationalEnergy = Scen3_TotalEnergy - Scen3_KineticEnergy
            else:
                Scen3_ExtraDistance = Scen3_HeightOfFloor - Scen3_MassHeight
                Scen3_ExtraTime = 0.05 * Scen3_ExtraDistance
                Scen3_CurrentDistanceFromGround -= Scen3_CurrentDistanceFromGround
                Scen3_MassHeight += Scen3_ExtraDistance
                Scen3_FinalTime += Scen3_ExtraTime * 100
                Scen3_EndingTime = Scen3_FinalTime / 1000
                Scen3_DistanceTravelledOverall = Scen3_InitialDistanceFromGroundValue - Scen3_CurrentDistanceFromGround
                Scen3_ExtraVelocity = Scen3_VerticalVelocityAtBeginningOfFrame + (Scen3_GravityValue * Scen3_ExtraTime)

                Scen3_DisplacementxStat -= abs(Scen3_EstimatedDistanceToPx - Scen3_DisplacementxStat)

                Scen3_KineticEnergy = Scen3_TotalEnergy
                Scen3_GravitationalEnergy = 0
        else:
            pygame.draw.rect(screen, '#c0e8ec', ((0, 0), (1200, 700)), 1000, 1)
            display_Scenario3()
            Scenario3ValuesUpdate()
            start_time = pygame.time.get_ticks()

    pygame.display.update()
    clock.tick(20)
