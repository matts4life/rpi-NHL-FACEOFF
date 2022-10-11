import random
import time
import pygame
from pygame import mixer

mixer.init()


class Run:
    def __init__(self):
        self.drop = True
        self.sfx_1 = mixer.Sound("pickupCoin.wav")
        self.sfx_2 = mixer.Sound("pickupCoin(1).wav")

    def Drop(self):
        if self.drop:
            self.sfx_1.play()
            time.sleep(1)
            self.sfx_1.play()
            time.sleep(1)
            self.sfx_2.play()
            time.sleep(.5)
            print("yay")


run = Run()
run.Drop()
