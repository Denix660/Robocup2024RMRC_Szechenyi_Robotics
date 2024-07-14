import queue
import threading

import pygame
import cv2 as cv

input_buffer = queue.Queue()

def feldogoz():
    while True:
        frame = input_buffer.get()
        cv.imshow('stream',frame)
    return



class Camera:
    def __init__(self):
        self.cap2 = cv.VideoCapture(2)
        self.cap1 = cv.VideoCapture(0)
        self.t = threading.Thread(target=feldogoz)

        self.launch()

    def launch(self):
        pygame.init()
        pygame.display.set_caption('Kamerák')

        self.make480p()
        self.make480p2()
        self.change_res(640, 480)
        self.change_res2(640, 480)

        self.time = pygame.time.Clock()

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

    def make480p(self):
        self.cap.set(3, 640)
        self.cap.set(4, 480)

    def make480p2(self):
        self.cap2.set(3, 640)
        self.cap2.set(4, 480)

    def change_res(self, szelesseg, magassag):
        self.cap.set(3, szelesseg)
        self.cap.set(4, magassag)

    def change_res2(self, szelesseg, magassag):
        self.cap2.set(3, szelesseg)
        self.cap2.set(4, magassag)



