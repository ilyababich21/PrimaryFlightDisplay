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
        # cap = cv2.VideoCapture(0)
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



