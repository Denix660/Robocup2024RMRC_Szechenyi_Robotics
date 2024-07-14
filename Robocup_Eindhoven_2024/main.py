import Adafruit_PCA9685
import pygame
from gpiozero import Motor, OutputDevice

from camera import Camera

camera = Camera()

"""pygame.init()
pygame.display.set_caption('Kamerák')
input_buffer = queue.Queue()


def feldogoz():
    while True:
        frame = input_buffer.get()
        cv.imshow('stream', frame)
    return


cap = cv.VideoCapture(0)
cap2 = cv.VideoCapture(2)


def make480p():
    cap.set(3, 640)
    cap.set(4, 480)


def make480p2():
    cap2.set(3, 640)
    cap2.set(4, 480)


def change_res(szelesseg, magassag):
    cap.set(3, szelesseg)
    cap.set(4, magassag)


def change_res2(szelesseg, magassag):
    cap2.set(3, szelesseg)
    cap2.set(4, magassag)


make480p()
make480p2()
change_res(640, 480)
change_res2(640, 480)

t = threading.Thread(target=feldogoz)

time = pygame.time.Clock()

while True:
    time.tick(60)
    ret, frame = flipped.read()
    ret2, frame2 = flipped2.read()
    input_buffer.put(frame)
    input_buffer.put(frame2)
    cv.imshow('frame1', frame)
    cv.imshow('frame2', frame2)
    if cv.waitKey(1) == ord('q'):
        break
        DestroyAllWindows()
        pygame.quit()

"""

pygame.init()
ablak = pygame.display.set_mode((300,300))
pygame.display.set_caption('Mozgás,kar')

speed = 0.9
motor1 = Motor(23,27)
motor1_enable = OutputDevice(5, initial_value=1)
motor2 = Motor(25,24)
motor2_enable = OutputDevice(17, initial_value=1)


pwm = Adafruit_PCA9685.PCA9685(busnum = 1)
# pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(70)

servo_min = 150  # Minimum servo pulse length
servo_max = 600  # Maximum servo pulse length

servo_angle = 5



servo_1 = 14
servo_2 = 13
servo_3 = 15
servo_4 = 12


servo1_degree = 0
servo2_degree = 0
servo3_degree = 0
servo4_degree = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print("a")
                    motor1.backward(speed)
                    motor2.forward(speed)
                if event.key == pygame.K_d:
                    print("d")
                    motor1.forward(speed)
                    motor2.backward(speed)
                if event.key == pygame.K_w:
                    print("w")
                    motor1.forward(speed)
                    motor2.forward(speed)
                if event.key == pygame.K_s:
                    print("s")
                    motor1.backward(speed)
                    motor2.backward(speed)
            #mozgás

                if event.key == pygame.K_r:
                    servo1_degree += servo_angle
                    servo_1_pwm = int((servo1_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_1, 0, servo_1_pwm)
                if event.key == pygame.K_f:
                    servo1_degree -= servo_angle
                    servo_1_pwm = int((servo1_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_1, 0, servo_1_pwm)

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
                    pwm.set_pwm(servo_3, 0, servo_3_pwm)
                if event.key == pygame.K_h:
                    servo3_degree -= servo_angle
                    servo_3_pwm = int((servo3_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_3, 0, servo_3_pwm)


                if event.key == pygame.K_u:
                    servo4_degree += 15
                    servo_4_pwm = int((servo4_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_4, 0, servo_4_pwm)
                if event.key == pygame.K_j:
                    servo4_degree -= 15
                    servo_4_pwm = int((servo4_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_4, 0, servo_4_pwm)
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
                    servo_2_pwm =int((servo2_degree / 180.0) * (servo_max - servo_min) + servo_min)
                    pwm.set_pwm(servo_2,0,servo_2_pwm)
                if event.key == pygame.K_g:
                    servo2_degree -= 0
                    servo_2_pwm =int((servo2_degree / 180.0) * (servo_max - servo_min) + servo_min)
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