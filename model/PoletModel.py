import random
from time import sleep

from PyQt6.QtCore import QTimer


class Polet():
    def __init__(self):
        self.pitch = 0
        self.roll = 0
        self.skipskid = 0
        self.heading = 0
        self.airspeed = 0
        self.alt = 0
        self.vspeed = 0
        self.battery = 0
        self.arm = False


    def update_params(self,pitch:float=0,roll:float=0,skipskid:float=0,heading:float=0,airspeed:float=0,alt:float=0,vspeed:float=0,battery:float=0,arm:bool=False):
        self.pitch =pitch
        self.roll =roll
        self.skipskid =skipskid
        self.heading =heading
        self.airspeed =airspeed
        self.alt =alt
        self.vspeed =vspeed
        self.battery =battery
        self.arm = arm



