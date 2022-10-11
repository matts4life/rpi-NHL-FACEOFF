import random
import time
import pygame
from pygame import mixer
from gpiozero import AngularServo

servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)

mixer.init()


class Run:
    def __init__(self):
        self.drop = True
        self.sfx_1 = mixer.Sound("pickupCoin.wav")
        self.sfx_2 = mixer.Sound("pickupCoin(1).wav")

    def Drop(self):
        if self.drop:
            while True:
                servo.angle = 90
                time.sleep(2)
                servo.angle = 0
                time.sleep(2)
                servo.angle = -90
                time.sleep(2)


run = Run()
run.Drop()
