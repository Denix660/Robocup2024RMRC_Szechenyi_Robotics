import queue
import threading

import pygame
import cv2 as cv

pygame.init()
pygame.display.set_caption('Kamerák')
input_buffer = queue.Queue()

def feldogoz():
    while True:
        frame = input_buffer.get()
        cv.imshow('stream',frame)
    return


cap = cv.VideoCapture(0)
cap2 = cv.VideoCapture(2)


def make480p():
    cap.set(3,640)
    cap.set(4,480)
def make480p2():
    cap2.set(3,640)
    cap2.set(4,480)
def change_res(szelesseg,magassag):
    cap.set(3,szelesseg)
    cap.set(4,magassag)

def change_res2(szelesseg,magassag):
    cap2.set(3,szelesseg)
    cap2.set(4,magassag)

make480p()
make480p2()
change_res(640,480)
change_res2(640,480)



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



