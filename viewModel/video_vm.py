import time
import random

import cv2
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QImage

from model.PoletModel import Polet
from resourse_path import resource_path


class VideoReader(QThread):
    change_pixmap_signal = pyqtSignal(QImage)

    def __init__(self, fps):
        super().__init__()
        self.fps = fps

    def run(self):

        cap = cv2.VideoCapture(resource_path("media/polet.mp4"))
        while True:
            ret, frame = cap.read()
            if ret:
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
                self.change_pixmap_signal.emit(qt_image)
                time.sleep(1 / self.fps)
            else:
                print("stop")
                break


class SensorsReader(QThread):
    params = pyqtSignal(Polet)

    def __init__(self):
        super().__init__()
        self.polet = Polet()

    def run(self):
        self.params.emit(self.polet)
        while True:
            # time.sleep(1)
            self.update_params()
            self.params.emit(self.polet)
            time.sleep(0.5)

    def update_params(self):
        # Update the display of the vehicle state
        self.polet.roll =random.uniform(-1, 1)
        self.polet.pitch = random.uniform(-1, 1)
        # self.polet.pitch = random.random()
        # pfd.heading = random.randint(0,90)
        self.polet.heading = random.randint(20, 50)
        self.polet.airspeed = random.randint(25, 50)
        self.polet.vspeed = random.random()  # variometr
        self.polet.alt = random.randint(500, 700)  # altmeter высотаметр
        # self.polet.skipskid = 5  # индикатор скольжения, с английского "скитаться"
        self.polet.skipskid = random.randint(-5, 7)  # индикатор скольжения, с английского "скитаться"
        self.polet.battery = 80
        self.polet.arm = True
