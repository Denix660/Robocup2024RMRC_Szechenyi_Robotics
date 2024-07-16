import Adafruit_PCA9685
import pygame
from gpiozero import Motor, OutputDevice

#szija

pygame.init()
ablak = pygame.display.set_mode((300,300))
pygame.display.set_caption('Mozgás,kar')

speed = 0.9
motor1 = Motor(23,27)
motor1_enable = OutputDevice(5, initial_value=1)
motor2 = Motor(25,24)
motor2_enable = OutputDevice(12, initial_value=1)


pwm = Adafruit_PCA9685.PCA9685(busnum = 1)
# pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

servo_min = 205  # Minimum servo pulse length
servo_max = 496  # Maximum servo pulse length

servo_angle = 5
fogokar_angle = 15

servo_1 = 12
servo_2 = 13
servo_3 = 14
servo_4 = 15


servo1_degree = 45
servo2_degree = 45
servo3_degree = 90
servo4_degree = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if speed < 0.9:
                        speed += 0.1
                        print(speed," is the current speed")
                elif event.key == pygame.K_DOWN:
                    if speed > 0.1:
                        speed -= 0.1
                        print(speed, "is the current speed")
                elif event.key == pygame.K_a:
                    print("a")
                    motor1.backward(speed)
                    motor2.forward(speed)
                elif event.key == pygame.K_d:
                    print("d")
                    motor1.forward(speed)
                    motor2.backward(speed)
                elif event.key == pygame.K_w:
                    print("w")
                    motor1.forward(speed)
                    motor2.forward(speed)
                elif event.key == pygame.K_s:
                    print("s")
                    motor1.backward(speed)
                    motor2.backward(speed)
            #mozgás

                elif event.key == pygame.K_r:
                    if servo1_degree < 180:
                        servo1_degree += servo_angle
                        servo_1_pwm = int((servo1_degree / 180.0) * (servo_max - servo_min) + servo_min)
                        print("szervo1 pwm:", servo_1_pwm)
                        pwm.set_pwm(servo_1, 0, servo_1_pwm)
                        print("1 szervó foka:", servo1_degree)


                elif event.key == pygame.K_f:
                    if servo1_degree > 0 :
                        servo1_degree -= servo_angle
                        servo_1_pwm = int((servo1_degree / 180.0) * (servo_max - servo_min) + servo_min)
                        print("szervo1 pwm:", servo_1_pwm)
                        pwm.set_pwm(servo_1, 0, servo_1_pwm)
                        print("1 szervó foka:", servo1_degree)


                elif event.key == pygame.K_t:
                    if servo2_degree < 180:
                        servo2_degree += servo_angle
                        servo_2_pwm = int((servo2_degree / 180.0) * (servo_max - servo_min) + servo_min)
                        print("szervo2 pwm:", servo_2_pwm)
                        pwm.set_pwm(servo_2,0,servo_2_pwm)
                        print("2 szervó foka:", servo2_degree)


                elif event.key == pygame.K_g:
                    if servo2_degree > 0:
                        servo2_degree -= servo_angle
                        servo_2_pwm = int((servo2_degree / 180.0) * (servo_max - servo_min) + servo_min)
                        print("szervo2 pwm:", servo_2_pwm)
                        pwm.set_pwm(servo_2,0,servo_2_pwm)
                        print("2 szervó foka:", servo2_degree)

                elif event.key == pygame.K_z:
                    if servo3_degree < 180:
                        servo3_degree += servo_angle
                        servo_3_pwm = int((servo3_degree / 180.0) * (servo_max - servo_min) + servo_min)
                        print("szervo3 pwm:", servo_3_pwm)
                        pwm.set_pwm(servo_3, 0, servo_3_pwm)
                        print("3 szervó foka:", servo3_degree)

                elif event.key == pygame.K_h:
                    if servo3_degree > 0:
                        servo3_degree -= servo_angle
                        servo_3_pwm = int((servo3_degree / 180.0) * (servo_max - servo_min) + servo_min)
                        print("szervo3 pwm:", servo_3_pwm)
                        pwm.set_pwm(servo_3, 0, servo_3_pwm)
                        print("3 szervó foka:", servo3_degree)

                elif event.key == pygame.K_u:
                    if servo4_degree < 180:
                        servo4_degree += fogokar_angle
                        servo_4_pwm = int((servo4_degree / 180.0) * (servo_max - servo_min) + servo_min)
                        print("szervo4 pwm:", servo_4_pwm)
                        pwm.set_pwm(servo_4, 0, servo_4_pwm)
                        print("4 szervó foka:", servo4_degree)
                elif event.key == pygame.K_j:
                    if servo4_degree > 0:
                        servo4_degree -= fogokar_angle
                        servo_4_pwm = int((servo4_degree / 180.0) * (servo_max - servo_min) + servo_min)
                        print("szervo4 pwm:", servo_4_pwm)
                        pwm.set_pwm(servo_4, 0, servo_4_pwm)
                        print("4 szervó foka:", servo4_degree)

            #kar
                if event.key == pygame.K_p:
                        pygame.quit()

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                        motor1.stop()
                        motor2.stop()
                if event.key == pygame.K_a:
                        motor1.stop()
                        motor2.stop()
                if event.key == pygame.K_w:
                        motor1.stop()
                        motor2.stop()
                if event.key == pygame.K_s:
                        motor1.stop()
                        motor2.stop()
