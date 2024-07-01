import sys
import Adafruit_PCA9685
import pygame
import time

pygame.init()
ablak = pygame.display.set_mode((300, 300))
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

servo_min = 150  # Minimum servo pulse length
servo_max = 600  # Maximum servo pulse length

servo_angle = 10

servo_1 = 8
servo_2 = 9
servo_3 = 10
servo_4 = 11

servo1_degree = 0
servo2_degree = 0
servo3_degree = 0
servo4_degree = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                    servo1_degree += servo_angle
                    servo_1_pwm = int((servo1_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_1, 0, servo_1_pwm)
            if event.key == pygame.K_f:
                    servo1_degree -= servo_angle
                    servo_1_pwm = int((servo1_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_1,0,servo_1_pwm)
            if event.key == pygame.K_t:
                    servo2_degree += servo_angle
                    servo_2_pwm = int((servo2_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_2,0,servo_2_pwm)
            if event.key == pygame.K_g:
                    servo2_degree -= servo_angle
                    servo_2_pwm = int((servo2_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_2,0,servo_2_pwm)
            if event.key == pygame.K_z:
                    servo3_degree += servo_angle
                    servo_3_pwm = int((servo3_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_3,0,servo_3_pwm)
            if event.key == pygame.K_h:
                    servo3_degree -= servo_angle
                    servo_3_pwm = int((servo3_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_3,0,servo_3_pwm)
            if event.key == pygame.K_u:
                    servo4_degree += servo_angle
                    servo_4_pwm = int((servo4_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_4,0,servo_4_pwm)
            if event.key == pygame.K_j:
                    servo4_degree -= - servo_angle
                    servo_4_pwm = int((servo4_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_4,0,servo_4_pwm)
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                    servo1_degree += 0
                    servo_1_pwm = int((servo1_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_1,0,servo_1_pwm)
            if event.key == pygame.K_f:
                    servo1_degree -= 0
                    servo_1_pwm = int((servo1_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_1,0,servo_1_pwm)
            if event.key == pygame.K_t:
                    servo2_degree += 0
                    servo_2_pwm =int ((servo2_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_2,0,servo_2_pwm)
            if event.key == pygame.K_g:
                    servo2_degree -= 0
                    servo_2_pwm = int((servo2_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_2,0,servo_2_pwm)
            if event.key == pygame.K_z:
                    servo3_degree += 0
                    servo_3_pwm = int((servo3_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_3,0,servo_3_pwm)
            if event.key == pygame.K_h:
                    servo3_degree -= 0
                    servo_3_pwm = int((servo3_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_3,0,servo_3_pwm)
            if event.key == pygame.K_u:
                    servo4_degree += 0
                    servo_4_pwm = int((servo4_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_4,0,servo_4_pwm)
            if event.key == pygame.K_j:
                    servo4_degree -= 0
                    servo_4_pwm = int((servo4_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_4,0,servo_4_pwm)




